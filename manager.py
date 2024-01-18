def add_task(tasks, name_task):
    task = {"name": name_task, "status": False}
    tasks.append(task)
    print(f"\nTask {name_task} has been added successfully!")

def view_tasks(tasks):
    print("\nCurrent tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task['name']} - {'Completed' if task['status'] else 'Not Completed'}")

def update_task(tasks, index):
    # In progress
    pass

def complete_task(tasks, index):
    # In progress
    pass

tasks = []

# Criação do menu
while True:
    print("\n Task Manager Menu:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Update task")
    print("4. Complete task")
    print("5. Delete completed tasks")
    print("6. Exit")

    choice = input("\nEnter your choice: ")
# Choice 1
    if choice == "1":
        name_task = input("\nEnter the name of the task you would like to add: ")
        if name_task:
            add_task(tasks, name_task)
        else:
            print("\nTask name cannot be empty. Please try again.")
# Choice 2
    elif choice == "2":
        view_tasks(tasks)
# Choice 3
    elif choice == "3":
        index = int(input("\nEnter the task number you want to update: ")) - 1
        update_task(tasks, index)
# Choice 4
    elif choice == "4":
        index = int(input("\nEnter the task number you want to mark as complete: ")) - 1
        complete_task(tasks, index)
# Choice 5
    elif choice == "5":
        tasks = [task for task in tasks if not task['status']]
        print("\nCompleted tasks have been deleted.")
# Choice 6
    elif choice == "6":
        break
    else:
        print("\nInvalid choice. Please choose a valid option.")

print("\nCompleted Program")
