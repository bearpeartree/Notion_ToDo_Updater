import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Domain import Day as day
from Domain import Task as task
from Domain import Week as week
from Domain.Exceptions import IllegalCalendarWeek as ilw


def test_get_correct_day():
    new_week = week.Week(46, "Dezember", 2021)
    the_day = new_week.get_day("Montag")
    assert the_day.get_day_name() == "Montag"


def test_get_invalid_day():
    new_week = week.Week(42, "Dezember", 2021)
    with pytest.raises(ValueError):
        new_week.get_day("Hello")


def test_get_empty_day_name():
    new_week = week.Week(42, "Dezember", 2021)
    with pytest.raises(ValueError):
        new_week.get_day("")


def test_get_non_String_day():
    new_week = week.Week(42, "Dezember", 2022)
    with pytest.raises(ValueError):
        new_week.get_day(6)


def test_construct_invalid_calendar_week():
    with pytest.raises(ilw.IllegalCalendarWeekError):
        week.Week(100, "Januar", 2022)