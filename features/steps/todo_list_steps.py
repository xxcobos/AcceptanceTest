from behave import *

# Importing the todo_list.py
from src import todo_list

@given('the task list is empty')
def step_impl(context):
    todo_list.remove_all_tasks()

@when('the user adds a task "{task_name}"')
def step_impl(context, task_name):
    todo_list.create_task(task_name)

@then('the task list should include "{task_name}"')
def step_impl(context, task_name):
    exists = any(task[0] == task_name for task in todo_list.TASKS)
    assert exists, f'Task "{task_name}" not found in the list.'

@when('the user displays all tasks')
def step_impl(context):
    todo_list.display_tasks()

@then('the output should show')
def step_impl(context):
    pass

@then('the task list should show task "{task_name}" as completed')
def step_impl(context, task_name):
    for task in todo_list.TASKS:
        if task[0] == task_name:
            assert task[1] == 'Completed', f'Task "{task_name}" is not marked as completed.'
            return
    assert False, f'Task "{task_name}" not found in the list.'

@when('the user removes all tasks')
def step_impl(context):
    todo_list.remove_all_tasks()

@then('the task list should be empty')
def step_impl(context):
    assert len(todo_list.TASKS) == 0, 'The list should be empty.'

@given('the task list contains tasks for listing')
def step_impl(context):
    todo_list.TASKS = [
        ("Buy groceries", "Pending"),
        ("Pay bills", "Pending")
    ]

@given('the task list contains tasks for marking completion')
def step_impl(context):
    todo_list.TASKS = [("Buy groceries", "Pending")]

@when('the user marks task "{task_name}" as completed')
def step_impl(context, task_name):
    todo_list.update_task_status(task_name)

@given('the task list contains tasks for clearing')
def step_impl(context):
    todo_list.TASKS = [
        ("Buy groceries", "Pending"),
        ("Pay bills", "Pending")
    ]

@given('the task list contains tasks for specific clearing')
def step_impl(context):
    todo_list.TASKS = [("Buy groceries", "Pending")]

@when('the user removes task "{task_name}" from the list')
def step_impl(context, task_name):
    for task in todo_list.TASKS:
        if task[0] == task_name:
            todo_list.TASKS.remove(task)
            return
    assert False, f'Task "{task_name}" not found.'

@given('the task list contains tasks with completed status')
def step_impl(context):
    todo_list.TASKS = [("Buy groceries", "Completed")]

@when('the user marks task "{task_name}" as pending')
def step_impl(context, task_name):
    for idx, task in enumerate(todo_list.TASKS):
        if task[0] == task_name:
            todo_list.TASKS[idx] = (task_name, "Pending")
            return
    assert False, f'Task "{task_name}" not found.'

@given('the task list contains tasks for completed listing')
def step_impl(context):
    todo_list.TASKS = [
        ("Buy groceries", "Completed"),
        ("Pay bills", "Pending")
    ]

@when('the user lists completed tasks')
def step_impl(context):
    print("Completed tasks:")
    for task in todo_list.TASKS:
        if task[1] == "Completed":
            print(task[0])

@then('the task list should not include task "{task_name}"')
def step_impl(context, task_name):
    exists = any(task[0] == task_name for task in todo_list.TASKS)
    assert not exists, f'Task "{task_name}" should not be in the list.'

@then('the task list should show task "{task_name}" as pending')
def step_impl(context, task_name):
    for task in todo_list.TASKS:
        if task[0] == task_name:
            assert task[1] == 'Pending', f'Task "{task_name}" is not marked as pending.'
            return
    assert False, f'Task "{task_name}" not found.'
