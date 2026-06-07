"""
Your job is to complete the definitions of each function mentioned in the comments so that it achieves its indicated behavior.

Do not run this file directly.
Rather, call whichever functions defined in this file that you want to run from within the file named main.py and run that file directly.
"""

import random

##--------------------- Function #1 ---------------------##
# Define a function named 'get_random_int'.
# This function accepts two arguments: a minimum value and a maximum value.
# The function must return a random integer between these two values, inclusive.
# Use the function random.randint() to generate the pseudo-random number.
def get_random_int(min_value, max_value) :
    random_integer = random.randint(min_value, max_value)
    return random_integer
    


##--------------------- Function #2 ---------------------##
# Define a function named 'get_guess'.
# This function accepts a single argument - an integer that serves as a max value.
# This function asks the user once to guess a random integer between 1 and the max value, inclusive.
# The function calls the function named get_random_int in order to generate the random integer in this range.
# If the user has entered an invalid response (i.e. anything that is not an integer in this range), the function returns an integer, -1.
# If the user has guessed the random integer correctly, this function returns a boolean True.
# If the user has guessed incorrectly, this function returns a boolean False.
def get_guess(max_value) :
    guess = input(f"Guess an integer between 1 and {max_value}")

    random_integer = get_random_int(1,max_value)

    if not guess.isdigit() or int(guess) < 1 or int(guess) > max_value : 
        return -1 
    
    elif int(guess) == random_integer : 
        return True 
    
    elif int(guess) != random_integer : 
        return False 
    


##--------------------- Function #3 ---------------------##
# Define a function named 'play_game'.
# This function does not accept any arguments.
# This function uses the get_guess function to ask the user four times to guess a random integer between 1 and 5, inclusive.
# Each time the user guesses, they are immediately informed whether they guessed correctly or not, with the printed output, "Correct!" or "Wrong!"
# If at any time, the user enters an invalid response, the program immediately prints out the text, "Invalid response!" and does not print out anything further.
# At the end, the function, assuming the user has entered all valid guesses, the program prints out the percent of guesses that user guessed correctly, following the format: "You guessed 75% of the random numbers correctly."

def play_game() : 

    result1 = get_guess(5)
    if result1 == -1 : 
        print("Invalid response!")
        return 
    
    elif result1 == True : 
        print("Correct!")

    elif result1 == False : 
        print("Wrong!")

    result2 = get_guess(5)
    if result2 == -1 : 
        print("Invalid response!")
        return 
    
    elif result2 == True : 
        print("Correct!")

    elif result2 == False : 
        print("Wrong!")

    result3 = get_guess(5)
    if result3 == -1 : 
        print("Invalid response!")
        return 
    
    elif result3 == True : 
        print("Correct!")

    elif result3 == False : 
        print("Wrong!")

    result4 = get_guess(5)
    if result4 == -1 : 
        print("Invalid response!")
        return 
    
    elif result4 == True : 
        print("Correct!")

    elif result4 == False : 
        print("Wrong!")

    correct = result1 + result2 + result3 + result4 # since return was added, the function wont subtract -1 here. Boolean True = 1, Boolean False = 0

    percent = int((correct/4) * 100)
    print(f"You guessed {percent}% of the random numbers correctly.")


    
