# This is a guess the number game.
import random
from course import course

course1 = course("DBMS", "CSC 325", 3, False)

print(course1.requisite())

def play_game(secretNumber):
    #  Ask the player to guess 6 times.
    for guessesTaken in range(1, 6):
        try:
            guess = int(input('Take a guess: '))
            if guess < secretNumber:
                print('Your guess is lower than the number.')
            elif guess > secretNumber:
                print('Your guess is higher than the number.')
            else:
                break  # This condition is the correct guess!
        except ValueError:
            print('Please enter an integer value\nYour amount of wrong input is deducted'
                  ' from your number of allowed guess')

    if guess == secretNumber:
        print('\nGood job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
    else:
        print('\nHaHa!! GMAE OVER \nYou have exceeded your allowed number of '
              'trial\nThe number I was thinking of is ' + str(secretNumber))


secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20. \nYou are given only 5 trials to guess the number')

consent = input('\nAre you in for the game?\nReply yes to opt in or anything else to opt out\n')

if consent == 'yes':
    play_game(secretNumber)
else:
    print('Lazy you.\nYou opted out.')
