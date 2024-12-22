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

    

    