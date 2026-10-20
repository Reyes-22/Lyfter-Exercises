
def bubble_sort(numbers):
    for i in range(len(numbers) - 1):
        has_made_changes = False

        for j in range(len(numbers) - i - 1):
            current_element = numbers[j]
            next_element = numbers[j + 1]

            print(
                f"-- Iteration {i}, {j}. "
                f"Actual: {current_element}, "
                f"Next: {next_element}"
            )

            if current_element > next_element:
                print("Swapping elements...")

                numbers[j] = next_element
                numbers[j + 1] = current_element

                has_made_changes = True

        if not has_made_changes:
            break

    return numbers


my_test_list = [1, 2, 3, 10, 4, 5, 6, 7, 8]

result = bubble_sort(my_test_list)

print("Sorted List:", result)
