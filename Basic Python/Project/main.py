import actions
import menu


def selected_option(num):
    option = num
    while option != 7:
        match option:
            case 1:
                actions.add_new_student()
            case 2:
                actions.show_information_students(actions.add_new_student)
            case 3:
                actions.view_top_averages(actions.add_new_student)
            case 4:
                actions.view_all_averages(actions.add_new_student)
            case 5:
            case 6:
