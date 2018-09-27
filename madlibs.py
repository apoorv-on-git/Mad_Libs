#Soft Code for the Mad Libs Game.

#Importing all the useful packages.

import os, random

#Empty Variables defined to use them as globals between the functions.

story = ""

dictionary = ""

#Function defined to choose a random theme from the folder for user to play.

def madlibs_theme():
	
	global story

	print ("Let's play Mad Libs")

	#Choosing a random theme from the designated folder.
	
	random_choice = random.choice(os.listdir('./Themes'))

	#Changing the directory of the python program as the program is situated in a different directory.
	
	cd = os.chdir('./Themes')
	f = open(random_choice, 'r')

	#To filter the title of the theme.
	
	split_story = f.read().split('\n')

	#To filter the contents of the theme.

	story = [split_story[0], split_story[1].split(' ')]

	print ("We have selected {} theme for you".format(story[0]))

	#Calling another function.
	input_dictionary()

#Function defined to take the input from the user.

def input_dictionary():
	
	global story
	global dictionary
	print ("Now enter the appropriate words to create your own funny version of the theme.")

	#To store the user input.
	
	dictionary = {}

	#Interating over the first element of story, which is a list.

	for i in story[1]:
		
		if i.isupper() and len(i) > 1:
			value = ''

			#While loop so user doesn't leaves the input blank.
			while len(value) == 0:
				value = input("Please enter a {} -> ".format(i))
			dictionary[i] = value
	
	#Calling another function.
	
	madlib_output()

#Function defined to display the final output with user's answers.
					
def madlib_output():

	global story
	global dictionary

	#Variable defined to store the final result.
	
	final_string = ''

	#Interating over the first element of the story, which is a list.
	
	for i in story[1]:

		#Replacing the older elements of the list with the user input.
	
		if i in dictionary:
			i = dictionary[i]

		final_string = final_string + ' ' + i

	#Printing the final result.
	
	print (final_string)

#Calling the first function to start the game.
madlibs_theme()

#ENJOY
