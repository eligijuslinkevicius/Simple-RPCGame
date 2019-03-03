import os
from random import randint

choices = ['r', 'p', 's']
playerAlive = True

print(" ~ (r)ock, (p)aper or (s)cissors?\n")

# conditions
def playerWon():
	print("You won!")
	playerAlive = True

def draw():
	print("Draw!")
	playerAlive = True

def lost():
	print("You lost...")
	playerAlive = False
	askToRestart()

# Game logic
def game():
	# Giving data
	playerInput = input("Your turn: ")
	botInput = choices[randint(0, len(choices) - 1)]
	print("Bot chose: " + botInput)

	# Game logic
	if (playerInput == 'r' and botInput == 'r'):
		draw()

	elif (playerInput == 'r' and botInput == 'p'):
		lost()

	elif (playerInput == 'r' and botInput == 's'):
		playerWon()

	elif (playerInput == 'p' and botInput == 'r'):
		playerWon()

	elif (playerInput == 'p' and botInput == 'p'):
		draw()

	elif (playerInput == 'p' and botInput == 's'):
		lost()

	elif (playerInput == 's' and botInput == 'r'):
		lost()

	elif (playerInput == 's' and botInput == 'p'):
		playerWon()

	elif (playerInput == 's' and botInput == 's'):
		draw()

	else:
		print("Something went wrong!")
		playerAlive = False


# Game loop. Works as long as the player is alive
while playerAlive:
	game()