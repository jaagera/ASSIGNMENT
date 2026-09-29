
#Variables created
name = "Jacob"                  # str
age = 25                        # int
country = "Nigeria"             # str
programming_experience = 1.5    # float (years of experience)
is_learning_python = True       # bool

#Print each value & type
print("name:", name, "| type:", type(name))
print("age:", age, "| type:", type(age))
print("country:", country, "| type:", type(country))
print("programming_experience:", programming_experience, "| type:", type(programming_experience))
print("is_learning_python:", is_learning_python, "| type:", type(is_learning_python))

#no. string to integer
numeric_string = "42"
converted_number = int(numeric_string)

print("\nBefore conversion:", numeric_string, "| type:", type(numeric_string))
print("After conversion:", converted_number, "| type:", type(converted_number))

#how it now works like a number
print("converted_number + 8 =", converted_number + 8)
print("Original string + '8' =", numeric_string + "8")  # string concatenation, not addition



