# daily_reminder.py
# Objective: Provide a customized reminder for a single task using match-case, conditionals, and loops.

# Prompt user for input
task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Process the task using match-case
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unspecified priority"

# Modify reminder if time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"

# Print the customized reminder using a loop (to emphasize repetition)
for i in range(1):  # loop runs once, but shows how loops can be used
    print("Reminder:", reminder)