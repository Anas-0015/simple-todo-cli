def main():
    task = []

    # Initial tasks input
    length = int(input("How many tasks: "))
    for _ in range(length):
        task.append(input("Enter task: "))

    while True:
        print("\n1. Add Task")
        print("2. Complete Task")
        print("3. View Tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_to_list(task)
        elif choice == '2':
            complete_task(task)
        elif choice == '3':
            view_tasks(task)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def add_to_list(task):
    new_task = input("Enter new task: ")
    task.append(new_task)
    print(f"Task '{new_task}' added.")

def complete_task(task):
    if not task:
        print("No tasks available to complete.")
        return

    view_tasks(task)
    try:
        task_number = int(input("Enter the task number to complete: "))
        if 1 <= task_number <= len(task):
            completed_task = task.pop(task_number - 1)
            print(f"Task '{completed_task}' completed and removed from the list.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def view_tasks(task):
    if not task:
        print("No tasks available.")
    else:
        print("Tasks:")
        for i, t in enumerate(task, start=1):
            print(f"{i}. {t}")

if __name__ == "__main__":
    main()
