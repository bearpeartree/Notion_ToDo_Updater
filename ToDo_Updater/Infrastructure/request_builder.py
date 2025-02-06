import json_builder as j

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

    print()
    new_json_week = jb.build_new_week("02")
    print(new_json_week)



if __name__ == "__main__":
    main()