from behave import *

# Importando el módulo de lista de tareas
from src import todo_list

@given('the to-do list is currently empty')
def step_impl(context):
    # Reiniciando la lista de tareas antes de cada prueba
    todo_list.clear_all_tasks()

@when('a task "{task_name}" is added by the user')
def step_impl(context, task_name):
    todo_list.add_new_task(task_name)

@then('"{task_name}" should appear in the to-do list')
def step_impl(context, task_name):
    # Verificando si la tarea está en la lista
    task_exists = any(task[0] == task_name for task in todo_list.LIST_TASKS)
    assert task_exists, f'Task "{task_name}" not found in the list.'

@when('the user requests to see all tasks')
def step_impl(context):
    # Este paso ejecutará la función para listar todas las tareas
    todo_list.list_all_task()

@then('the displayed output should include')
def step_impl(context):
    # Este paso se usa para verificar la salida detallada cuando se listan tareas
    pass

@then('the task "{task_name}" should be marked as completed')
def step_impl(context, task_name):
    # Verificando que la tarea esté marcada como completada
    for task in todo_list.LIST_TASKS:
        if task[0] == task_name:
            assert task[1] == 'Completed', f'Task "{task_name}" is not marked as completed.'
            return

    assert False, f'Task "{task_name}" not found in the list.'

@when('the user clears all tasks')
def step_impl(context):
    todo_list.clear_all_tasks()

@then('the to-do list should be empty')
def step_impl(context):
    # Verificando que la lista de tareas esté vacía
    assert not todo_list.LIST_TASKS, 'The to-do list is not empty.'

@given('the to-do list contains the following tasks listAll')
def step_impl(context):
    # Inicializando la lista con tareas predefinidas
    todo_list.LIST_TASKS = [
        ("Buy groceries", "Pending"),
        ("Pay bills", "Pending")
    ]

@given('the to-do list has tasks markTaskCompleted')
def step_impl(context):
    # Inicializando la lista con una tarea pendiente
    todo_list.LIST_TASKS = [("Buy groceries", "Pending")]

@when('a task "{task_name}" is marked as completed')
def step_impl(context, task_name):
    todo_list.mark_task(task_name)

@given('the to-do list contains tasks for clearing')
def step_impl(context):
    # Inicializando la lista con tareas para pruebas de eliminación
    todo_list.LIST_TASKS = [
        ("Buy groceries", "Pending"),
        ("Pay bills", "Pending")
    ]

@given('the to-do list has a task for specific removal')
def step_impl(context):
    # Inicializando la lista con una tarea específica
    todo_list.LIST_TASKS = [("Buy groceries", "Pending")]

@when('the user removes task "{task_name}" from the list')
def step_impl(context, task_name):
    for task in todo_list.LIST_TASKS:
        if task[0] == task_name:
            todo_list.LIST_TASKS.remove(task)
            return
    assert False, f'Task "{task_name}" not found in the list.'

@given('the to-do list has tasks for marking as pending')
def step_impl(context):
    # Inicializando la lista con una tarea completada para volver a pendiente
    todo_list.LIST_TASKS = [("Buy groceries", "Completed")]

@when('a task "{task_name}" is set back to pending')
def step_impl(context, task_name):
    for index, task in enumerate(todo_list.LIST_TASKS):
        if task[0] == task_name:
            todo_list.LIST_TASKS[index] = (task_name, "Pending")
            return
    assert False, f'Task "{task_name}" not found in the list.'

@given('the to-do list contains the following completed tasks')
def step_impl(context):
    # Inicializando la lista con tareas completadas y pendientes
    todo_list.LIST_TASKS = [
        ("Buy groceries", "Completed"),
        ("Pay bills", "Pending")
    ]

@when('the user requests to see completed tasks')
def step_impl(context):
    print("Completed tasks:")
    for task in todo_list.LIST_TASKS:
        if task[1] == "Completed":
            print(task[0])

@then('the list should not include task "{task_name}"')
def step_impl(context, task_name):
    # Verificando que la tarea no esté en la lista
    task_exists = any(task[0] == task_name for task in todo_list.LIST_TASKS)
    assert not task_exists, f'Task "{task_name}" is still in the list, but should not be.'

@then('the task "{task_name}" should be displayed as pending')
def step_impl(context, task_name):
    # Verificando que la tarea esté marcada como pendiente
    for task in todo_list.LIST_TASKS:
        if task[0] == task_name:
            assert task[1] == 'Pending', f'Task "{task_name}" is not marked as pending.'
            return

    assert False, f'Task "{task_name}" not found in the list.'
