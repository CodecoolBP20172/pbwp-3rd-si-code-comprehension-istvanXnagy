import random  # imports the random module from the library

guessesTaken = 0  # initializes a variable with a value 0

print('Hello! What is your name?')  # prints the string inside the brackets
myName = input()  # creates a variable; it will require a user input. (Said user input will become its value)

number = random.randint(1, 20)  # number variable's value will be a number between and including 1 and 20
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')
# prints the string inside the brackets, which is concatenated from two constant values and a variable

while guessesTaken < 6:  # starting a loop. The indented block will run as long as guessesTaken's value is less than 6
    print('Take a guess.')  # prints the string inside the brackets
    guess = input()  # guess variable will take the value of a user input
    guess = int(guess)  # converts above variable to integer

    guessesTaken += 1  # guessesTaken = guessesTaken + 1

    if guess < number:  # the indented block will run if guess variable's value is less than number variable's
        print('Your guess is too low.')  # prints the string inside the brackets

    if guess > number:  # the indented block will run if guess variable's value is greater than number variable's
        print('Your guess is too high.')  # prints the string inside the brackets

    if guess == number:  # the indented block will run if guess variable's value is equal to number variable's
        break  # breaks out of the loop

if guess == number:  # the indented block will run if guess variable's value is equal to number variable's.
    guessesTaken = str(guessesTaken)  # guessesTaken's value is converted to string
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')
    # prints the string inside the brackets, which is concatenated from three constant values and two variables

if guess != number:  # the indented block will run if guess variable's value is not equal to number variable's
    number = str(number)  # number variable's value is converted to string
    print('Nope. The number I was thinking of was ' + number)
    # prints the string inside the brackets, which is concatenated from a constant value and a variable
