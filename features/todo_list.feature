Feature: Task Management

    @addTask
    Scenario: Add a task to the list
        Given the task list is empty
        When the user adds a task "Buy groceries"
        Then the task list should include "Buy groceries"

    @listAll
    Scenario: View all tasks
        Given the task list contains tasks for listing
            | Task          |
            | Buy groceries |
            | Pay bills     |
        When the user displays all tasks
        Then the output should show
            | Tasks         |
            | Buy groceries |
            | Pay bills     |

    @markTaskCompleted
    Scenario: Mark a task as completed
        Given the task list contains tasks for marking completion
            | Task          | Status  |
            | Buy groceries | Pending |
        When the user marks task "Buy groceries" as completed
        Then the task list should show task "Buy groceries" as completed

    @clearList
    Scenario: Clear the entire task list
        Given the task list contains tasks for clearing
            | Task          |
            | Buy groceries |
            | Pay bills     |
        When the user removes all tasks
        Then the task list should be empty

    @clearSpecificTask
    Scenario: Remove a specific task
        Given the task list contains tasks for specific clearing
            | Task          | Status  |
            | Buy groceries | Pending |
        When the user removes task "Buy groceries" from the list
        Then the task list should not include task "Buy groceries"

    @markTaskAsPending
    Scenario: Mark a task as pending
        Given the task list contains tasks with completed status
            | Task          | Status    |
            | Buy groceries | Completed |
        When the user marks task "Buy groceries" as pending
        Then the task list should show task "Buy groceries" as pending

    @listCompleted
    Scenario: List completed tasks
        Given the task list contains tasks for completed listing
            | Task          | Status    |
            | Buy groceries | Completed |
            | Pay bills     | Pending   |
        When the user lists completed tasks
        Then the output should show
            | Tasks         |
            | Buy groceries |
