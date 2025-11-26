students = []  # for store student's data


# checking student's name in data and add a new student in data
def add_student():
    try:
        learner: str = input("Enter student's name: ")
        learner = " ".join(learner.split())  # removing unnecessary spaces
        # checking the line filling
        if not learner:
            print("Name cannot be empty!")
            return
        # name length check
        if len(learner) < 2:
            print("Your name is too short!")
            return
        if len(learner) > 50:
            print("Name must be shorter then 50 simbols!")
            return
        # checking for special simbols and numbers in the name
        if not all(x.isalpha() or x.isspace() for x in learner):
            print("Name can only contain letters and spaces!")
            return
        # checking existing students
        if any(map(lambda s: s["name"].casefold() == learner.casefold(), students)):
            print("This student already exists!")
            return
        # create dictionary for new student if not found in list
        student = {
            "name": learner,
            "grades": []
        }
        students.append(student)
        print(f"Student {learner} added!")
    except Exception as e:
        print(f"Error while reading input: {e}")
        return


# add student's grades
def add_grade():
    try:
        learner = input("Enter student's name: ").strip()
        # student search
        find_student = lambda name: next((s for s in students if s["name"].casefold() == name.casefold()), None)
        student = find_student(learner)
        # if student not found in data
        if not student:
            print("Student not found!")
            return
        # enter grades
        while True:
            grade = input("Enter a grade (or 'done' to finish): ")
            if grade.casefold() == 'done':
                break
            try:
                grade = int(grade)
                if 0 <= grade <= 100:
                    student["grades"].append(grade)
                else:
                    print("Grade must be between 0 and 100")
            except ValueError:
                print("Invalid input. Please enter a number or 'done'")
        return
    except Exception as e:
        print(f"Error while adding grade: {e}")


while True:
    print(
        "\n--- Student Grade Analyzer ---\n"
        "1 - add a new student;\n"
        "2 - add grades for a student;\n"
        "3 - show report (all students);\n"
        "4 - find top performer;\n"
        "5 - exit\n")
    try:
        choice = int(input("Enter your choice: "))
        if choice not in range(1, 6):
            print("Please, enter numbers from 1 to 5")
        elif choice == 1:
            add_student()
        elif choice == 2:
            add_grade()
        elif choice == 5:
            break
    except ValueError:
        print("You can enter only numbers from 1 to 5")

print(students)
