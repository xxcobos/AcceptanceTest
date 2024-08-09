task_list = []

def add_task(name):
    task_list.append((name, "Pending"))

def display_tasks():
    print("Index - Task - Status")
    if task_list:
        for index, (task, status) in enumerate(task_list):
            print(f"{index + 1} - {task} - {status}")
    else:
        print("No tasks available")

def complete_task(name):
    display_tasks()
    found = False
    for index, (task, status) in enumerate(task_list):
        if task == name:
            task_list[index] = (name, "Completed")
            found = True
            break

    if not found:
        print(f'Task "{name}" not found.')
    else:
        display_tasks()

def remove_all_tasks():
    task_list.clear()

def show_menu():
    print("Task Manager")
    print("1. Add a task")
    print("2. Show all tasks")
    print("3. Mark a task as done")
    print("4. Remove all tasks")
    print("5. Exit")

def main():
    show_menu()
    option = int(input("Select an option: "))
    while option != 5:
        if option == 1:
            task_name = input("Enter task name: ")
            add_task(task_name)
        elif option == 2:
            display_tasks()
        elif option == 3:
            task_name = input("Enter task name to mark as done: ")
            complete_task(task_name)
        elif option == 4:
            remove_all_tasks()

        show_menu()
        option = int(input("Select an option: "))

if __name__ == "__main__":
    main()
