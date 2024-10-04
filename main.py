import requests
import json
import os
from datetime import date
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("NOTION_KEY")
page_id = os.getenv("NOTION_PAGE_ID")

def main():
    base_url = "https://api.notion.com"



if __name__ == "__main__":
    main()