# daily_reminder.py

# Prompt for a single task
task = input("Enter the task description: ")

# Prompt for the task's priority
priority = input("Enter the task's priority (high, medium, low): ").lower()

# Ask if the task is time-bound
time_bound = input("Is the task time-bound? (yes/no): ").lower()

# Process the task based on priority and time sensitivity
match priority:
    case 'high':
        reminder = f"The task '{task}' has a high priority."
    case 'medium':
        reminder = f"The task '{task}' has a medium priority."
    case 'low':
        reminder = f"The task '{task}' has a low priority."
    case _:
        reminder = f"The task '{task}' has an unknown priority."

# Modify the reminder if the task is time-bound
if time_bound == 'yes':
    reminder += " This task requires immediate attention today!"

# Provide the customized reminder
print(reminder)
