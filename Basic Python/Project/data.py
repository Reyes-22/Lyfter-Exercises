import csv


def export_data(list_of_students):
    with open("list_of_students.csv", "w", newline="", encoding="utf-8") as file:
        headers = ["Name", "Section", "Spanish Grade", "English Grade",
                   "Science Grade", "Geography Grade", "Average Grade"]
        writer = csv.DictWriter(file, fieldnames=headers)

        writer.writeheader()
        writer.writerows(list_of_students)


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
