def validate_grade(subject):
    while True:
        try:
            grade = float(input(f'Enter the grade of {subject}: '))

            if 0 <= grade <= 100:
                return grade
            else:
                print('Invalid grade! Please enter a grade between 0 and 100.')
        except ValueError:
            print('Invalid character! Try again!')


def add_new_student(list_of_students):
    try:
        number_of_students = int(
            input('How many students do you wanna enter?'))

        for i in range(number_of_students):
            student = {"Name": input("Enter student's complete name: "),
                       "Section": input("Enter student's section: "),
                       "Spanish Grade": validate_grade('Spanish Grade'),
                       "English Grade": validate_grade('English Grade'),
                       "Science Grade": validate_grade('Science Grade'),
                       "Geography Grade": validate_grade('Geography Grade'),
                       }

            average_grade = (student["Spanish Grade"] + student["English Grade"] +
                             student["Science Grade"]+student["Geography Grade"])/4
            student["Average Grade"] = average_grade

            list_of_students.append(student)

        return list_of_students

    except ValueError:
        print("Invalid character, Try again!")


def show_information_students(list_of_students):
    for student in list_of_students:
        for key, value in student.items():
            print(f"{key}:{value}")
        print("\n")


def get_average(list_of_students):
    return list_of_students["Average Grade"]


def view_top_averages(list_of_students):
    top_3_list = sorted(list_of_students, key=get_average, reverse=True)[:3]

    for top3 in top_3_list:
        print(top3["Name"])
        print(top3["Average Grade"])
        print("\n")


def view_all_averages(list_of_students):
    for student in list_of_students:
        print(student["Name"])
        print(student["Average Grade"])
        print("\n")
