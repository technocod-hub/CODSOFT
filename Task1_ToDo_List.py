# Task 1 - To-Do List Application
# CodSoft Python Internship - Azhaan Azam

tasks = []

def show_tasks():
    if len(tasks) == 0:
        print("\n📋 No tasks found! Add some tasks first.")
    else:
        print("\n📋 Your To-Do List:")
        print("-" * 35)
        for i, task in enumerate(tasks, 1):
            status = "✅" if task['done'] else "❌"
            print(f"{i}. {status} {task['name']}")
        print("-" * 35)

def add_task():
    name = input("\nEnter task name: ")
    tasks.append({'name': name, 'done': False})
    print(f"✅ Task '{name}' added successfully!")

def mark_done():
    show_tasks()
    if len(tasks) == 0:
        return
    try:
        num = int(input("\nEnter task number to mark as done: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]['done'] = True
            print(f"✅ Task '{tasks[num-1]['name']}' marked as done!")
        else:
            print("❌ Invalid task number!")
    except ValueError:
        print("❌ Please enter a valid number!")

def delete_task():
    show_tasks()
    if len(tasks) == 0:
        return
    try:
        num = int(input("\nEnter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"🗑️ Task '{removed['name']}' deleted!")
        else:
            print("❌ Invalid task number!")
    except ValueError:
        print("❌ Please enter a valid number!")

def update_task():
    show_tasks()
    if len(tasks) == 0:
        return
    try:
        num = int(input("\nEnter task number to update: "))
        if 1 <= num <= len(tasks):
            new_name = input("Enter new task name: ")
            old_name = tasks[num - 1]['name']
            tasks[num - 1]['name'] = new_name
            print(f"✏️ Task '{old_name}' updated to '{new_name}'!")
        else:
            print("❌ Invalid task number!")
    except ValueError:
        print("❌ Please enter a valid number!")

print("===== To-Do List Application =====")

while True:
    print("\nMenu:")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Update Task")
    print("5. Delete Task")
    print("6. Exit")

    choice = input("\nEnter your choice (1-6): ")

    if choice == '1':
        show_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        mark_done()
    elif choice == '4':
        update_task()
    elif choice == '5':
        delete_task()
    elif choice == '6':
        print("\nGoodbye! Stay productive! 💪")
        break
    else:
        print("❌ Invalid choice! Please enter 1-6.")