import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Appservice import todo_service as ts
from Domain.Exceptions import IllegalCalendarWeek as icw

def test_valid_creation_new_week():
    service = ts.todo_service()
    new_week = service.create_new_week(7, 10, 2024)
    assert new_week is not None


def test_week_seven_days():
    service = ts.todo_service()
    new_week = service.create_new_week(7, 10, 2024)
    assert len(new_week.get_days()) == 7


def test_invalid_week_creation():
    service = ts.todo_service()
    with pytest.raises(ValueError):
        service.create_new_week(60, 100, 3)