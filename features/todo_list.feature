Feature: To-Do List Management

    @taskAddition
    Scenario: Add a new task to the to-do list
        Given the to-do list is currently empty
        When a task "Buy groceries" is added by the user
        Then "Buy groceries" should be present in the to-do list

    @taskListing
    Scenario: Display all tasks in the to-do list
        Given the to-do list has the following tasks:
            | Task          |
            | Buy groceries |
            | Pay bills     |
        When the user requests to see all tasks
        Then the displayed tasks should include:
            | Task          |
            | Buy groceries |
            | Pay bills     |

    @taskCompletion
    Scenario: Mark a specific task as completed
        Given the to-do list includes:
            | Task          | Status  |
            | Buy groceries | Pending |
        When the user marks "Buy groceries" as completed
        Then the status of "Buy groceries" should be updated to completed

    @taskClearing
    Scenario: Remove all tasks from the to-do list
        Given the to-do list contains:
            | Task          |
            | Buy groceries |
            | Pay bills     |
        When the user clears the entire to-do list
        Then the to-do list should be completely empty

    @specificTaskRemoval
    Scenario: Remove a specific task from the to-do list
        Given the to-do list has:
            | Task          | Status  |
            | Buy groceries | Pending |
        When the user removes "Buy groceries" from the list
        Then "Buy groceries" should no longer appear in the to-do list

    @taskPending
    Scenario: Change a task status to pending
        Given the to-do list has:
            | Task          | Status    |
            | Buy groceries | Completed |
        When the user marks "Buy groceries" as pending
        Then the status of "Buy groceries" should be shown as pending

    @completedTasksListing
    Scenario: Display only completed tasks
        Given the to-do list has:
            | Task          | Status    |
            | Buy groceries | Completed |
            | Pay bills     | Pending   |
        When the user requests to see completed tasks
        Then the displayed completed tasks should include:
            | Task          |
            | Buy groceries |
