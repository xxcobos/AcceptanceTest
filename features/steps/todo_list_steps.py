from todo_list import TaskListManager

@given('the task list is empty')
def step_impl(context):
    context.task_manager = TaskListManager()
    context.task_manager.tasks = []

@when('the user adds a task "{task_description}"')
def step_impl(context, task_description):
    context.task_manager.add_task(task_description)

@then('the task list should contain "{task_description}"')
def step_impl(context, task_description):
    assert task_description in [task.description for task in context.task_manager.tasks]

@given('the task list contains the following tasks:')
def step_impl(context):
    context.task_manager = TaskListManager()
    for row in context.table:
        context.task_manager.add_task(row['Task'])

@when('the user lists all tasks')
def step_impl(context):
    context.output = context.task_manager.list_tasks()

@then('the output should include:')
def step_impl(context):
    for row in context.table:
        assert row['Task'] in [task.description for task in context.output]

@when('the user marks the task "{task_description}" as complete')
def step_impl(context, task_description):
    context.task_manager.mark_task_complete(task_description)

@then('the task list should display "{task_description}" as completed')
def step_impl(context, task_description):
    assert any(task.description == task_description and task.status == "Completed" for task in context.task_manager.tasks)

@when('the user marks the task "{task_description}" as in progress')
def step_impl(context, task_description):
    context.task_manager.mark_task_in_progress(task_description)

@then('the task list should display "{task_description}" as in progress')
def step_impl(context, task_description):
    assert any(task.description == task_description and task.status == "In Progress" for task in context.task_manager.tasks)

@when('the user clears all tasks')
def step_impl(context):
    context.task_manager.tasks = []
    context.task_manager.save_tasks()

@then('the task list should be empty')
def step_impl(context):
    assert len(context.task_manager.tasks) == 0

@when('the user updates the task "{old_task}" to "{new_task}"')
def step_impl(context, old_task, new_task):
    for task in context.task_manager.tasks:
        if task.description == old_task:
            task.description = new_task
            context.task_manager.save_tasks()
            return
    raise ValueError("Task not found")
