def decorator(func):
    def wrapper(*args, **kwargs):
        for parameter in args:
            if not isinstance(parameter, int):
                raise ValueError("All parameters must be integers.")

        return func(*args, **kwargs)

    return wrapper


@decorator
def create_list_of_numbers(num1, num2, num3, num4, num5):
    return [num1, num2, num3, num4, num5]


print(create_list_of_numbers(1, 2, 3, "hello", 5))
