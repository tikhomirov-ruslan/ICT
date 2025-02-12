# Task 8: To-Do List Manager Using a Loop 

todo_list = []

while True:
        print("\nChoose what to-do:")
        print("1. Add a new to-do item")
        print("2. View all to-do items")
        print("3. Remove a to-do item by its number")
        print("q. Exit")

        choice = input()

        if choice == "1":
            new_task = input("Enter a new to-do item: ")
            todo_list.append(new_task)
            print("Success!")

        elif choice == "2":
            if todo_list:
                print("\nList of to-do items:")
                for i, task in enumerate(todo_list, start=1):
                    print(f"{i}. {task}")
            else:
                print("The list is empty!")

        elif choice == "3":
            if todo_list:
                try:
                    task_number = int(input("Enter a task number to delete: "))
                    if 1 <= task_number <= len(todo_list):
                        removed_task = todo_list.pop(task_number - 1)
                        print(f"The '{removed_task}' to-do item is deleted!")
                    else:
                        print("Error! There is no task with this number")
                except ValueError:
                    print("Error! Please enter a valid task number")
            else:
                print("The list is empty!")

        elif choice.lower() == "q":
            print("Exitting the programm...")
            break

        else:
            print("Error! Try again later")