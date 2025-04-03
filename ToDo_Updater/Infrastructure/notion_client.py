import requests
import os
from dotenv import load_dotenv
import json

from Infrastructure import json_builder
from Appservice import todo_service

load_dotenv()
api_key = os.getenv("NOTION_KEY")
page_id = os.getenv("NOTION_PAGE_ID")

# Header for each HTTP-Query
header = {
    "Authorization": "Bearer " + api_key,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

BASE_URL = "https://api.notion.com/v1/pages/"+ page_id

class notion_client:
    def __init__(self, todo_service, json_builder):
        self.todo_service = todo_service
        self.json_builder = json_builder
    

    def post_new_week(self, start_day, month, year):
        # ts = create new week
        new_week = self.todo_service.create_new_week(start_day, month, year)

        # jb = create new json week
        json_week = self.json_builder.build_new_week(new_week.get_week_calendar())


        # send to notion server
        new_week_resp = requests.patch(f"https://api.notion.com/v1/blocks/{page_id}/children", json=json_week, headers=header)

        # zum testen
        print(json.dumps(new_week_resp.json(), indent=2))

        return new_week_resp

    
