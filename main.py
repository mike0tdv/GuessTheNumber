import random
import sys

# Declaring the variables
used_numbers = []
tries = 0
failed = True
below = True

# A function to check if the user entered the correct number
def guessing(guess):
    global used_numbers, tries, failed, random_num, below

    if guess == random_num:
        failed = False
        tries += 1
    if guess is not random_num:
        if random_num > guess:
            below = True
        else: below = False
        used_numbers.append(guess)
        tries += 1


# Choosing a range for the random number to be chosen from
print("Enter the range of numbers! The minimum range should be 5!")
num1 = int(input("The beginning of the range: "))
num2 = int(input("The end of the range: "))

if num1 == num2 or 5 > num2 - num1 or num1 > num2:
    print("Nuh uh")
    sys.exit()

random_num = random.randint(num1, num2)

# Loop in which the user tries to guess the number
while failed:
    guess = int(input("Enter your guess: "))
    guessing(guess)

    # Tell the user where is the random number compared to the one they have guessed
    if below:
        print("The correct number is above the number you have guessed!")
    else: print("The correct number is below the number you have guessed!")

    # Print out the used numbers
    print("The numbers you have used: ")
    for num in used_numbers:
        print(num, end=", ")
    print()

    # Prints out when the game ends
else: print(f"Congrats! You guessed the number - {random_num} with {tries} tries!")