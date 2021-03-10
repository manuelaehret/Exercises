import random
to_guess = random.randrange(0, 100)
print("Try to guess which number between 0 and 100 I'm thinking of!")

user_guess = int(input("Your guess: "))
if user_guess == to_guess:
    print("That's correct!")
elif user_guess > to_guess:
    print("No it's lower.")
else:
    print("No it's higher.")
