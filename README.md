<div align="center">
    <img src="https://socialify.git.ci/yashksaini-coder/Task-Tracker/image?forks=1&issues=1&language=1&name=1&pulls=1&stargazers=1&theme=Auto" alt="Task Tracker CLI" width="640" height="320" />
</div>
<br><br>

<div align="center">
    <img alt="GitHub Repo Name" src="https://img.shields.io/badge/Task_Tracker-7209b7">
    <img alt="GitHub Author" src="https://img.shields.io/badge/Author-Yash%20K.%20Saini-006d77">
    <img alt="GitHub commit-activity" src="https://img.shields.io/github/commit-activity/t/yashksaini-coder/Task-Tracker">
    <img alt="GitHub contributors" src="https://img.shields.io/github/contributors/yashksaini-coder/Task-Tracker">
    <img alt="GitHub Created At" src="https://img.shields.io/github/created-at/yashksaini-coder/Task-Tracker">
    <img alt="GitHub Last Commit" src="https://img.shields.io/github/last-commit/yashksaini-coder/Task-Tracker">
    <img alt="GitHub Repo Size" src="https://img.shields.io/github/repo-size/yashksaini-coder/Task-Tracker">
    <img alt="GitHub License" src="https://img.shields.io/github/license/yashksaini-coder/Task-Tracker">
    <img alt="GitHub Open Issues" src="https://img.shields.io/github/issues/yashksaini-coder/Task-Tracker">
    <img alt="GitHub Closed Issues" src="https://img.shields.io/github/issues-closed/yashksaini-coder/Task-Tracker">
    <img alt="GitHub Open PR" src="https://img.shields.io/github/issues-pr/yashksaini-coder/Task-Tracker">
    <img alt="GitHub Closed PR" src="https://img.shields.io/github/issues-pr-closed/yashksaini-coder/Task-Tracker">
    <img alt="GitHub Forks" src="https://img.shields.io/github/forks/yashksaini-coder/Task-Tracker">
    <img alt="GitHub Stars" src="https://img.shields.io/github/stars/yashksaini-coder/Task-Tracker">
    <img alt="GitHub Watchers" src="https://img.shields.io/github/watchers/yashksaini-coder/Task-Tracker">
    <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/yashksaini-coder/Task-Tracker">
</div>
<br>

<div align='center' style=" display: grid;">

  [![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:ys3853428@gmail.com)
  [![Github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/yashksaini-coder)
  [![Medium](https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@yashksaini)
  [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/yashksaini/)
  [![Bento](https://img.shields.io/badge/Bento-768CFF.svg?style=for-the-badge&logo=Bento&logoColor=white)](https://bento.me/yashksaini)
[![Instagram](https://img.shields.io/badge/Instagram-%23FF006E.svg?style=for-the-badge&logo=Instagram&logoColor=white)](https://www.instagram.com/yashksaini.codes/)
  [![X](https://img.shields.io/badge/X-%23000000.svg?style=for-the-badge&logo=X&logoColor=white)](https://twitter.com/EasycodesDev) 
</div>

---

# Task Tracker CLI Project

The **Task Tracker** is a command-line interface (CLI) project designed to help you track and manage tasks. It allows you to add, update, and delete tasks, as well as mark tasks as "in-progress" or "done." This project will help you practice essential programming skills, including working with the filesystem, handling user inputs, and building a basic CLI application.

## Requirements

The application should run from the command line, accept user actions and inputs as arguments, and store the tasks in a JSON file. The user should be able to:

- Add, Update, and Delete tasks
- Mark a task as "in-progress" or "done"
- List all tasks
- List all tasks that are marked as "done"
- List all tasks that are marked as "todo"
- List all tasks that are marked as "in-progress"

### Constraints

- You can use any programming language to build this project.
- Use **positional arguments** in the command line to accept user inputs.
- Use a **JSON file** to store the tasks in the current directory.
- The JSON file should be created if it does not exist.
- Use the **native filesystem module** of your programming language to interact with the JSON file.
- Do not use any external libraries or frameworks to build this project.
- Ensure to handle errors and edge cases gracefully.

## Example Commands

Here are some example commands and their usage:

```bash
# Adding a new task
task-cli add "Buy groceries"
# Output: Task added successfully (ID: 1)

# Updating and deleting tasks
task-cli update 1 "Buy groceries and cook dinner"
task-cli delete 1

# Marking a task as in-progress or done
task-cli mark-in-progress 1
task-cli mark-done 1

# Listing all tasks
task-cli list

# Listing tasks by status
task-cli list done
task-cli list todo
task-cli list in-progress
```

## Task Properties

Each task should have the following properties:

- `id`: A unique identifier for the task
- `description`: A short description of the task
- `status`: The status of the task (`todo`, `in-progress`, `done`)
- `createdAt`: The date and time when the task was created
- `updatedAt`: The date and time when the task was last updated

These properties should be stored in the JSON file when adding a new task and updated when modifying a task.

## Conclusion

This project is an opportunity to improve your programming and CLI development skills. It allows you to practice interacting with the filesystem, handling JSON data, and managing user input via the command line—all while building a useful task-tracking tool.

Original Project Link: [Task Tracker CLI](https://roadmap.sh/projects/task-tracker)

---

## Getting Started

### Prerequisites

Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yashksaini-coder/Task-Tracker.git
    cd Task-Tracker
    ```

2. Create a virtual environment:
    ```sh
    python -m venv venv
    ```

3. Activate the virtual environment:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

4. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

### Usage

1. Run the Task Tracker CLI:
    ```sh
    pip install -e .
    task-tracker    
    ```

2. Follow the on-screen instructions to add, view, update, or delete tasks.

### Basic Commands

- **Add a Task**: 
    ```sh
    add "Task Description"
    ```

- **View All Tasks**: 
    ```sh
    view
    ```

- **Update a Task**: 
    ```sh
    update <task_id> "New Task Description"
    ```

- **Delete a Task**: 
    ```sh
    delete <task_id>
    ```

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---