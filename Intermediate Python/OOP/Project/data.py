import csv
from actions import Student


def export_data(list_of_students):
    list_of_students_dicts = []

    for student in list_of_students:
        student_dict = {
            "Name": student.name,
            "Section": student.section,
            "Spanish Grade": student.spanish_grade,
            "English Grade": student.english_grade,
            "Science Grade": student.science_grade,
            "Geography Grade": student.geography_grade,
            "Average Grade": student.average_grade
        }
        list_of_students_dicts.append(student_dict)

    with open("list_of_students.csv", "w", newline="", encoding="utf-8") as file:
        headers = ["Name", "Section", "Spanish Grade", "English Grade",
                   "Science Grade", "Geography Grade", "Average Grade"]
        writer = csv.DictWriter(file, fieldnames=headers)

        writer.writeheader()
        writer.writerows(list_of_students_dicts)


def convert_dicts_to_students(list_of_dicts):
    list_of_students = []

    for row in list_of_dicts:
        student = Student(
            row["Name"],
            row["Section"],
            row["Spanish Grade"],
            row["English Grade"],
            row["Science Grade"],
            row["Geography Grade"],
            row["Average Grade"]
        )
        list_of_students.append(student)

    return list_of_students


def import_data():
    try:
        with open("list_of_students.csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            list_of_students = []
            for row in reader:
                row["Spanish Grade"] = float(row["Spanish Grade"])
                row["English Grade"] = float(row["English Grade"])
                row["Science Grade"] = float(row["Science Grade"])
                row["Geography Grade"] = float(row["Geography Grade"])
                row["Average Grade"] = float(row["Average Grade"])
                list_of_students.append(row)
        return list_of_students

    except FileNotFoundError:
        print("There is not an exported file found.")
        return []
