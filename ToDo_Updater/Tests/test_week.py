import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Domain.Day import Day as day
from Domain.Task import Task as task
from Domain import Week as week
from Domain.Exceptions import IllegalDay
from Domain.Exceptions import DayNotFoundError


def test_correct_week_cal():
    new_week = week.Week(7, 10, 2024)
    assert new_week.get_week_calendar() == 41


def test_get_nonvalid_day():
    new_week = week.Week(7, 10, 2024)
    with pytest.raises(IllegalDay.IllegalDayException):
        new_week.get_day("Hello")


def test_add_todo_to_day():
    new_week = week.Week(5,5, 2025)
    new_week.add_todo_to_day("montag", "programmieren")

    test_day = new_week.get_day("montag")
    assert test_day.get_all_tasks_names() == ["programmieren"]


def test_add_noname_task_to_day():
    new_week = week.Week(3, 2, 2025)

    with pytest.raises(ValueError):
        new_week.add_todo_to_day("mittwoch", "")