students = []  # a list for storing student data


# name verification
def validate_name(name: str) -> str | None:
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


# a function for calculating the average score
def average(grades: list[int]) -> float | None:
    return sum(grades) / len(grades) if grades else None


# a function for adding a new student
def add_student():
    learner = input("Enter student's name: ")
    error = validate_name(learner)
    if error:
        print(error)
        return
    students.append({"name": " ".join(learner.split()), "grades": []})
    print(f"Student {learner} added!")


# a function for adding grades to a student
def add_grade():
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


# report on all students
def report():
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


# a function for finding the best students
def find_top_performer():
    valid_students = [s for s in students if s["grades"]]
    if not valid_students:
        print("No grades to evaluate top performer.")
        return

    # find the maximum average score
    top_student = max(valid_students, key=lambda s: average(s["grades"]))
    max_score = average(top_student["grades"])

    # select all students with this score
    top_students = [s["name"] for s in valid_students if average(s["grades"]) == max_score]

    if len(top_students) == 1:
        print(f"The student with the highest average is {top_students[0]} with a grade of {round(max_score, 2)}")
    else:
        print(f"Top performers are {', '.join(top_students)} with a grade of {round(max_score, 2)}")


# main menu
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
