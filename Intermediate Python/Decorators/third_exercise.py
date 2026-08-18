from datetime import date


class User:
    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year
        if today < date(today.year, self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age


def adult_only(func):
    def wrapper(user, *args, **kwargs):
        if user.age < 18:
            raise ValueError("User must be at least 18 years old.")
        return func(user, *args, **kwargs)
    return wrapper


@adult_only
def verify_user(user):
    return print(f"User {user.name} is verified and is {user.age} years old.")


user1 = User("Bryan", date(2015, 5, 15))
verify_user(user1)
