from dotenv import find_dotenv, load_dotenv
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import notion_client
import json_builder


def main():
    print("Willkommen zum Notion-ToDo-Updater!")
    dotenv_path = find_dotenv()

    api_key = input("Bitte gib die API-Key deines Workspaces ein: ")
    page_id = input("Bitte gib die Page-Id der Seite von der du die Todos verwalten willst: ")

    # with open("../../.env", 'w') as f:
    with open(dotenv_path, 'w') as f:
        f.write(f"NOTION_KEY = {api_key}\n")
        f.write(f"NOTION_PAGE_ID = {page_id}")

    # zum testen
    print(os.getenv("NOTION_KEY"))
    print(os.getenv("NOTION_PAGE_ID"))

if __name__ == "__main__":
    main()