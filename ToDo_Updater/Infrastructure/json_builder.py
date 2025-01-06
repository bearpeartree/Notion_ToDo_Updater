import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Domain.Color import color
from random import randint
from Appservice import todo_service as ts
import json

class json_builder:
    def __init__(self):
        self.json_builder = json_builder

    
    def __get_random_background_color(self):
        bc_list = [color_member for color_member in color]
        rand_index = randint(0, len(bc_list))
        return bc_list[rand_index]


    # string - Wochentag (Montag...), Datum
    def build_new_day_toggle(self, week_day, full_date):
        return {
                "object": "block",
                "type": "toggle",
                "toggle": {
                    "rich_text": [{
                        "type": "text",
                        "text": {
                            "content": week_day + " - " + full_date,
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


    # string - Kalenderwoche, Startdatum, Enddatum
    def build_week_text(self, calendar_week, start_week, end_week):

        random_background_color = self.__get_random_background_color()

        return {
            "object": "block",
			"type": "paragraph",
			"paragraph": {
				"rich_text": [
					{
						"type": "text",
						"text": {
							"content": "Woche " + calendar_week + " / " + start_week + " - " + end_week,
                            "link": None
						},
                        "annotations": {
                            "bold": True,
        		            "italic": False,
        		            "strikethrough": False,
        		            "underline": True,
        		            "color": random_background_color.value
                        }
					}
				]
			}
        }


    def build_new_week(self, calendar_week):
        service = ts.todo_service()
        correct_week = service.get_correct_week(int(calendar_week)) # Week Object with Day Objects
        new_week = {
            "children": []
        }

        # add the week text
        montag = correct_week.get_day("montag")
        sonntag = correct_week.get_day("sonntag")
        formatted_montag = montag.format_datetime_to_string()
        formatted_sonntag = sonntag.format_datetime_to_string()
        new_week["children"].append(self.build_week_text(calendar_week,formatted_montag, formatted_sonntag))

        # add the individual days
        days = correct_week.get_days()

        for day in days:
            new_week["children"].append(self.build_new_day_toggle(day.get_week_day().capitalize(), day.format_datetime_to_string()))


        return json.dumps(new_week)
