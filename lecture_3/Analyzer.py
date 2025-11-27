students = []  # a list for storing dictionaries with student data


def validate_name(name: str) -> str | None:
    """
    Validate a student's name according to predefined rules.

    The function checks the given `name` string and returns an error message
    if validation fails. Otherwise, it returns None.

    Validation rules:
    - Name must not be empty.
    - Name length must be at least 2 characters.
    - Name length must not exceed 50 characters.
    - Name can only contain letters and spaces.
    - Name must be unique (no duplicates in the `students` list).

    Args:
        name (str): The student's name to validate.

    Returns:
        str | None: An error message if validation fails, otherwise None.
    """
    name = " ".join(name.split())
    if not name:
        return "Name cannot be empty!"
    if len(name) < 2:
        return "Your name is too short!"
    if len(name) > 50:
        return "Name must be shorter than 50 symbols!"
    if not all(ch.isalpha() or ch.isspace() for ch in name):
        return "Name can only contain letters and spaces!"
    if any(student["name"].casefold() == name.casefold() for student in students):
        return "This student already exists!"
    return None


def average(grades: list[int]) -> float | None:
    """
    Calculate the average score from a list of grades.

    The function computes the arithmetic mean of the provided `grades` list.
    If the list is empty, it returns None.

    Args:
        grades (list[int]): A list of integer grade values.

    Returns:
        float | None: The average score as a float, or None if the list is empty.
    """
    return sum(grades) / len(grades) if grades else None


def add_student():
    """
    Add a new student to the students list.

    The function prompts the user to enter a student's name, validates it using
    `validate_name()`, and if the name passes validation, adds the student to
    the global `students` list with an empty grades list. If validation fails,
    an error message is printed and the student is not added.

    Workflow:
    - Prompt the user for a student's name.
    - Validate the name with `validate_name()`.
    - If validation fails, print the error message and exit.
    - If validation succeeds, append a new student dictionary to `students`.

    Returns:
        None
    """
    learner = input("Enter student's name: ")
    error = validate_name(learner)
    if error:
        print(error)
        return
    students.append({"name": " ".join(learner.split()), "grades": []})
    print(f"Student {learner} added!")


# a function for adding grades to a student
def add_grade():
    """
    Add a grade to an existing student.

    The function prompts the user to enter a student's name, searches for the
    student in the global `students` list, and if found, allows adding a grade
    to their record. If the student does not exist, an error message is printed
    and no grade is added.

    Workflow:
    - Prompt the user for a student's name.
    - Search for the student in the `students` list (case-insensitive).
    - If the student is not found, print an error message and exit.
    - If the student is found, proceed to add a grade to their `grades` list.

    Returns:
        None
    """
    learner = input("Enter student's name: ").strip()
    student = next((s for s in students if s["name"].casefold() == learner.casefold()), None)
    if not student:
        print("Student not found!")
        return

    while True:
        grade = input("Enter a grade (or 'done' to finish): ")
        if grade.casefold() == 'done':
            break
        try:
            grade = int(grade)
            if 0 <= grade <= 100:
                student["grades"].append(grade)
                print(f"Grade {grade} added for {student['name']}")
            else:
                print("Grade must be between 0 and 100")
        except ValueError:
            print("Invalid input. Please enter a number or 'done'")


def report():
    """
    Generate a report of all students and their average grades.

    The function prints each student's average grade (or "N/A" if no grades are available).
    It also calculates and displays a summary including:
    - Maximum average grade
    - Minimum average grade
    - Overall average grade across all students

    Workflow:
    - If no students exist, print a message and exit.
    - For each student, calculate the average using `average()`.
    - Print the student's average grade or "N/A" if no grades are present.
    - Collect valid averages to compute summary statistics.
    - Print summary statistics if at least one student has grades.

    Returns:
         None
    """
    if not students:
        print("No students in the list.")
        return

    averages = []
    for s in students:
        avg = average(s["grades"])
        if avg is None:
            print(f"{s['name']}'s average grade is N/A")
        else:
            averages.append(avg)
            print(f"{s['name']}'s average grade is {round(avg, 2)}")

    if averages:
        print("\nSummary:")
        print(f"Max average: {round(max(averages), 2)}")
        print(f"Min average: {round(min(averages), 2)}")
        print(f"Overall average: {round(sum(averages) / len(averages), 2)}")
    else:
        print("\nNo grades available to calculate summary.")


def find_top_performer():
    """
    Find and display the student(s) with the highest average grade.

    The function evaluates all students who have at least one grade recorded.
    It determines the maximum average score and selects all students who share
    that score. The result is printed to the console.

    Workflow:
    - Filter out students without grades.
    - If no valid students exist, print a message and exit.
    - Calculate the maximum average grade among valid students.
    - Identify all students whose average equals the maximum.
    - Print the top performer(s) and their average grade.

    Returns:
        None
    """
    valid_students = [s for s in students if s["grades"]]
    if not valid_students:
        print("No grades to evaluate top performer.")
        return

    top_student = max(valid_students, key=lambda s: average(s["grades"]))
    max_score = average(top_student["grades"])
    top_students = [s["name"] for s in valid_students if average(s["grades"]) == max_score]

    if len(top_students) == 1:
        print(f"The student with the highest average is {top_students[0]} with a grade of {round(max_score, 2)}")
    else:
        print(f"Top performers are {', '.join(top_students)} with a grade of {round(max_score, 2)}")


def main_menu():
    """
    Display the main menu and handle user interaction.

    The function runs an infinite loop that presents the user with options
    to manage students and their grades. Based on the user's choice, it
    calls the appropriate function.

    Menu options:
    1 - Add a new student
    2 - Add grades for a student
    3 - Show report (all students)
    4 - Find top performer
    5 - Exit the program

    Workflow:
    - Display the menu.
    - Prompt the user for a choice (1–5).
    - Validate input; if invalid, show an error message.
    - Use `match` to call the corresponding function.
    - Exit the loop when the user selects option 5.

    Returns:
        None
    """
    while True:
        print(
            "\n--- Student Grade Analyzer ---\n"
            "1 - add a new student;\n"
            "2 - add grades for a student;\n"
            "3 - show report (all students);\n"
            "4 - find top performer;\n"
            "5 - exit\n"
        )
        try:
            choice = int(input("Enter your choice: "))
            if choice not in range(1, 6):
                print("Please, enter numbers from 1 to 5")
                continue

            match choice:
                case 1:
                    add_student()
                case 2:
                    add_grade()
                case 3:
                    report()
                case 4:
                    find_top_performer()
                case 5:
                    print("Exiting program. Goodbye!")
                    break
        except ValueError:
            print("You can enter only numbers from 1 to 5")


main_menu()