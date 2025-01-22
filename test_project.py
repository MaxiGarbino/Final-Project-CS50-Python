import pytest
from project import add_task, tasks, complete_task
def main():
    test_add_task()
    test_complete_task()

def test_add_task():
    tasks.clear()
    add_task()
    assert len(tasks) == 1

def test_complete_task():
    tasks.clear()
    tasks.append({"name": "Test", "description": "Test", "deadline": "2025-12-31", "completed": False})
    complete_task()
    assert tasks[0]["completed"] == True

if __name__ == "__main__":
    main()
