import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import json_builder as j
from Appservice import todo_service as ts

# Hmmm ich will auch mal so wirklich testen (also wie ich es kenne so eine controller klasse oder so)

def main():
    jb = j.json_builder()
    new_json = jb.build_new_day_toggle("Montag", "06.12.2021")
    print(new_json)

    print()
    new_json_banner = jb.build_week_text("01", "30.12.2024", "05.01.2025")
    print(new_json_banner)

    print()
    new_json_weektext = jb.build_week_text("02", "06.01.2025", "12.01.2025")
    print(new_json_weektext)


    # print()
    # new_json_toggle_day = jb.build_new_day_toggle("Montag","1999.12.2021")
    # print(new_json_toggle_day)

    print()
    # todo_s = ts.todo_service()
    # todo_s.create_new_week(3, 2, 2025)
    # # print(todo_s.get_stored_weeks())
    # new_json_week = jb.build_new_week("6")
    # print(new_json_week)



if __name__ == "__main__":
    main()