class json_builder:
    def __init__(self):
        self.json_builder = json_builder


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
    