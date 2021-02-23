students = {"Alice": 25, "Bob":27, "Claire": 17, "Dan": 21, "Emma": 22}

print(students)

print(students["Dan"])

# Add a student to the dictionary
students["Fred"] = 25
print(students["Fred"])
print(students)

# Change the data held in the dictionary keys
students["Alice"] = 26

# Remove a student from the dictionary
del students["Fred"]

# Convert keys to a list
a = (list(students.keys()))

# Access data stored in keys in a certain range
print(list(students.values())[2:])