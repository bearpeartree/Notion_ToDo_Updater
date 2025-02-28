import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import json
import re

from Domain.Color import color
from random import randint
from Appservice import todo_service
from Domain.Exceptions.DateFormatError import DateFormatError 
from Domain.Exceptions.DayNotFoundError import DayNotFoundError
from Domain.Exceptions.IllegalCalendarWeek import IllegalCalendarWeekError

class json_builder:
    def __init__(self, td_service):
        self.service = td_service
        self.json_builder = json_builder

    
    def __get_random_background_color(self):
        bc_list = [color_member for color_member in color]
        rand_index = randint(0, len(bc_list)-1)
        return bc_list[rand_index]


    # string - Wochentag (Montag...), Datum
    def build_new_day_toggle(self, week_day, full_date):
        pattern = re.compile("(^[0-9][0-9]).([0-9][0-9]).([1-9][0-9][0-9][0-9])")
        
        if not re.match(pattern, full_date):
            raise DateFormatError("Format des Datums falsch!")
        elif week_day.lower() not in ["montag", "dienstag", "mittwoch", "donnerstag", "freitag", "samstag", "sonntag"]:
            raise DayNotFoundError("Tag existiert nicht!")

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
    

    def create_new_todo(self, task_name):
        return {
            "object": "block",
            "type": "to_do",
            "has_children": False,
            "to_do": {
                "rich_text": [{
                    "type": "text",
                    "text": {
                        "content": task_name,
                        "link": None
                    }
                }]
            }
        }
    

    # Erwartet: JSON String für eine Woche, task_name als String
    # Return: JSON String mit der eingefügten ToDo
    def add_todo_to_date(self, json_week, task_name, date):
        json_week_first_child = json_week["children"]
        for day in json_week_first_child:
            if day["type"] == "toggle":
                current_date = day["toggle"]["rich_text"][0]["text"]["content"]
                if date in current_date:
                    # Wenn keine Children als Liste vorhanden
                    if "children" not in day["toggle"]:
                        day["toggle"]["children"] = []
                    day["toggle"]["children"].append(self.create_new_todo(task_name))
                    return json.dumps(json_week)
        
        raise DayNotFoundError("Datum nicht in der Woche gefunden!")


    # string - Kalenderwoche, Startdatum, Enddatum
    def build_week_text(self, calendar_week, start_week, end_week):
        new_digit = calendar_week
        if(len(new_digit) == 1):
            new_digit = "0" + calendar_week 


        random_background_color = self.__get_random_background_color()

        return {
            "object": "block",
			"type": "paragraph",
			"paragraph": {
				"rich_text": [
					{
						"type": "text",
						"text": {
							"content": "Woche " + new_digit + " / " + start_week + " - " + end_week,
                            "link": None
						},
                        "annotations": {
                            "bold": True,
        		            "italic": False,
        		            "strikethrough": False,
        		            "underline": True,
        		            "color": random_background_color
                        }
					}
				]
			}
        }


    def build_new_week(self, calendar_week):
        if calendar_week.isnumeric() == False:
            raise ValueError("Kalenderwoche muss eine Zahl sein!")
        if int(calendar_week) <= 0 or int(calendar_week) > 52:
            raise IllegalCalendarWeekError("Kalenderwoche ist eine ungültige Zahl!")
        string_days_of_week = self.service.convert_week_to_day_string(int(calendar_week))

        new_week = {
            "children": []
        }

        # add the week text (header)
        montag = string_days_of_week[0]
        sonntag = string_days_of_week[len(string_days_of_week)-1]
        new_week["children"].append(self.build_week_text(calendar_week,montag[1], sonntag[1]))

        # add the individual days as toggles
        for day in string_days_of_week:
            new_week["children"].append(self.build_new_day_toggle(day[0], day[1]))


        # return json string
        return json.dumps(new_week)
