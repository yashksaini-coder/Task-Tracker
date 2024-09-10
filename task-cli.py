import json
import os
import sys
from datetime import datetime
from rich.console import Console
from rich.table import Table
import argparse
from rich.prompt import Prompt

console = Console()

TASK_TRACKER_ASCII = """
 _____         _     _____               _             
|_   _|_ _ ___| | __| __  |___ ___ ___ _| |___ ___ 
  | | | | |_ -| |/ /|    -| .'| .'|  _| . | -_|  _|
  |_| |___|___|_|_/ |__|__|__,|__,|_| |___|___|_|  
"""

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


def get_next_id(tasks):
    return max([task['id'] for task in tasks], default=0) + 1

def add_task(description):
    tasks = load_tasks()
    task_id = get_next_id(tasks)
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
    console.print(f"[green]Task added successfully (ID: {task_id})[/green]")


def list_tasks(status=None):
    """List tasks filtered by status, or list all tasks if no status is provided."""
    tasks = load_tasks()
    if status:
        tasks = [task for task in tasks if task['status'] == status.lower().capitalize()]
    if not tasks:
        console.print("[red]No tasks found.[/red]")
        return
    
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
        
    console.print(table)


def update_task_status(task_id, new_status):
    """Update the status of an existing task."""
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = new_status
            task['updatedAt'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_tasks(tasks)
            console.print(f"[green]Task ID {task_id} marked as {new_status}.[/green]")
            return
    console.print(f"[red]Task ID {task_id} not found.[/red]")

def mark_in_progress(task_id):
    update_task_status(task_id, 'In-progress')

def mark_done(task_id):
    update_task_status(task_id, 'Completed')

def delete_task(task_id):
    """Delete a task by its ID."""
    tasks = load_tasks()
    task_exists = False
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            task_exists = True
            break
    if task_exists:
        save_tasks(tasks)
        console.print(f"[yellow]Task ID {task_id} deleted successfully.[/yellow]")
    else:
        console.print(f"[red]Task ID {task_id} does not exist.[/red]")


def update_task(task_id, new_description):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = new_description
            task['updatedAt'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_tasks(tasks)
            console.print(f"[green]Task ID {task_id} updated successfully.[/green]")
            return
    console.print(f"[red]Task ID {task_id} not found.[/red]")


def main():
    parser = argparse.ArgumentParser(description="Task Tracker CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add task
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", help="Task description")

    # List tasks
    list_parser = subparsers.add_parser("list", help="List tasks")
    list_parser.add_argument("--status", choices=["pending", "in-progress", "completed"], help="Filter by status")

    # Update task
    update_parser = subparsers.add_parser("update", help="Update a task")
    update_parser.add_argument("id", type=int, help="Task ID")
    update_parser.add_argument("description", help="New task description")

    # Mark task status
    mark_parser = subparsers.add_parser("mark", help="Mark task status")
    mark_parser.add_argument("id", type=int, help="Task ID")
    mark_parser.add_argument("status", choices=["in-progress", "completed"], help="New status")

    # Delete task
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("id", type=int, help="Task ID")

    args = parser.parse_args()

    console.print(TASK_TRACKER_ASCII, style="bold blue")
    console.print("Welcome to the Task Tracker CLI!", style="bold green")

    if args.command == "add":
        add_task(args.description)
    elif args.command == "list":
        list_tasks(args.status)
    elif args.command == "update":
        update_task(args.id, args.description)
    elif args.command == "mark":
        update_task_status(args.id, args.status.capitalize())
    elif args.command == "delete":
        if Prompt.ask(f"Are you sure you want to delete task {args.id}?", choices=["y", "n"]) == "y":
            delete_task(args.id)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
