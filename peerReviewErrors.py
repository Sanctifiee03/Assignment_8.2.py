# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: Sanctifiee Musafiri Mimo
# Creation Date: September 26th,2020
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')

	#print() 
	#There is no need for this because we are not passing in any argument and it is just doing nothing in the code


def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':

		#print('Which cave will you go into? (1 or 2)')
		#cave = input()
		#The above commands should combine as corrected and not separately
	    cave = input('Which cave will you go into? (1 or 2)')
	#return caves
	return cave
	#caves is not defined. Only cave is defined and this need to be indented in the function
	

def checkCave(chosenCave):
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
	time.sleep(3)
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	# print()
	##There is no need for this because we are not passing in any argument and it is just doing nothing in the code
	#sleep for 2 seconds
	time.sleep(2)
	#friendlyCave = random.randint(1, 2)
	friendlyCave = random.randint(1, 2)

	if chosenCave == str(friendlyCave):
		print('Gives you his treasure!')
	else:
		#print 'Gobbles you down in one bite!'
		print ('Gobbles you down in one bite!')
		#parenthesis were missing
"""
playAgain = 'yes'
#while playAgain = 'yes' or playAgain = 'y':
while playAgain == 'yes'or playAgain =='y':
	#There should be double equals (==)instead of just one (=)
	displayIntro()
	caveNumber = choosecave()
	checkCave(caveNumber)
    
	#print('Do you want to play again? (yes or no)')
	#playAgain = input()
	playAgain = input('Do you want to play again? (yes or no)')
	#The above commands should combine as corrected and not separately
"""
#The above code needs to be indented once to run.
playAgain = 'yes'
#while playAgain = 'yes' or playAgain = 'y':
while playAgain == 'yes'or playAgain =='y':
	#There should be double equals (==)instead of just one (=) for assignment
	displayIntro()
	#caveNumber = choosecave()
	caveNumber = chooseCave()
	#choosecave in not defined it needs to be chooseCave which is defined
	checkCave(caveNumber)
    
	#print('Do you want to play again? (yes or no)')
	#playAgain = input()
	playAgain = input('Do you want to play again? (yes or no)')
	#The above commands should combine as corrected and not separately


	if playAgain == "no":
		print("Thanks for planing")

