# TODO: Setup the game
#   TODO: creation of hidden combination
#       pseudocode:
#           take a list of all the colours
#           randomly select 5 from the list
#           return the hidden combination
#           # Now we have the hidden combination, we can start the game

import random

list_of_colours = ["red", "blue", "green", "yellow", "purple", "orange"]
amount_of_spaces = 5
guess_correctness = []

hidden_combination_list = []
for i in range(amount_of_spaces):
    hidden_combination_list.append(random.choice(list_of_colours))

print(hidden_combination_list)

def answer_function(user_guess_list, hidden_combination_list):
    guess_correctness = []
    if user_guess_list == hidden_combination_list:
        print(user_guess_list)
        return "win"
    else:
        for x in range(amount_of_spaces):
            if user_guess_list[x] == hidden_combination_list[x]:
                print(f"Correct colour in space {x + 1}")
                guess_correctness.append("black")
            elif user_guess_list[x] in hidden_combination_list:
                # check for if the colour is in the hidden combination but not in the right place
                print(f"Wrong place, right colour in space {x + 1}")
                guess_correctness.append("white")
            else:
                print(f"Wrong colour in space {x + 1}")
                guess_correctness.append("blank")
    return guess_correctness


def algorithm_colour_fill():
    algorithm_guess = []
    algorithm_known = [0, 0, 0, 0, 0] # make it so we can directly change which space from 1 to 5 is what colour based on what we know
    for i in range(len(list_of_colours)):
        for j in range(amount_of_spaces):
            algorithm_guess.append(list_of_colours[i])

        guess_correctness = answer_function(algorithm_guess, hidden_combination_list)
        print(guess_correctness)
        for x in range(len(guess_correctness)):
            if guess_correctness[x] == "black":
                algorithm_known[x] = list_of_colours[i]

        print(f"algorithm_known: {algorithm_known}")
        # add somehow that it records all the correct colours into algorithm known
        algorithm_guess = []
        # guess for each colour in the range of colours for all the spaces
        # record when a colour is guessed correctly and their space
        #   a list of correct spaces will be appended with the right values
        #   for each correct space append the list with the specific space
        #   then the algorithm will use this list to solve the puzzle later on
        # move on to the next colour
        # until all spaces are filled
        # then solve with the right colours
        #
    return answer_function(algorithm_known, hidden_combination_list) == "win"




# TODO: Solving algorithm
#   pseudocode:
#      there are about 60000 possible combinations so we need to find a normal working strategy that has
#      a good chance of finding the hidden combination in a reasonable number of guesses, while for start being simple
#      we can start with a brute force approach where it goes through all possible colours and fills each row fully with one colour
#      then it moves on to the next row and repeats the process with all possible colours
#      takes notes of all the colours it has tried and their corresponding feedback
#      when it has filled all 5 places, it solves the puzzle


# TODO: game functions themselves
#       how to input your guess
#       checking of your guess
#       telling you how many correct colours you have
#           there are 3 possible outcomes:
#               right place, right colour
#               wrong place, right colour
#               wrong place, wrong colour

while True:
    user_guess_list = []
    for i in range(amount_of_spaces):
        user_guess = input("Enter your guess: ")
        if user_guess == "use algorithm": # TODO: Giving the algorithm ability to solve and play the game
            algorithm_colour_fill()
            continue
        user_guess_list.append(user_guess)
    answer_function(user_guess_list, hidden_combination_list)
