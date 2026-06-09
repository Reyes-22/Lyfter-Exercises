string_string = "Bryan " + "Reyes"
print(string_string)  # If I sum two strings, I get a string.

string_integer = "I am " + str(29) + " years old."
# If I sum a string and an integer, I get an error. I have to convert the integer to a string first.
print(string_integer)

list_list = ["Bryan", "Reyes"] + ["is my name."]
print(list_list)  # If I sum two lists, I get a  combined list.

float_integer = 75.6 + 10
# If I sum a float and an integer, I get a float. The integer is converted to a float before the addition is performed.
print(float_integer)

integer_float = 29 + 10.7
# If I sum an integer and a float, I get a float. The integer is converted to a float before the addition is performed.
print(integer_float)

bool_bool = True + False
# If I sum two boolean values, I get an integer. True is treated as 1 and False is treated as 0, so the result is 1.
print(bool_bool)

bool_integer = True + 10
# If I sum a boolean value and an integer, I get an integer. True is treated as 1 and False is treated as 0, so the result is 11.
print(bool_integer)

integer_bool = 29 + False
# If I sum an integer and a boolean value, I get an integer. True is treated as 1 and False is treated as 0, so the result is 29.
print(integer_bool)

list_bool = ["Bryan", "Reyes"] + [True]
# If I sum a list and a boolean value, I get an error. I cannot add a list and a boolean value together because they are different data types and cannot be combined in this way.
print(list_bool)
