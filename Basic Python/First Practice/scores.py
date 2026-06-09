print("Welcome to the grades program!")

total_grades = int(input("Enter the total number of grades: "))
counter_grades = 1
approved_grades = 0
failing_grades = 0
average_approved_grade = 0
average_failing_grade = 0
average_total_grades = 0


while counter_grades <= total_grades:
    print(f"Enter grade {counter_grades}:")
    grade = int(input("Current grade: "))
    if grade < 70:
        failing_grades += 1
        average_failing_grade += grade
    else:
        approved_grades += 1
        average_approved_grade += grade
    counter_grades += 1

average_failing_grade = average_failing_grade / \
    failing_grades if failing_grades > 0 else 0
average_approved_grade = average_approved_grade / \
    approved_grades if approved_grades > 0 else 0
average_total_grades = (average_failing_grade * failing_grades + average_approved_grade * approved_grades) / \
    total_grades if total_grades > 0 else 0


print(f"Approved grades: {approved_grades}")
print(f"Failing grades: {failing_grades}")
print(f"Average of approved grades: {average_approved_grade}")
print(f"Average of failing grades: {average_failing_grade}")
print(f"Average of all grades: {average_total_grades}")
