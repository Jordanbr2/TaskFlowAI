def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")


tasks = load_tasks()
done = [False] * len(tasks)

while True:
    print("\nMenu:")
    print("1. Add task")
    print("2. Show tasks")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        task_title = input("Task title: ")
        if not task_title.strip():
            print("Task title cannot be empty. Please try again.")
            continue

        tasks.append(task_title)
        done.append(False)
        save_tasks(tasks)
        print(f"Added task: {task_title}")

    elif choice == "2":
        if not tasks:
            print("No tasks yet.")
        else:
            print("Tasks:")
            for index, task in enumerate(tasks, start=1):
                status = "Done" if done[index - 1] else "Not Done"
                print(f"{index}. {task} [{status}]")

    elif choice == "3":
        if not tasks:
            print("No tasks to mark as done.")
            continue

        input_index = input("Enter the task number to mark as done: ")
        if not input_index.isdigit():
            print("Invalid input. Please enter a valid task number.")
            continue

        task_index = int(input_index) - 1
        if 0 <= task_index < len(tasks):
            done[task_index] = True
            save_tasks(tasks)
            print(f"Marked task as done: {tasks[task_index]}")
        else:
            print("Invalid task number. Please try again.")

    elif choice == "4":
        if not tasks:
            print("No tasks to delete.")
            continue

        input_index = input("Enter the task number to delete: ")
        if not input_index.isdigit():
            print("Invalid input. Please enter a valid task number.")
            continue

        task_index = int(input_index) - 1

        if 0 <= task_index < len(tasks):
            deleted_task = tasks.pop(task_index)
            done.pop(task_index)
            save_tasks(tasks)
            print(f"Deleted task: {deleted_task}")
        else:
            print("Invalid task number. Please try again.")

    elif choice == "5":
        print("Exiting the task manager. Goodbye!")
        break

    else:
        print("Invalid option. Please try again.")
