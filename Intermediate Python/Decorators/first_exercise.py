def print_parameters_and_return(func):

    def wrapper(*args, **kwargs):

        print("Parameters:")
        print("args:", args)
        print("kwargs:", kwargs)

        result = func(*args, **kwargs)

        print("Return:", result)

        return result

    return wrapper


@print_parameters_and_return
def func_sum(a, b):
    return a + b


result = func_sum(5, 10)
