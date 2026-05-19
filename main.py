import os

habits = []
completed = []

if os.path.exists("habits.txt"):
    file = open("habits.txt", "r")

    for line in file:
        habits.append(line.strip())

    file.close()

while True:
    print("\n--- Daily Habit Tracker ---")
    print("1. Add Habit")
    print("2. View Habits")
    print("3. Mark Habit Complete")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        habit = input("Enter habit name: ")

        if habit in habits:
            print("Habit already exists!")
        else:
            habits.append(habit)

            file = open("habits.txt", "a")
            file.write(habit + "\n")
            file.close()

            print("Habit added successfully!")

    elif choice == "2":
        if len(habits) == 0:
            print("No habits added yet.")
        else:
            print("\nYour Habits:")

            for i in range(len(habits)):

                if habits[i] in completed:
                    print(i + 1, ".", habits[i], "[Done]")
                else:
                    print(i + 1, ".", habits[i], "[Pending]")

    elif choice == "3":
        habit = input("Enter completed habit name: ")

        if habit in habits:
            completed.append(habit)
            print("Habit marked as completed!")
        else:
            print("Habit not found.")

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice")