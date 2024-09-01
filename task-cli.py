import json
import os
import sys
from datetime import datetime

def load_task():
    if not os.path.exists('tasks.json'):
        with open('tasks.json', 'w') as file:
            json.dump([], file)
        return []
    
    with open('tasks.json', 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def save_task(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(description):
    tasks = load_task()
    task_id = len(tasks) + 1
    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    
    new_task = {
        'id': task_id,
        'description': description,
        'status': 'pending',
        'createdAt': formatted_time,
        'updatedAt': formatted_time
    }
    tasks.append(new_task)
    save_task(tasks)
    print(f'Task added successfully (ID: {task_id})')

def list_task():
    tasks = load_task()
    for task in tasks:
        print(f"{task['id']} - {task['description']} - {task['status']} - {task['createdAt']} - {task['updatedAt']}")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == 'add' and len(sys.argv) > 2:
            add_task(sys.argv[2])
        elif command == 'list': 
            list_task()
    else:
        print("No command provided.")
