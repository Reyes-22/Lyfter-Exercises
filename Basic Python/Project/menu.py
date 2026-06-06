def show_menu():
    print('''
          Main Menu
          
          1. Add a new student to the system.
          2. Information about the students.
          3. Top 3 best averages.
          4. Overall averages of each student.
          5. Export file.
          6. Import file
          7. Exit
          ''')
    while True:
        try:
            option = int(input("Choose an option: "))

            if 0 < option < 8:
                return option
            else:
                print('Invalid option, Try again!')
        except ValueError:
            print('Invalid character, Try again!')
