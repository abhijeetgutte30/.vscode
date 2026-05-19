import os
import time
import random

# ===============================
# UTIL FUNCTIONS
# ===============================

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input("\nPress Enter to continue...")

# ===============================
# STUDENT MANAGEMENT SYSTEM
# ===============================

students = {}

def add_student():
    clear()
    print("=== ADD STUDENT ===")
    roll = input("Roll No: ")
    if roll in students:
        print("Student already exists!")
        pause()
        return
    name = input("Name: ")
    marks = int(input("Marks: "))
    students[roll] = {"name": name, "marks": marks}
    print("Student added successfully!")
    pause()

def view_students():
    clear()
    print("=== STUDENT LIST ===")
    if not students:
        print("No students found!")
    else:
        for roll, data in students.items():
            print(f"Roll: {roll} | Name: {data['name']} | Marks: {data['marks']}")
    pause()

def delete_student():
    clear()
    print("=== DELETE STUDENT ===")
    roll = input("Enter Roll No: ")
    if roll in students:
        del students[roll]
        print("Student deleted!")
    else:
        print("Student not found!")
    pause()

# ===============================
# MINI GAMES
# ===============================

def guess_number():
    clear()
    print("=== GUESS THE NUMBER GAME ===")
    number = random.randint(1, 20)
    attempts = 5

    while attempts > 0:
        guess = int(input("Guess number (1-20): "))
        if guess == number:
            print("🎉 Correct! You win!")
            break
        elif guess > number:
            print("Too high!")
        else:
            print("Too low!")
        attempts -= 1
        print("Attempts left:", attempts)

    if attempts == 0:
        print("❌ You lost! Number was:", number)
    pause()

def rock_paper_scissors():
    clear()
    print("=== ROCK PAPER SCISSORS ===")
    choices = ["rock", "paper", "scissors"]
    user = input("Choose rock/paper/scissors: ").lower()
    computer = random.choice(choices)

    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("🎉 You win!")
    else:
        print("❌ You lose!")
    pause()

# ===============================
# CALCULATOR
# ===============================

def calculator():
    clear()
    print("=== SIMPLE CALCULATOR ===")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("1.Add  2.Subtract  3.Multiply  4.Divide")
    ch = input("Choose operation: ")

    if ch == "1":
        print("Result:", a + b)
    elif ch == "2":
        print("Result:", a - b)
    elif ch == "3":
        print("Result:", a * b)
    elif ch == "4":
        print("Result:", a / b if b != 0 else "Infinity")
    else:
        print("Invalid choice!")
    pause()

# ===============================
# MAIN MENU
# ===============================

def main_menu():
    while True:
        clear()
        print("""
==============================
🔥 MEGA PYTHON PROJECT 🔥
==============================
1. Add Student
2. View Students
3. Delete Student
4. Guess The Number Game
5. Rock Paper Scissors
6. Calculator
7. Exit
==============================
""")
        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            guess_number()
        elif choice == "5":
            rock_paper_scissors()
        elif choice == "6":
            calculator()
        elif choice == "7":
            clear()
            print("Goodbye! 👋")
            time.sleep(1)
            break
        else:
            print("Invalid choice!")
            pause()

# ===============================
# PROGRAM START
# ===============================

main_menu()
