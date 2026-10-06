full_name = input("Enter your full name: ")
print("Uppercase:", full_name.upper())
print("Lowercase:", full_name.lower())

print("Number of characters:", len(full_name))

names = full_name.split()
first_name = names[0]
last_name = names[-1]

print("First name:", first_name)
print("Last name:", last_name)

print(f"Hello {first_name}! Your full name is {full_name}, and it contains {len(full_name)} characters.")

