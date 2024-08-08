Feature: Task List Management
  Scenario: Add a new task to the task list
    Given the task list is empty
    When the user adds a task "Pick up dry cleaning"
    Then the task list should contain "Pick up dry cleaning"

  Scenario: Display all tasks in the task list
    Given the task list contains the following tasks:
      | Task                |
      | Pick up dry cleaning |
      | Pay the electricity bill |
    When the user lists all tasks
    Then the output should include:
      | Task                |
      | Pick up dry cleaning |
      | Pay the electricity bill |

  Scenario: Mark a task as complete
    Given the task list contains the following tasks:
      | Task                | Status    |
      | Pick up dry cleaning | Pending |
    When the user marks the task "Pick up dry cleaning" as complete
    Then the task list should display "Pick up dry cleaning" as completed

  Scenario: Remove all tasks from the task list
    Given the task list contains the following tasks:
      | Task                |
      | Pick up dry cleaning |
      | Pay the electricity bill |
    When the user clears all tasks
    Then the task list should be empty

  Scenario: Mark a task as in progress
    Given the task list contains the following tasks:
      | Task                | Status    |
      | Pick up dry cleaning | Pending |
    When the user marks the task "Pick up dry cleaning" as in progress
    Then the task list should display "Pick up dry cleaning" as in progress

  Scenario: Update a task's details
    Given the task list contains the following tasks:
      | Task                |
      | Pick up dry cleaning |
    When the user updates the task "Pick up dry cleaning" to "Pick up laundry"
    Then the task list should contain "Pick up laundry"
