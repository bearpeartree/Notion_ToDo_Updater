import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest

from Infrastructure import json_builder as jb
from Appservice import todo_service as ts


def test_build_correct_new_day_toggle():
    json_b = jb.json_builder()

    test_jobject = json_b.build_new_day_toggle("Montag", "06.12.2021")

    assert test_jobject == {
                "object": "block",
                "type": "toggle",
                "toggle": {
                    "rich_text": [{
                        "type": "text",
                        "text": {
                            "content": "Montag - 06.12.2021",
                            "link": None
                        },
                         "annotations": {
                            "bold": False,
        		            "italic": False,
        		            "strikethrough": False,
        		            "underline": False,
        		            "color": "default"
                        }
                    }]
                }
            }


def test_build_invalid_new_day_toggle():
    json_b = jb.json_builder()

    with pytest.raises(ValueError):
        json_b.build_new_day_toggle("BlaBlub", "some_day")