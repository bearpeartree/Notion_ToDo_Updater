import requests
import json
import os
from datetime import date
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


def print_readable_json(json_object):
    print(json.dumps(json_object.json(), indent=2))


if __name__ == "__main__":
    main()