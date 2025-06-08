import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Domain.Day import Day as day
from Domain.day_factory import day_factory
from Domain.Task import Task
from Domain import Week as week
from Domain.Exceptions.TaskNotFoundError import TaskNotFoundError


def test_add_task():
    monday = day_factory.create_day(2022, 12, 6)
    monday.add_task("Zimmer dekorieren")
    tasks_for_monday = monday.get_tasks()
    assert tasks_for_monday[0].get_task_name() == "Zimmer dekorieren"


def test_add_noname_task():
    new_week = week.Week(26, 2, 2024)
    monday = new_week.get_day("Montag")
    with pytest.raises(ValueError):
        monday.add_task("")


def test_correct_week_calendar():
    new_day = day_factory.create_day(2021, 12, 6)
    assert new_day.get_week_calendar() == 49


def test_correct_week_day():
    new_day = day_factory.create_day(2021, 12, 6)
    assert new_day.get_week_day() == "montag"


def test_found_task():
    mittwoch = day_factory.create_day(2025, 2, 5)
    mittwoch.add_task("Programmieren")
    mittwoch.add_task("Stricken")
    mittwoch.add_task("Kochen")

    found_task = mittwoch.find_correct_task("Programmieren")
    assert found_task.get_task_name() == "Programmieren" 


def test_non_existent_task_fail():
    mittwoch = day_factory.create_day(2025, 2, 5)
    mittwoch.add_task("Programmieren")
    mittwoch.add_task("Stricken")
    mittwoch.add_task("Kochen")

    with pytest.raises(TaskNotFoundError):
        mittwoch.find_correct_task("blub")