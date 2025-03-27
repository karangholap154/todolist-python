import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    """Load tasks from a file."""
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks):
    """Save tasks to a file."""
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    """Display tasks."""
    if not tasks:
        print("No tasks found.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    print()

def add_task(tasks):
    """Add a new task."""
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("Task added successfully!\n")

def delete_task(tasks):
    """Delete a task."""
    show_tasks(tasks)
    try:
        task_no = int(input("Enter task number to delete: ")) - 1
        if 0 <= task_no < len(tasks):
            removed_task = tasks.pop(task_no)
            save_tasks(tasks)
            print(f"Task '{removed_task}' removed successfully!\n")
        else:
            print("Invalid task number!\n")
    except ValueError:
        print("Please enter a valid number!\n")

def main():
    tasks = load_tasks()
    while True:
        print("To-Do List:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Try again.\n")

if __name__ == "__main__":
    main()
