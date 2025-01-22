# Task Manager  
#### Video Demo:  https://youtu.be/2hxTfWFkqDY
#### Description:  
Task Manager is a simple command-line application built with Python to help manage tasks. It lets you add tasks, view your task list, and mark tasks as completed. Tasks are saved in a JSON file, ensuring your data persists between sessions.  

### **Files**  
- **project.py**: The main script with all core functionality.  
  - `add_task()`: Adds a new task with a name, description, and deadline.  
  - `view_tasks()`: Displays all tasks, showing their status (Pending or Completed).  
  - `complete_task()`: Marks a selected task as completed.  

- **test_project.py**: Contains tests using `pytest` to ensure the main functions work as expected.  
- **tasks.json**: Stores tasks persistently. The file is created automatically if it doesn’t exist.  
- **requirements.txt**: Lists `pytest` as a dependency for running tests.  

This project is a simple, user-friendly way to track tasks while demonstrating foundational programming and testing skills.  
