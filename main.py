tasks = []

while True:
    print("\n Task Manager")
    print("\n1. Add Task\n2.View Tasks\n3.Delete Task\n4.Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        option = input ("What Task would you like to add: ")
        tasks.append(option)
        print ("successfully added!")

    elif choice == "2":
        if not tasks:
            print("No tasks added yet")
        else:
            for number, task in enumerate(tasks, start = 1):
                print(f"{number}. {task}")

    elif choice == "3":
        number = int(input("Enter task number: "))
        tasks.pop(number - 1)

    elif choice == "4":
        print ("Goodbye")
        break
    else:
        print ("invalid choice")
      