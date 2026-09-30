# Student Grading System Project
# Python project for student records

students_list = []


def get_grade(per):
    # check grade based on total percentage
    if per >= 90:
        return "A+"
    elif per >= 80:
        return "A"
    elif per >= 70:
        return "B"
    elif per >= 60:
        return "C"
    elif per >= 50:
        return "D"
    else:
        return "Fail"


def add_student_data():
    print("\n--- Enter New Student Details ---")
    s_name = input("Student Name: ")
    roll = input("Roll Number: ")

    # taking marks input
    try:
        maths_mark = float(input("Maths marks: "))
        sci_mark = float(input("Science marks: "))
        eng_mark = float(input("English marks: "))
    except Exception:
        print("Error: Enter numbers only for marks!\n")
        return

    # calculate total & average
    total_marks = maths_mark + sci_mark + eng_mark
    percent = total_marks / 3
    final_grade = get_grade(percent)

    # store in dictionary
    data = {
        "name": s_name,
        "roll_no": roll,
        "maths": maths_mark,
        "science": sci_mark,
        "english": eng_mark,
        "total": total_marks,
        "percentage": percent,
        "grade": final_grade,
    }

    students_list.append(data)
    print("Done! Student record saved.\n")


def display_all():
    if len(students_list) == 0:
        print("\nNo records added yet!\n")
        return

    print("\n---------------- STUDENT LIST ----------------")
    i = 1
    for s in students_list:
        print("Record #" + str(i))
        print("Roll No: " + s["roll_no"] + " | Name: " + s["name"])
        print(
            "Marks: Math="
            + str(s["maths"])
            + ", Sci="
            + str(s["science"])
            + ", Eng="
            + str(s["english"])
        )
        print(
            "Total: "
            + str(s["total"])
            + "/300 | Percentage: "
            + str(round(s["percentage"], 2))
            + "%"
        )
        print("Grade: " + s["grade"])
        print("----------------------------------------------")
        i = i + 1
    print()


def search_student():
    if not students_list:
        print("\nList is empty!\n")
        return

    search_id = input("\nEnter roll number to search: ")
    found_flag = 0

    for s in students_list:
        if s["roll_no"] == search_id:
            print("\n*** Student Found ***")
            print("Name: " + s["name"])
            print("Roll No: " + s["roll_no"])
            print("Total Score: " + str(s["total"]) + " / 300")
            print("Percentage: " + str(round(s["percentage"], 2)) + "%")
            print("Grade: " + s["grade"] + "\n")
            found_flag = 1
            break

    if found_flag == 0:
        print("Student with roll no " + search_id + " not found.\n")


def show_stats():
    if len(students_list) == 0:
        print("\nNo data to calculate statistics.\n")
        return

    sum_percentages = 0
    top_score = -1
    topper_name = ""

    for s in students_list:
        sum_percentages = sum_percentages + s["percentage"]
        if s["percentage"] > top_score:
            top_score = s["percentage"]
            topper_name = s["name"]

    avg_score = sum_percentages / len(students_list)

    print("\n--- Class Performance Summary ---")
    print("Total Students: " + str(len(students_list)))
    print("Class Average: " + str(round(avg_score, 2)) + "%")
    print(
        "Top Performer: "
        + topper_name
        + " ("
        + str(round(top_score, 2))
        + "%)\n"
    )


def menu():
    while True:
        print("***** STUDENT GRADING SYSTEM *****")
        print("1. Add New Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Class Statistics")
        print("5. Exit")

        ch = input("Enter choice (1-5): ")

        if ch == "1":
            add_student_data()
        elif ch == "2":
            display_all()
        elif ch == "3":
            search_student()
        elif ch == "4":
            show_stats()
        elif ch == "5":
            print("Exiting project. Bye!")
            break
        else:
            print("Invalid option! Enter 1 to 5.\n")


# start program
menu()
