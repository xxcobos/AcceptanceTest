TASKS = []

def create_task(name):
    TASKS.append((name, "Pending"))

def display_tasks():
    print("Index - Task - Status")
    if TASKS:
        for idx, task in enumerate(TASKS):
            print(f"{idx + 1} - {task[0]} - {task[1]}")
    else:
        print("No tasks available.")

def update_task_status(name):
    display_tasks()
    task_found = False
    for idx, task in enumerate(TASKS):
        if task[0] == name:
            TASKS[idx] = (name, "Completed")
            task_found = True
            break

    if not task_found:
        print(f'Task "{name}" not found.')
    else:
        display_tasks()

def remove_all_tasks():
    TASKS.clear()

def show_menu():
    print("Task Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Remove All Tasks")
    print("5. Exit")

def run_app():
    show_menu()
    choice = int(input("Select an option: "))
    while choice != 5:
        if choice == 1:
            task_name = input("Enter task name: ")
            create_task(task_name)
        elif choice == 2:
            display_tasks()
        elif choice == 3:
            task_name = input("Enter task name to mark as completed: ")
            update_task_status(task_name)
        elif choice == 4:
            remove_all_tasks()

        show_menu()
        choice = int(input("Select an option: "))

if __name__ == "__main__":
    run_app()
