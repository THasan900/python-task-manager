import json
try:
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
except FileNotFoundError:
    tasks = []

def save_task(task_list):
    with open("tasks.json", "w") as file:
        json.dump(task_list, file, indent=4)

while True:
    print("\n Task Manager")
    print("\n1. Add Task\n2.View Tasks\n3.Delete Task\n4.Complete Task\n5.Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        option = input ("What Task would you like to add: ")
        new_task = {
            "name" : option,
            "completed" : False
        }
        tasks.append(new_task)
        save_task(tasks)
        print ("successfully added!")

    elif choice == "2":
        if not tasks:
            print("No tasks added yet")
        else:
            for number, task in enumerate(tasks, start = 1):
                if task["completed"]:
                    print(f"{number}. {task["name"]} - Completed")
                else:
                    print(f"{number}. {task["name"]} - Not Completed")

    elif choice == "3":
        if not tasks:
            print("no tasks added yet")
        else:
            try:
                number = int(input("Enter task number: "))
                if 1 <= number <=len(tasks):
                    tasks.pop(number - 1)
                    save_task(tasks)
                    print("Task deleted successfully")
                else:
                    print("Not a valid Task number!")
            except ValueError:
                print("please Enter a number!")

    elif choice == "4":
        if not tasks:
            print("no tasks added yet")
        else:
            try:
                number = int(input("Enter task number: "))
                if 1 <= number <=len(tasks):
                    tasks[number - 1]["completed"] = True
                    save_task(tasks)
                    print("Task completed successfulyy")
                else:
                    print("Not a valid Task number!")
            except ValueError:
                print("Please enter a Number!")


    elif choice == "5":
        print ("Goodbye")
        break
    else:
        print ("invalid choice")
      