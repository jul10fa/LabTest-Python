
students = [
    [301, "Sakib", [75, 82, 88]],
    [302, "Mim", [60, 72, 69]],
    [303, "Arif", [90, 85, 93]],
    [304, "Nusrat", [50, 58, 62]],
    [305, "Fahim", [80, 85, 78]]
]


# Task 1: Calculate Average
def calculate_average(marks):

    if len(marks) == 0:
        return None

    total = sum(marks)
    average = total / len(marks)

    return average


# Task 2: Classify Performance
def classify_performance(average):

    if average == None:
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

        # Check student information
        if len(student) != 3:
            print("Invalid student record!")
            continue

        sid = student[0]
        name = student[1]
        marks = student[2]

        # Check ID and name
        if sid == None or name == "":
            print("Missing student ID or name!")
            continue

        # Check marks availability
        if type(marks) != list or len(marks) == 0:
            print(name, ": No marks available")
            continue

        # Check valid marks
        valid = True

        for mark in marks:
            if (not isinstance(mark, (int, float))
                or isinstance(mark, bool)
                or mark < 0 or mark > 100):

                valid = False
                break

        if valid == False:
            print(name, ": Invalid marks!")
            continue

        # Calculate average and performance
        avg = calculate_average(marks)
        result = classify_performance(avg)

        print(f"{sid:<10}{name:<12}{avg:<15.2f}{result}")

    print("-" * 65)


# Run the Program
display_report(students)
