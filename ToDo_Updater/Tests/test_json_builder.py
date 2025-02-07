import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
import json



from Infrastructure import json_builder as jb


def test_build_correct_new_day_toggle(mocker):
    mocked_service = mocker.patch('Appservice.todo_service')
    json_b = jb.json_builder(mocked_service)

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


def test_build_invalid_new_day_toggle(mocker):
    mocked_service = mocker.patch('Appservice.todo_service')

    json_b = jb.json_builder(mocked_service)

    with pytest.raises(ValueError):
        json_b.build_new_day_toggle("BlaBlub", "some_day")


def test_new_day_toggle_3_digits_day_invalid(mocker):
    mocked_service = mocker.patch("Appservice.todo_service")

    json_b = jb.json_builder(mocked_service)

    with pytest.raises(ValueError):
        json_b.build_new_day_toggle("Montag", "199.24.2021")


def test_new_valid_week(mocker):
    fake_service = mocker.patch("Appservice.todo_service")

    # Setup for fake_service
    string_dates = [("Montag", "03.02.2025"), ("Dienstag", "04.02.2025"), ("Mittwoch", "05.02.2025"),
                    ("Donnerstag", "06.02.2025"), ("Freitag", "07.02.2025"), ("Samstag", "08.02.2025"), ("Sonntag", "09.02.2025")]
    fake_service.convert_week_to_day_string.return_value = string_dates

    
    json_b = jb.json_builder(fake_service)

    mocker.patch.object(jb.json_builder, '_json_builder__get_random_background_color', return_value = "blue_background")
    

    tested_json = json_b.build_new_week("6")

    expected_json = {
        "children": [
            {
            "object": "block",
			"type": "paragraph",
			"paragraph": {
				"rich_text": [
					{
						"type": "text",
						"text": {
							"content": "Woche 06 / 03.02.2025 - 09.02.2025",
                            "link": None
						},
                        "annotations": {
                            "bold": True,
        		            "italic": False,
        		            "strikethrough": False,
        		            "underline": True,
        		            "color": "blue_background"
                        }
					}
				]
			}
            },
            {
                "object": "block",
                "type": "toggle",
                "toggle": {
                    "rich_text": [{
                        "type": "text",
                        "text": {
                            "content": "Montag - 03.02.2025",
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
            },
            {
                "object": "block",
                "type": "toggle",
                "toggle": {
                    "rich_text": [{
                        "type": "text",
                        "text": {
                            "content": "Dienstag - 04.02.2025",
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
            },
            {
                "object": "block",
                "type": "toggle",
                "toggle": {
                    "rich_text": [{
                        "type": "text",
                        "text": {
                            "content": "Mittwoch - 05.02.2025",
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
            },
            {
                "object": "block",
                "type": "toggle",
                "toggle": {
                    "rich_text": [{
                        "type": "text",
                        "text": {
                            "content": "Donnerstag - 06.02.2025",
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
            },
            {
                "object": "block",
                "type": "toggle",
                "toggle": {
                    "rich_text": [{
                        "type": "text",
                        "text": {
                            "content": "Freitag - 07.02.2025",
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
            },
            {
                "object": "block",
                "type": "toggle",
                "toggle": {
                    "rich_text": [{
                        "type": "text",
                        "text": {
                            "content": "Samstag - 08.02.2025",
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
            },
            {
                "object": "block",
                "type": "toggle",
                "toggle": {
                    "rich_text": [{
                        "type": "text",
                        "text": {
                            "content": "Sonntag - 09.02.2025",
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
        ]
    }

    assert tested_json == json.dumps(expected_json)