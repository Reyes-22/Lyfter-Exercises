import actions
import menu
import data


def selected_option(num):
    students = []
    option = num
    while option != 7:
        match option:
            case 1:
                students = actions.add_new_student(students)
            case 2:
                actions.show_information_students(students)
            case 3:
                actions.view_top_averages(students)
            case 4:
                actions.view_all_averages(students)
            case 5:
                data.export_data(students)
            case 6:
                students = data.import_data()
                actions.show_information_students(students)
        option = menu.show_menu()


selected_option(menu.show_menu())
