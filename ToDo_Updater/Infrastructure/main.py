from dotenv import find_dotenv
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import notion_client
import json_builder
from Appservice import todo_service


def remove_leading_zeros(number):
    if '0' in number:
        return number.removeprefix('0')
    return number


def main():
    print("Willkommen zum Notion-ToDo-Updater!")
    dotenv_path = find_dotenv()

    if os.getenv("NOTION_KEY") == None and os.getenv("NOTION_PAGE_ID") == None:
        api_key = input("Bitte gib die API-Key deines Workspaces ein: ")
        page_id = input("Bitte gib die Page-Id der Seite von der du die Todos verwalten willst: ")

        # with open("../../.env", 'w') as f:
        with open(dotenv_path, 'w') as f:
            f.write(f"NOTION_KEY = {api_key}\n")
            f.write(f"NOTION_PAGE_ID = {page_id}")

    # zum testen
    # print(os.getenv("NOTION_KEY"))
    # print(os.getenv("NOTION_PAGE_ID"))

    # Commands, zurzeit nur neue Woche hinzufügen
    print()
    print("Hier eine Übersicht von verfügbaren Commands:")
    print("==================================================")
    print("reset == Umgebungsvariablen ändern")
    print("new_week == Neue Woche mit leeren Todos hinzufügen")
    my_command = input()


    # execute
    service = todo_service.todo_service()
    j_builder = json_builder.json_builder(service)
    client = notion_client.notion_client(service, j_builder)

    match my_command:
        case "reset":
            api_key = input("Neue API-Key eingeben: ")
            page_id = input("Neue Page-Id eingeben: ")
            with open(dotenv_path, 'w') as f:
                f.write(f"NOTION_KEY = {api_key}\n")
                f.write(f"NOTION_PAGE_ID = {page_id}")
        case "new_week":
            day = remove_leading_zeros(input("Tag eingeben (Montag der neuen Woche, als Zahl): ")) # keine führende Nullen 
            month = remove_leading_zeros(input("Monat eingeben als Zahl: ")) # keine führende Nullen, und als Zahl
            year = input("Jahr eingeben: ") # 202..

            client.post_new_week(int(day), int(month), int(year))
        case _:
            print("Der Command existert nicht.")


if __name__ == "__main__":
    main()