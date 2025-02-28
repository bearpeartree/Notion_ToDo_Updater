import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
import json

from Infrastructure import json_builder as jb
from Domain.Exceptions.DateFormatError import DateFormatError 
from Domain.Exceptions.DayNotFoundError import DayNotFoundError
from Domain.Exceptions.IllegalCalendarWeek import IllegalCalendarWeekError

def test_build_correct_new_day_toggle(mocker):
    mocked_service = mocker.patch('Appservice.todo_service')
    json_b = jb.json_builder(mocked_service)

    test_jobject = json_b.build_new_day_toggle("Montag", "06.12.2021")

    assert test_jobject == {
                "object": "block",
                "type": "toggle",
                "toggle": {
                    "rich_text": [{
                        "type": "text",
                        "text": {
                            "content": "Montag - 06.12.2021",
                            "link": None
                        },
                         "annotations": {
                            "bold": False,
        		            "italic": False,
        		            "strikethrough": False,
        		            "underline": False,
        		            "color": "default"
                        }
                    }]
                }
            }


def test_build_invalid_new_day_toggle(mocker):
    mocked_service = mocker.patch('Appservice.todo_service')

    json_b = jb.json_builder(mocked_service)

    with pytest.raises(DateFormatError):
        json_b.build_new_day_toggle("BlaBlub", "some_day")


def test_invalid_weekday_new_day_toggle(mocker):
    mocked_service = mocker.patch('Appservice.todo_service')

    json_b = jb.json_builder(mocked_service)

    with pytest.raises(DayNotFoundError):
        json_b.build_new_day_toggle("blub", "05.02.2025")


def test_new_day_toggle_3_digits_day_invalid(mocker):
    mocked_service = mocker.patch("Appservice.todo_service")

    json_b = jb.json_builder(mocked_service)

    with pytest.raises(DateFormatError):
        json_b.build_new_day_toggle("Montag", "199.24.2021")


def test_new_valid_week(mocker):
    fake_service = mocker.patch("Appservice.todo_service")

    # Setup for fake_service
    string_dates = [("Montag", "03.02.2025"), ("Dienstag", "04.02.2025"), ("Mittwoch", "05.02.2025"),
                    ("Donnerstag", "06.02.2025"), ("Freitag", "07.02.2025"), ("Samstag", "08.02.2025"), ("Sonntag", "09.02.2025")]
    fake_service.convert_week_to_day_string.return_value = string_dates

    
    json_b = jb.json_builder(fake_service)

    mocker.patch.object(jb.json_builder, '_json_builder__get_random_background_color', return_value = "blue_background")
    

    tested_json = json_b.build_new_week("6")

    # Redundant? Du brauchst nur den JSON String?
    with open("json_files_for_tests/new_valid_week.json") as f:
        expected_json = json.load(f)
    

    assert tested_json == json.dumps(expected_json)


def test_non_existent_week_creation(mocker):
    fake_service = mocker.patch("Appservice.todo_service")

    fake_service.convert_week_to_day_string.side_effect = KeyError("Woche existiert nicht!")

    json_b = jb.json_builder(fake_service)

    with pytest.raises(KeyError):
        json_b.build_new_week("2")


def test_non_numeric_weeknumber_creation(mocker):
    fake_service = mocker.patch("Appservice.todo_service")

    fake_service.convert_week_to_day_string.side_effect = ValueError("Woche muss eine Zahl sein!")

    json_b = jb.json_builder(fake_service)

    with pytest.raises(ValueError):
        json_b.build_new_week("blablub")


def test_non_valid_weeknumber_creation(mocker):
    fake_service = mocker.patch("Appservice.todo_service")

    json_b = jb.json_builder(fake_service)

    with pytest.raises(IllegalCalendarWeekError):
        json_b.build_new_week("1000")


def test_add_new_todo_to_date(mocker):
    fake_service = mocker.patch("Appservice.todo_service")

    json_b = jb.json_builder(fake_service)

    with open("json_files_for_tests/new_valid_todo_week.json") as f:
        expected_json = json.load(f)

    with open("json_files_for_tests/new_valid_week.json") as e:
        empty_weekdays = json.load(e)

    to_be_tested_json = json_b.add_todo_to_date(empty_weekdays, "Finish programming", "05.02.2025")

    assert to_be_tested_json == json.dumps(expected_json)


def test_add_new_todo_to_nonexistent_date(mocker):
    fake_service = mocker.patch("Appservice.todo_service")

    json_b = jb.json_builder(fake_service)

    with open("json_files_for_tests/new_valid_week.json") as e:
        empty_weekdays = json.load(e)
    
    with pytest.raises(DayNotFoundError):
        json_b.add_todo_to_date(empty_weekdays, "blub", "10.02.2025")


def test_add_new_todo_to_invalid_date_format(mocker):
    fake_service = mocker.patch("Appservice.todo_service")

    json_b = jb.json_builder(fake_service)

    with open("json_files_for_tests/new_valid_week.json") as e:
        empty_weekdays = json.load(e)

    with pytest.raises(DateFormatError):
        json_b.add_todo_to_date(empty_weekdays, "bla", "48234.122.203.222")


def test_add_new_multiple_todos_to_multipe_dates(mocker):
    fake_service = mocker.patch("Appservice.todo_service")

    json_b = jb.json_builder(fake_service)

    with open("json_files_for_tests/new_valid_multiple_todo_week.json") as f:
        expected_json = json.load(f)

    with open("json_files_for_tests/new_valid_week.json") as e:
        empty_weekdays = json.load(e)

    first_add = json_b.add_todo_to_date(empty_weekdays, "Programmierung", "05.02.2025")
    second_add = json_b.add_todo_to_date(json.loads(first_add), "Kochen", "06.02.2025")

    assert second_add == json.dumps(expected_json)