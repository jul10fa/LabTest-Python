
students = [
    [201, "Amina", [78, 85, 90]],
    [202, "Rahim", [65, 70, 68]],
    [203, "Nadia", [92, 88, 95]],
    [204, "Hasan", [55, 60, 65]],
    [205, "Tania", [80, 80, 80]]
]


# Task 1: Calculate Average
def calculate_average(marks):
    if not marks:
        return None

    return sum(marks) / len(marks)


# Task 2: Classify Performance
def classify_performance(average):

    if average is None:
        return "No Marks"
    elif average >= 80:
        return "Excellent"
    elif average >= 70:
        return "Good"
    elif average >= 60:
        return "Satisfactory"
    else:
        return "Needs Improvement"


# Task 3: Display Student Report
def display_report(students):

    print("STUDENT MARKS REPORT")
    print("-" * 65)
    print(f"{'ID':<10}{'Name':<12}{'Average':<15}{'Performance'}")
    print("-" * 65)

    for student in students:

        # Check missing or invalid data
        if len(student) != 3:
            print("Invalid student record!")
            continue

        student_id, name, marks = student

        if not student_id or not name:
            print("Missing student ID or name!")
            continue

        if not isinstance(marks, list) or len(marks) == 0:
            print(f"{name}: No marks available")
            continue

        if not all(
            isinstance(m, (int, float)) and not isinstance(m, bool)
            and 0 <= m <= 100 for m in marks
        ):
            print(f"{name}: Invalid marks!")
            continue

        average = calculate_average(marks)
        performance = classify_performance(average)

        print(f"{student_id:<10}{name:<12}{average:<15.2f}{performance}")

    print("-" * 65)


# Run the Program
display_report(students)