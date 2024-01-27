tasks = []

print("Welcome to the To-Do List Application!")
print("1. Add Tasks")
print("2. Delete Tasks")
print("3. View Tasks")
print("4. Exit")

while True:  
    choice = input("Enter your choice: ")

    if choice == "1":
        t1 = input("Enter the tasks: ")
        tasks.append(t1)
        print("Tasks added successfully!")

    elif choice == "2":
        t1 = input("Enter the task to delete: ")
        if t1 in tasks:
            tasks.remove(t1)
            print("Tasks deleted ")
        else:
            print("Tasks not found!")

    elif choice == "3":
        if len(tasks) == 0:
            print("Tasks not found!")
        else:
            print("Your present tasks is:")
            for t1 in tasks:
                print(t1)

    elif choice == "4":
        print("Exit application")
        break

    else:
        print("Invalid choice! Please try again")
