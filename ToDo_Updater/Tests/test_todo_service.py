import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Appservice import todo_service as ts
from Domain.Exceptions import IllegalCalendarWeek as icw
from Domain.day_factory import day_factory
from Domain.Day import Day
import datetime
from datetime import date

def test_valid_creation_new_week():
    service = ts.todo_service()
    service.create_new_week(7, 10, 2024)
    assert len(service.weeks_in_store) == 1


def test_seven_days_new_week():
    service = ts.todo_service()
    new_week = service.create_new_week(7, 10, 2024)
    assert len(new_week.get_days()) == 7


def test_correct_day_conv():
    service = ts.todo_service()
    a_date = service.convert_to_date("6.12.2022")
    date_time_a_date = a_date.get_date()
    assert date_time_a_date.date().month == 12
    assert date_time_a_date.date().day == 6
    assert date_time_a_date.date().year == 2022


def test_correct_task():
    service = ts.todo_service()
    new_week = service.create_new_week(6, 12, 2021)

    service.add_task_to_day("clean room", "6.12.2021")

    test_day = new_week.get_day("montag")
    assert len(test_day.get_tasks()) == 1


def test_empty_task():
    service = ts.todo_service()
    service.create_new_week(6, 12, 2021)

    with pytest.raises(ValueError):
        service.add_task_to_day("", "6.12.2021")


def test_add_tasks_multiple_week_days():
    service = ts.todo_service()
    new_week = service.create_new_week(6, 12, 2021)

    service.add_task_to_day("Vorlesung nachbereiten", "6.12.2021")
    service.add_task_to_day("Zimmer aufräumen", "8.12.2021")

    montag = new_week.get_day("montag")
    mittwoch = new_week.get_day("mittwoch")

    montag_tasks = montag.get_tasks()
    mittwoch_tasks = mittwoch.get_tasks()
    montag_task_name = montag_tasks[0].get_task_name()
    mittwoch_task_name = mittwoch_tasks[0].get_task_name()


    assert montag_task_name == "Vorlesung nachbereiten"
    assert mittwoch_task_name == "Zimmer aufräumen"


def test_add_tasks_to_same_day():
    service = ts.todo_service()
    new_week = service.create_new_week(6, 12, 2021)

    service.add_task_to_day("Vorlesung nachbereiten", "6.12.2021")
    service.add_task_to_day("programmieren", "6.12.2021")

    montag = new_week.get_day("montag")
    montag_tasks = montag.get_tasks()
    tasks_name = []
    for m in montag_tasks:
        tasks_name.append(m.get_task_name())

    assert set(tasks_name) == set(["Vorlesung nachbereiten", "programmieren"])
    

def test_mark_existing_task_as_done():
    service = ts.todo_service()
    new_week = service.create_new_week(6, 12, 2021)
    service.add_task_to_day("Vorlesung nachbereiten", "6.12.2021")

    service.mark_task_as_done("Vorlesung nachbereiten", "6.12.2021")
    montag = new_week.get_day("montag")
    montag_tasks = montag.get_tasks()
    
    assert montag_tasks[0].is_finished() == True


def test_mark_non_existing_task_as_done():
    service = ts.todo_service()
    service.create_new_week(6, 12, 2021)
    service.add_task_to_day("Vorlesung nachbereiten", "6.12.2021")

    with pytest.raises(ValueError):
        service.mark_task_as_done("Hallo", "6.12.2021")


def test_mark_empty_task_as_done():
    service = ts.todo_service()
    service.create_new_week(6, 12, 2021)
    service.add_task_to_day("Vorlesung nachbereiten", "6.12.2021")
    with pytest.raises(ValueError):
        service.mark_task_as_done("", "6.12.2021")


def test_basic_move_to_next_day():
    service = ts.todo_service()
    new_week = service.create_new_week(6, 12, 2021)
    service.add_task_to_day("Vorlesung nachbereiten", "6.12.2021")
    service.add_task_to_day("programmieren", "6.12.2021")

    service.move_undone_tasks_to_next_day("6.12.2021")

    dienstag = new_week.get_day("dienstag")
    dienstag_tasks = dienstag.get_tasks()

    task_names = []
    for t in dienstag_tasks:
        task_names.append(t.get_task_name())

    assert set(task_names) == set(["Vorlesung nachbereiten", "programmieren"])


def test_partial_move_to_next_day():
    service = ts.todo_service()
    new_week = service.create_new_week(6, 12, 2021)
    service.add_task_to_day("Vorlesung nachbereiten", "6.12.2021")
    service.add_task_to_day("programmieren", "6.12.2021")
    service.add_task_to_day("Wäsche waschen", "6.12.2021")

    service.mark_task_as_done("Wäsche waschen", "6.12.2021")
    service.mark_task_as_done("programmieren", "6.12.2021")

    service.move_undone_tasks_to_next_day("6.12.2021")


    dienstag = new_week.get_day("dienstag")
    dienstag_tasks = dienstag.get_tasks()

    task_names = []
    for t in dienstag_tasks:
        task_names.append(t.get_task_name())

    assert set(task_names) == set(["Vorlesung nachbereiten"])


def test_edged_move_to_next_day():
    service = ts.todo_service()
    new_week = service.create_new_week(26, 2, 2024)
    service.add_task_to_day("Geschirr spülen", "29.2.2024")

    service.move_undone_tasks_to_next_day("29.2.2024")

    freitag = new_week.get_day("freitag")
    freitag_tasks = freitag.get_tasks()

    task_names = []
    for t in freitag_tasks:
        task_names.append(t.get_task_name())

    assert set(task_names) == set(["Geschirr spülen"])


def test_recurrent_task_easy_case_3_weeks():
    service = ts.todo_service()
    new_week = service.create_new_week(2, 12, 2024)
    new_week2 = service.create_new_week(9, 12, 2024)
    new_week3 = service.create_new_week(16, 12, 2024)

    service.add_mundane_task("Geschirr spülen", "montag", "2.12.2024", 3)

    montag = new_week.get_day("montag")
    montag2 = new_week2.get_day("montag")
    montag3 = new_week3.get_day("montag")

    task_names = []
    montag_task = montag.get_tasks()
    montag2_task = montag2.get_tasks()
    montag3_task = montag3.get_tasks()

    task_names.append(montag_task[0].get_task_name())
    task_names.append(montag2_task[0].get_task_name())
    task_names.append(montag3_task[0].get_task_name())

    assert set(task_names) == set(["Geschirr spülen"])


def test_recurrent_task_edged_weeks():
    service = ts.todo_service()
    new_week = service.create_new_week(23, 12, 2024)
    new_week2 = service.create_new_week(30, 12, 2024)
    new_week3 = service.create_new_week(6, 1, 2025)

    service.add_mundane_task("programmieren", "mittwoch", "23.12.2024", 3)
    service.add_mundane_task("Nachbereitung", "donnerstag", "23.12.2024", 3)

    mittwoch = new_week.get_day("mittwoch")
    mittwoch2 = new_week2.get_day("mittwoch")
    mittwoch3 = new_week3.get_day("mittwoch")
    donnerstag = new_week.get_day("donnerstag")
    donnerstag2 = new_week2.get_day("donnerstag")
    donnerstag3 = new_week3.get_day("donnerstag")

    task_names = []
    mittwoch_task = mittwoch.get_tasks()
    mittwoch2_task = mittwoch2.get_tasks()
    mittwoch3_task = mittwoch3.get_tasks()
    donnerstag_task = donnerstag.get_tasks()
    donnerstag2_task = donnerstag2.get_tasks()
    donnerstag3_task = donnerstag3.get_tasks()

    task_names.append(mittwoch_task[0].get_task_name())
    task_names.append(mittwoch2_task[0].get_task_name())
    task_names.append(mittwoch3_task[0].get_task_name())
    task_names.append(donnerstag_task[0].get_task_name())
    task_names.append(donnerstag2_task[0].get_task_name())
    task_names.append(donnerstag3_task[0].get_task_name())

    assert set(task_names) == set(["programmieren", "Nachbereitung"])


def test_move_existing_task_to_another_day():
    service = ts.todo_service()
    new_week = service.create_new_week(2, 12, 2024)
    service.add_task_to_day("Nachbereitung", "5.12.2024")

    service.move_task_of_today_to_any_other_day("Nachbereitung", "5.12.2024", "8.12.2024")

    sonntag = new_week.get_day("sonntag")
    sonntag_tasks = sonntag.get_tasks()

    assert sonntag_tasks[0].get_task_name() == "Nachbereitung"


def test_move_non_existing_task_throws_exception():
    service = ts.todo_service()
    service.create_new_week(2, 12, 2024)
    service.add_task_to_day("Nachbereitung", "5.12.2024")

    with pytest.raises(ValueError):
        service.move_task_of_today_to_any_other_day("Wäsche", "5.12.2024", "6.12.2024")


def test_move_existing_task_to_non_existing_goal_date():
    service = ts.todo_service()
    service.create_new_week(2, 12, 2024)
    service.add_task_to_day("Nachbereitung", "5.12.2024")

    with pytest.raises(KeyError):
        service.move_task_of_today_to_any_other_day("Nachbereitung", "5.12.2024", "12.12.2024")