class Student:
    def __init__(self, name, section, spanish_grade, english_grade, science_grade, geography_grade, average_grade):
        self.name = name
        self.section = section
        self.spanish_grade = spanish_grade
        self.english_grade = english_grade
        self.science_grade = science_grade
        self.geography_grade = geography_grade
        self.average_grade = average_grade


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
            name = input("Enter student's complete name: ")
            section = input("Enter student's section: ")
            spanish_grade = validate_grade('Spanish Grade')
            english_grade = validate_grade('English Grade')
            science_grade = validate_grade('Science Grade')
            geography_grade = validate_grade('Geography Grade')

            student = Student(name, section, spanish_grade,
                              english_grade, science_grade, geography_grade, 0)

            average_grade = (student.spanish_grade + student.english_grade +
                             student.science_grade + student.geography_grade) / 4
            student.average_grade = average_grade

            list_of_students.append(student)

        return list_of_students

    except ValueError:
        print("Invalid character, Try again!")
        return list_of_students


def show_information_students(list_of_students):
    for student in list_of_students:
        print(f"Name: {student.name}")
        print(f"Section: {student.section}")
        print(f"Spanish Grade: {student.spanish_grade}")
        print(f"English Grade: {student.english_grade}")
        print(f"Science Grade: {student.science_grade}")
        print(f"Geography Grade: {student.geography_grade}")
        print(f"Average Grade: {student.average_grade}")
        print("\n")


def get_average(student):
    return student.average_grade


def view_top_averages(list_of_students):
    top_3_list = sorted(list_of_students, key=get_average, reverse=True)[:3]

    for top3 in top_3_list:
        print(top3.name)
        print(top3.average_grade)
        print("\n")


def view_all_averages(list_of_students):
    for student in list_of_students:
        print(student.name)
        print(student.average_grade)
        print("\n")
