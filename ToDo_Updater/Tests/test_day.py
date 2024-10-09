import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Domain.Day import Day as day
from Domain.day_factory import day_factory
from Domain import Task as task
from Domain import Week as week


def test_add_task():
    monday = day_factory.create_day(2022, 12, 6)
    monday.add_task("Zimmer dekorieren")
    assert monday.get_tasks() == ["Zimmer dekorieren"]


def test_add_noname_task():
    new_week = week.Week(24, 2, 2024)
    monday = new_week.get_day("Montag")
    with pytest.raises(ValueError):
        monday.add_task("")