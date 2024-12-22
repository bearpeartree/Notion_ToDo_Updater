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
