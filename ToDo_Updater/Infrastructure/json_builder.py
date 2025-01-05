from Domain.Color import color
from random import randint

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
