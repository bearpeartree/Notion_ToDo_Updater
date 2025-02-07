import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest



from Infrastructure import json_builder as jb
from Appservice import todo_service as ts


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
    service = ts.todo_service()

    json_b = jb.json_builder(service)

    # Uh so funktioniert es nicht da das Objekt im json builder ein anderer ist als das was du außen erzeugst
    # daher müssen wir die interne dependency von der Funktion im json Builder wegmocken und zustand entsprechend setzen
    # erspart damit einem Zeit, Speicher und Nerven: Denn davor dachte ich irgendwas war mit dem Service falsch. Aber
    # Schlussendlich war der Fehler dass die Zustände mit dem internen Service Objekt ein anderer war als das was ich außen 
    # erzeugt hab.
    # TODO mocking!
    todo_s = ts.todo_service()
    todo_s.create_new_week(3, 2, 2025)

    tested_json = json_b.build_new_week("6")

    assert tested_json == {
        "children": [
            {
            "object": "block",
			"type": "paragraph",
			"paragraph": {
				"rich_text": [
					{
						"type": "text",
						"text": {
							"content": "Woche 06 / 03.02.25 - 09.02.25",
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