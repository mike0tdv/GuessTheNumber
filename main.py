import random
import sys

# Declaring the variables
used_numbers = []
tries = 0
success = False


# A function to check if the user entered the correct number
def guessing(guess):
    global used_numbers, tries, success, random_num

    if guess == random_num:
        success = True
    if guess is not random_num:
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

while success == False:
    guess = int(input("Enter your guess: "))
    guessing(guess)
    print("The numbers you have used: ")
    for num in used_numbers:
        print(num, end=", ")
    print()
else: print(f"Congrats! You guessed the number - {random_num} with {tries} tries!")