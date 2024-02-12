"""Title: PyRemind: Simple Console Todo List Manager"""
import datetime

# Initialize an empty dictionary to store reminders
reminders = {}

# Function to add a new reminder
def add_reminder(name, due_date):
    reminders[name] = due_date
    print(f"Reminder '{name}' added successfully for {due_date}.")

# Function to view all reminders
def view_reminders():
    if reminders:
        print("Current Reminders:")
        for name, due_date in reminders.items():
            print(f"{name}: {due_date}")
    else:
        print("No reminders.")

# Function to update a reminder's due date
def update_reminder(name, new_due_date):
    reminders[name] = new_due_date
    print(f"Due date for reminder '{name}' updated successfully to {new_due_date}.")

# Function to delete a reminder
def delete_reminder(name):
    del reminders[name]
    print(f"Reminder '{name}' deleted successfully.")

# Function to prompt the user for input
def get_user_input():
    try:
        name = input("Enter the reminder name: ").strip()
        date_str = input("Enter the due date (YYYY-MM-DD): ").strip()
        due_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        return name, due_date
    except ValueError:
        print("Invalid input. Please enter the reminder name and due date in the correct format.")
        return None, None

# Function to get due reminders
def get_due_reminders():
    today = datetime.date.today()
    due_reminders = {name: due_date for name, due_date in reminders.items() if due_date <= today}
    return due_reminders

# Main loop to interact with the user
while True:
    print("\nREMINDER MANAGEMENT SYSTEM")
    print("1. Add Reminder")
    print("2. View Reminders")
    print("3. Update Reminder")
    print("4. Delete Reminder")
    print("5. View Due Reminders")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ").strip()

    if choice == '1':
        name, due_date = get_user_input()
        if name and due_date:
            add_reminder(name, due_date)
    elif choice == '2':
        view_reminders()
    elif choice == '3':
        name, _ = get_user_input()
        if name in reminders:
            _, new_due_date = get_user_input()
            if new_due_date:
                update_reminder(name, new_due_date)
        else:
            print(f"Reminder '{name}' not found.")
    elif choice == '4':
        name, _ = get_user_input()
        if name in reminders:
            delete_reminder(name)
        else:
            print(f"Reminder '{name}' not found.")
    elif choice == '5':
        due_reminders = get_due_reminders()
        if due_reminders:
            print("Due Reminders:")
            for name, due_date in due_reminders.items():
                print(f"{name}: {due_date}")
        else:
            print("No due reminders.")
    elif choice == '6':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
