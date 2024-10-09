import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Domain.Day import Day as day
from Domain.Task import Task as task
from Domain import Week as week
from Domain.Exceptions import IllegalDay


def test_correct_week_cal():
    new_week = week.Week(7, 10, 2024)
    assert new_week.get_week_calendar() == 41


def test_get_nonvalid_day():
    new_week = week.Week(7, 10, 2024)
    with pytest.raises(IllegalDay.IllegalDayException):
        new_week.get_day("Hello")