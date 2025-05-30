# scoreboard_no_functions.py

# A simple Class Scoreboard CLI without functions

class_list = []

while True:
    # Main menu
    print("\n=== CLASS SCOREBOARD ===")
    print("1) Add Students")
    print("2) Statistics")
    print("3) Search Student")
    print("4) Honour Roll")
    print("5) Quit")
    choice = input("Choice: ")

    if choice == "1":
        # Add Students
        print("\nEnter student details (leave name blank to return to menu):")
        while True:
            name = input("Name: ")
            if not name:
                break
            # Validate score input
            while True:
                score_str = input("Score (0–100): ")
                try:
                    score = int(score_str)
                    if 0 <= score <= 100:
                        break
                    else:
                        print("Please enter a score between 0 and 100.")
                except ValueError:
                    print("Invalid input. Enter an integer score.")
            class_list.append({"name": name, "score": score})
            print(f"Added: {name} — {score}\n")
    elif choice == "2":
        # Statistics
        if not class_list:
            print("\nNo student records available.\n")
        else:
            scores = [student["score"] for student in class_list]
            highest = max(scores)
            lowest = min(scores)
            average = sum(scores) / len(scores)
            print(
                f"\nStudents: {len(scores)} | "
                f"Highest: {highest} | "
                f"Lowest: {lowest} | "
                f"Average: {average:.2f}\n"
            )
    elif choice == "3":
        # Search Student
        if not class_list:
            print("\nNo student records available.\n")
        else:
            name_query = input("\nEnter name to search: ").lower()
            found = False
            for student in class_list:
                if student["name"].lower() == name_query:
                    print(f"Found: {student['name']} — {student['score']}\n")
                    found = True
                    break
            if not found:
                print("Student not found.\n")
    elif choice == "4":
        # Honour Roll
        honours = [s for s in class_list if s["score"] >= 90]
        print("\n=== Honour Roll (90+) ")
        if not honours:
            print("No students on the honour roll.\n")
        else:
            for student in honours:
                print(f"{student['name']} — {student['score']}")
            print()
    elif choice == "5":
        # Quit
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Enter a number between 1 and 5.\n")

print("Program terminated.")