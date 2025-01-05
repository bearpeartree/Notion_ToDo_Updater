import json_builder as j

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



if __name__ == "__main__":
    main()