from random import choice

questions = ["Why is the sky blue?: ", "Is the moon made of cheese?: ", "What's your favourite dinosaur?: "]

question = choice(questions)
answer = input(question).strip().lower()

while answer != "just because":
    answer = input("Why?: ").strip().lower()

print("Oh... Okay")