import json
import os
import sys
from datetime import datetime
from rich.console import Console
from rich.table import Table

def load_tasks():
    if not os.path.exists('tasks.json'):
        with open('tasks.json', 'w') as file:
            json.dump([], file)
        return []
    
    with open('tasks.json', 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)


def add_task(description):
    tasks = load_tasks()
    task_id = len(tasks) + 1
    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    
    new_task = {
        'id': task_id,
        'description': description,
        'status': 'Pending',
        'createdAt': formatted_time,
        'updatedAt': formatted_time,
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f'Task added successfully (ID: {task_id})')


def list_tasks(status=None):
    """List tasks filtered by status, or list all tasks if no status is provided."""
    tasks = load_tasks()
    if status:
        tasks = [task for task in tasks if task['status'] == status]
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("ID")
    table.add_column("Description")
    table.add_column("Status")
    table.add_column("Created At")
    table.add_column("Updated At")
    for task in tasks:
        status_color = "green" if task['status'] == 'Completed' else "purple"
        table.add_row(
            str(task['id']),
            task['description'],
            f"[{status_color}]{task['status']}[/{status_color}]",
            task['createdAt'],
            task['updatedAt']
        )
    console = Console()
    console.print(table)

# Main function to handle command-line arguments
if __name__ == '__main__':
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == 'add' and len(sys.argv) > 2:
            add_task(sys.argv[2])
        
        elif command == 'list':
            if len(sys.argv) > 2:
                list_tasks(sys.argv[2])
            else:
                list_tasks()
        else:
            print("Command not recognized. Available commands: add, update, delete, mark-in-progress, mark-done, list")
    else:
        print("No command provided. Available commands: add, update, delete, mark-in-progress, mark-done, list")
