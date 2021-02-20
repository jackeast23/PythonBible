# Ask user for name
name = input('What is your name? ')

# Ask user for age
age = input('How old are you? ')

# Ask user for city
city = input('What city do you live in? ')

# Ask user what they enjoy
hobby = input('What do you enjoy doing in your freetime? ')

# Create output text
user_bio = name + " is " + age + " years old and lives in " + city + ". " + name + " likes " + hobby + "."
string = "Your name is {} and you are {} years old. You live in {} and you like {}."
output = string.format(name, age, city, hobby)

# Print output to screen
print(user_bio)
print(output)