import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Domain import Day as day
from Domain import Task as task
from Domain import Week as week


def test_add_task():
    monday = day.Day("Montag", 52)
    monday.add_task("Zimmer dekorieren")
    assert monday.get_tasks() == ["Zimmer dekorieren"]
