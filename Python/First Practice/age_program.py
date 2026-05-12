name = input("What is your name? ")
last_name = input("What is your last name? ")
age = int(input("How old are you? "))

if age < 3:
    print("You are a baby.")
elif age < 10:
    print("You are a child.")
elif age < 13:
    print("You are a pre-teen.")
elif age < 20:
    print("You are a teenager.")
elif age < 35:
    print("You are an young adult.")
elif age < 60:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
