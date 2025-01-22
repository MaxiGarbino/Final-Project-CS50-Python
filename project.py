import json
import sys

FILENAME = "tasks.json"

def main():
    load_tasks()
    while True:
        try:
            print("\nMenu:")
            print("1. Add task")
            print("2. View all tasks")
            print("3. Mark task as completed")
            print("4. Exit")
            choice = input("Choose an option: ")
            
            if choice == "1":
                add_task()
            elif choice == "2":
                view_tasks()
            elif choice == "3":
                complete_task()
            elif choice == "4":
                save_tasks()
                print("Tasks saved. Goodbye!")
                sys.exit(0)
            else:
                print("Invalid option. Please enter a number between 1 and 4.")
        except KeyboardInterrupt:
            print("\nProgram interrupted by user. Exiting.")
            sys.exit(0)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

tasks = []

def load_tasks():
    try:
        with open(FILENAME, "r") as file:
            global tasks
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    except json.JSONDecodeError:
        print("Error: The tasks file is corrupted. Starting with an empty task list.")
        tasks = []

def save_tasks():
    try:
        with open(FILENAME, "w") as file:
            json.dump(tasks, file, indent=4)
    except Exception as e:
        print(f"Error saving tasks: {e}")

from datetime import datetime

from datetime import datetime

def add_task():
    try:
        name = input("Task name: ").strip()
        if not name:
            raise ValueError("Task name cannot be empty.")
        
        description = input("Task description: ").strip()
        
        deadline = input("Deadline (YYYY-MM-DD): ").strip()
        if not deadline:
            raise ValueError("Deadline cannot be empty.")
        
        try:
            deadline_date = datetime.strptime(deadline, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Please enter a date in the format YYYY-MM-DD.")
        
        current_date = datetime.now()
        if deadline_date <= current_date:
            raise ValueError("Deadline must be after the current date.")
        
        task = {"name": name, "description": description, "deadline": deadline, "completed": False}
        tasks.append(task)
        print("Task added successfully.")
    except ValueError as e:
        print(f"Input error: {e}")


def view_tasks():
    if not tasks:
        print("No tasks available.")
        return
    try:
        for i, task in enumerate(tasks, 1):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{i}. {task['name']} - {task['description']} - {task['deadline']} - {status}")
    except Exception as e:
        print(f"Error displaying tasks: {e}")

def complete_task():
    if not tasks:
        print("No tasks available to complete.")
        return
    view_tasks()
    try:
        task_num = input("Task number to mark as completed: ").strip()
        if not task_num.isdigit() or not (1 <= int(task_num) <= len(tasks)):
            raise ValueError("Invalid task number.")
        tasks[int(task_num) - 1]["completed"] = True
        print("Task marked as completed.")
    except ValueError as e:
        print(f"Input error: {e}")

if __name__ == "__main__":
    main()
