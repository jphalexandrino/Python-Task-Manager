from colorama import Fore, Style, init

def add_task(tasks, name_task):
    task = {"name": name_task, "status": False}
    tasks.append(task)
    print(f"\n{Fore.GREEN}Task {Fore.BLUE}{name_task} {Fore.GREEN}has been added successfully!")

def view_tasks(tasks):
    print(f"\n{Fore.BLUE}Current tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{Fore.YELLOW}{i}. {task['name']} - {f'{Fore.GREEN}✓ Completed' if task['status'] else f'{Fore.RED}× Not Completed'}")

def update_task(tasks, index):
    try:
        if 0 <= index < len(tasks):
            new_name = input(f"\n{Fore.GREEN}Enter the new name for the task: {Fore.BLUE}")
            if new_name:
                tasks[index]["name"] = new_name
                print(f"\n{Fore.GREEN}Task {Fore.BLUE}{index + 1} {Fore.GREEN}updated successfully!")
            else:
                print(f"\n{Fore.RED}Task name cannot be empty. Update failed.")
        else:
            print(f"\n{Fore.RED}Invalid task number. Update failed.")
    except ValueError:
        print(f"\n{Fore.RED}Invalid input. Please enter a valid task number.")

def complete_task(tasks, index):
    try:
        if 0 <= index < len(tasks):
            tasks[index]["status"] = True
            print(f"\nTask {index + 1} marked as complete!")
        else:
            print(f"\n{Fore.RED}Invalid task number. Mark as complete failed.")
    except ValueError:
        print(f"\n{Fore.RED}Invalid input. Please enter a valid task number.")

def delete_completed_tasks(tasks):
    tasks = [task for task in tasks if not task['status']]
    print(f"\n{Fore.RED}Completed tasks have been deleted.")
    return tasks

def confirm_exit():
    answer = input(f"\n{Fore.RED}Are you sure you want to exit? (yes/no): {Fore.BLUE}")
    return answer.lower() == 'yes'

tasks = []

# Criação do menu
while True:
    print(f"\n {Fore.BLUE} Task Manager Menu:")
    print(f"\n{Fore.YELLOW}1. {Fore.GREEN}Add task")
    print(f"{Fore.YELLOW}2. {Fore.GREEN}View tasks")
    print(f"{Fore.YELLOW}3. {Fore.GREEN}Update task")
    print(f"{Fore.YELLOW}4. {Fore.GREEN}Complete task")
    print(f"{Fore.YELLOW}5. {Fore.GREEN}Delete completed tasks")
    print(f"{Fore.YELLOW}6. {Fore.RED}Exit")

    choice = input(f"\n{Fore.GREEN}Enter your choice: {Fore.BLUE}")

    if choice == "1":
        name_task = input(f"\n{Fore.GREEN}Enter the name of the task you would like to add:{Fore.BLUE} ")
        if name_task:
            add_task(tasks, name_task)
        else:
            print(f"\n{Fore.RED}Task name cannot be empty. Please try again.")
    elif choice == "2":
        view_tasks(tasks)
    elif choice == "3":
        try:
            index = int(input(f"{Fore.GREEN}\nEnter the task number you want to update: {Fore.BLUE}")) - 1
            update_task(tasks, index)
        except ValueError:
            print(f"\n{Fore.RED}Invalid input. Please enter a valid task number.")
    elif choice == "4":
        try:
            index = int(input(f"\n{Fore.GREEN}Enter the task number you want to mark as complete: {Fore.BLUE}")) - 1
            complete_task(tasks, index)
        except ValueError:
            print(f"\n{Fore.RED}Invalid input. Please enter a valid task number.")
    elif choice == "5":
        tasks = delete_completed_tasks(tasks)
    elif choice == "6":
        if confirm_exit():
            print(f"\n{Fore.RED}Exiting the program.")
            break
    else:
        print(f"\n{Fore.RED}Invalid choice. Please choose a valid option.")

print(f"\n {Fore.WHITE}Completed Program")
