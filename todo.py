import json

class ToDoList:
    def __init__(self, filename='tasks.json'):
        self.tasks = []
        self.filename = filename
        self.load_tasks()

    def add_task(self):
        task = input("Enter a task: ")
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task '{task}' added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks added yet!")
        else:
            print("Tasks:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

    def delete_task(self):
        self.view_tasks()
        try:
            task_num = int(input("Enter the task number to delete: "))
            task = self.tasks.pop(task_num - 1)
            self.save_tasks()
            print(f"Task '{task}' deleted successfully!")
        except (IndexError, ValueError):
            print("Invalid task number!")

    def edit_task(self):
        self.view_tasks()
        try:
            task_num = int(input("Enter the task number to edit: "))
            task = self.tasks[task_num - 1]
            new_task = input(f"Enter new task (currently: {task}): ")
            self.tasks[task_num - 1] = new_task
            self.save_tasks()
            print(f"Task '{task}' updated to '{new_task}' successfully!")
        except (IndexError, ValueError):
            print("Invalid task number!")

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as f:
                self.tasks = json.load(f)
        except FileNotFoundError:
            pass

    def save_tasks(self):
        with open(self.filename, 'w') as f:
            json.dump(self.tasks, f)

def main():
    todo = ToDoList()
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Edit Task")
        print("5. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            todo.add_task()
        elif choice == "2":
            todo.view_tasks()
        elif choice == "3":
            todo.delete_task()
        elif choice == "4":
            todo.edit_task()
        elif choice == "5":
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()