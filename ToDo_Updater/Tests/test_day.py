import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Domain.Day import Day as day
from Domain.day_factory import day_factory
from Domain.Task import Task
from Domain import Week as week


def test_add_task():
    monday = day_factory.create_day(2022, 12, 6)
    monday.add_task("Zimmer dekorieren")
    tasks_for_monday = monday.get_tasks()
    assert tasks_for_monday[0].get_task_name() == "Zimmer dekorieren"


def test_add_noname_task():
    new_week = week.Week(24, 2, 2024)
    monday = new_week.get_day("Montag")
    with pytest.raises(ValueError):
        monday.add_task("")


def test_correct_week_calendar():
    new_day = day_factory.create_day(2021, 12, 6)
    assert new_day.get_week_calendar() == 49