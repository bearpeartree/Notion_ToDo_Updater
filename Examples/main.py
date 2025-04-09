import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("NOTION_KEY")
page_id = os.getenv("NOTION_PAGE_ID")

# Header for each HTTP-Query
header = {
    "Authorization": "Bearer " + api_key,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

def main():
    base_url = "https://api.notion.com/v1/pages/"+ page_id

    response = requests.get(base_url, headers=header)
    print(response.status_code)
    print_readable_json(response)

    # Playground, Add new page to existing page
    # page_body = {
    #     "parent": { "page_id": page_id },
    #     "properties": {
    #         "title": {
    #       "title": [{ "type": "text", "text": { "content": "Hello World!" } }]
    #         }
    #     },
    #     "children": [
    #     {
    #       "object": "block",
    #       "type": "paragraph",
    #       "paragraph": {
    #         "rich_text": [{ "type": "text", "text": { "content": "This page was made using an APi call!" } }]
    #       }
    #     }
    #   ]
    # }
    # Add Kale-Description via API
#     page_body = {
#         "children": [
# 		{
# 			"object": "block",
# 			"type": "heading_2",
# 			"heading_2": {
# 				"rich_text": [{ "type": "text", "text": { "content": "Lacinato kale" } }]
# 			}
# 		},
# 		{
# 			"object": "block",
# 			"type": "paragraph",
# 			"paragraph": {
# 				"rich_text": [
# 					{
# 						"type": "text",
# 						"text": {
# 							"content": "Lacinato kale is a variety of kale with a long tradition in Italian cuisine, especially that of Tuscany. It is also known as Tuscan kale, Italian kale, dinosaur kale, kale, flat back kale, palm tree kale, or black Tuscan palm.",
# 							"link": { "url": "https://en.wikipedia.org/wiki/Lacinato_kale" }
# 						}
# 					}
# 				]
# 			}
# 		}
# 	]
#     }

#     new_page_resp = requests.patch(f"https://api.notion.com/v1/blocks/{page_id}/children", json=page_body, headers=header)
#     print_readable_json(new_page_resp)


#     # children anhängen kann man in einer Methode wegabstrahieren
#     page_heading_2 = {
#         "children": [
#             {
#                 "object": "block",
#                 "type": "heading_2",
#                 "heading_2": {
#                     "rich_text": [
#                         {
#                             "type": "text",
#                             "text": {
#                                 "content": "This is created by API",
#                                 "link": None
#                             },
#                             "annotations": {
#                                 "bold": False,
#                                 "italic": False,
#                                 "strikethrough": False,
#                                 "underline": False,
#                                 "code": False,
#                                 "color": "blue"
#                             },
#                             "plain_text": "This is created by API",
#                             "href": None
#                         }
#                     ],
#                     "color": "default",
#                     "is_toggleable": False
#                 }
#             }
#         ]
#     }
#     new_header_resp = requests.patch(f"https://api.notion.com/v1/blocks/{page_id}/children", json=page_heading_2, headers=header)
#     # print_readable_json(new_header_resp)


#     # Eine neue Woche zusammenbauen; hier sind die Bestandteile: 
#         # - die Wochenzahl Woche X / Startdatum - Enddatum (Dick, Unterstrichen, Hervorhebung)
#         # - 7 Toggles mit der Beschriftung "X-Tag - Datum" (Normal)

#     # Wochenzahltext
#     week_text = {
#         "children": [
#             {
# 			"object": "block",
# 			"type": "paragraph",
# 			"paragraph": {
# 				"rich_text": [
# 					{
# 						"type": "text",
# 						"text": {
# 							"content": "Woche 01 / 31.12.24 - 05.01.25",
#                             "link": None
# 						},
#                         "annotations": {
#                             "bold": True,
#         		            "italic": False,
#         		            "strikethrough": False,
#         		            "underline": True,
#         		            "color": "blue_background"
#                         }
# 					}
# 				]
# 			}
# 		}
#     ]
# }
    
#     one_day = {
#         "children": [
#             {
#                 "object": "block",
#                 "type": "toggle",
#                 "toggle": {
#                     "rich_text": [{
#                         "type": "text",
#                         "text": {
#                             "content": "Montag - 31.12.2024",
#                             "link": None
#                         },
#                          "annotations": {
#                             "bold": False,
#         		            "italic": False,
#         		            "strikethrough": False,
#         		            "underline": False,
#         		            "color": "default"
#                         }
#                     }]
#                 }
#             }
#         ]
#     }


    a_full_new_week = {
        "children": [
            {
            "object": "block",
			"type": "paragraph",
			"paragraph": {
				"rich_text": [
					{
						"type": "text",
						"text": {
							"content": "Woche 01 / 31.12.24 - 05.01.25",
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
                            "content": "Montag - 30.12.2024",
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
                            "content": "Dienstag - 31.12.2024",
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
                            "content": "Mittwoch - 01.01.2025",
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
                            "content": "Donnerstag - 02.01.2025",
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
                            "content": "Freitag - 03.01.2025",
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
                            "content": "Samstag - 03.01.2025",
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
                            "content": "Sonntag - 05.01.2025",
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
    print(f"==== API KEY: {api_key}")
    print(f"==== PAGE ID: {page_id}")


    new_header_resp = requests.patch(f"https://api.notion.com/v1/blocks/{page_id}/children", json=a_full_new_week, headers=header)
    print_readable_json(new_header_resp)

    # todo_block = {
    #     "children": [
    #         {
    #             "object": "block",
    #             "type": "toggle",
    #             "toggle": {
    #                 "rich_text": [{
    #                     "type": "text",
    #                     "text": {
    #                         "content": "Montag - 30.12.2024",
    #                         "link": None
    #                     },
    #                      "annotations": {
    #                         "bold": False,
    #     		            "italic": False,
    #     		            "strikethrough": False,
    #     		            "underline": False,
    #     		            "color": "default"
    #                     }}],
    #                     "children": [{
    #                         "object": "block",
    #                         "type": "to_do",
    #                         "has_children": False,
    #                         "to_do": {
    #                             "rich_text": [{
    #                                 "type": "text",
    #                                 "text": {
    #                                     "content": "Finish programming",
    #                                     "link": None
    #                                 }
    #                             }]
    #                         }
    #                     }]
                    
    #             }
    #         }
    #     ]
    # }

    # new_todo_resp = requests.patch(f"https://api.notion.com/v1/blocks/{page_id}/children", json=todo_block, headers=header)
    # print_readable_json(new_todo_resp)


def print_readable_json(json_object):
    print(json.dumps(json_object.json(), indent=2))


if __name__ == "__main__":
    main()