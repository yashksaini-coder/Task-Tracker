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
        tasks = [task for task in tasks if task['status'] == status.lower().capitalize()]
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("ID")
    table.add_column("Description")
    table.add_column("Status")
    table.add_column("Created At")
    table.add_column("Updated At")
    for task in tasks:
        if task['status'] == 'Pending':
            status_color = "green"
        elif task['status'] == 'In-progress':
            status_color = "purple"
        elif task['status'] == 'Completed':
            status_color = "red"
        else:
            status_color = "white"
        table.add_row(
            str(task['id']),
            task['description'],
            f"[{status_color}]{task['status']}[/{status_color}]",
            task['createdAt'],
            task['updatedAt']
        )
    console = Console()
    console.print(table)

def update_task(task_id, new_description):
    """Update the description of an existing task."""
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = new_description
            task['updatedAt'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_tasks(tasks)
            print(f'Task ID {task_id} updated successfully.')
            return
    print(f'Task ID {task_id} not found.')

def mark_in_progress(task_id):
    """Mark a task as in-progress."""
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = 'In-progress'
            task['updatedAt'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_tasks(tasks)
            print(f'Task ID {task_id} marked as in-progress.')
            return
    print(f'Task ID {task_id} not found.')

def delete_task(task_id):
    """Delete a task by its ID."""
    tasks = load_tasks()
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks(tasks)
    print(f'Task ID {task_id} deleted successfully.')


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
        
        elif command == 'update' and len(sys.argv) > 3:
            update_task(int(sys.argv[2]), sys.argv[3])
            
        elif command == 'mark-in-progress' and len(sys.argv) > 2:
            mark_in_progress(int(sys.argv[2]))
            
        elif command == 'delete' and len(sys.argv) > 2:
            delete_task(int(sys.argv[2]))
            
    else:
        print("No command provided. Available commands: add, update, delete, mark-in-progress, mark-done, list")
