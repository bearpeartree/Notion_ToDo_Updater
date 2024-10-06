import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Appservice import todo_service as ts

def test_valid_creation_new_week():
    service = ts.todo_service()
    new_week = service.create_new_week(52, "Dezember")
    assert new_week is not None


def test_week_seven_days():
    service = ts.todo_service()
    new_week = service.create_new_week(52, "Dezember")
    assert len(new_week.get_days()) == 7
