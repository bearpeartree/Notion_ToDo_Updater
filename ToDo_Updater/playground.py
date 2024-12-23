import Appservice.todo_service as ts

def main():
    service = ts.todo_service()
    new_week = service.create_new_week(23, 12, 2024)
    new_week2 = service.create_new_week(30, 12, 2024)
    new_week3 = service.create_new_week(6, 1, 2025)

    service.add_mundane_task("programmieren", "mittwoch", "23.12.2024", 3)
    service.add_mundane_task("Nachbereitung", "donnerstag", "23.12.2024", 3)

    mittwoch = new_week.get_day("mittwoch")
    mittwoch2 = new_week2.get_day("mittwoch")
    mittwoch3 = new_week3.get_day("mittwoch")
    donnerstag = new_week.get_day("donnerstag")
    donnerstag2 = new_week2.get_day("donnerstag")
    donnerstag3 = new_week3.get_day("donnerstag")

    task_names = []
    mittwoch_task = mittwoch.get_tasks()
    mittwoch2_task = mittwoch2.get_tasks()
    mittwoch3_task = mittwoch3.get_tasks()
    donnerstag_task = donnerstag.get_tasks()
    donnerstag2_task = donnerstag2.get_tasks()
    donnerstag3_task = donnerstag3.get_tasks()

    task_names.append(mittwoch_task[0].get_task_name())
    task_names.append(mittwoch2_task[0].get_task_name())
    task_names.append(mittwoch3_task[0].get_task_name())
    task_names.append(donnerstag_task[0].get_task_name())
    task_names.append(donnerstag2_task[0].get_task_name())
    task_names.append(donnerstag3_task[0].get_task_name())

    print(task_names)



if __name__ == "__main__":
    main()