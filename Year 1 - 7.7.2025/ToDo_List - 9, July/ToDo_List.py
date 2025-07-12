tasks = ["clean", "wash"]

while True:
    print("\nWhat do you want to do?")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        adding = input("What task do you want to add?:")
        tasks.append(adding)

    elif choice == "2":
         for i in tasks:
             print(i)

    elif choice == "3":
        removing = input("What tasks do you want to remove?:")
        tasks.remove(removing)

    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
