print("Welcome to the love calculator")
name1 = (input("What is YOUR name? ")).lower()
name2 = (input("What is their name? ")).lower()

true = 0
love = 0

true += name1.count("t") + name2.count("t")
true += name1.count("r") + name2.count("r")
true += name1.count("u") + name2.count("u")
true += name1.count("e") + name2.count("e")

love += name1.count("l") + name2.count("l")
love += name1.count("o") + name2.count("o")
love += name1.count("v") + name2.count("v")
love += name1.count("e") + name2.count("e")


score = 10 * true + love

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else :
    print(f"Your score is {score}.")





# 💪 This is a Difficult Challenge 💪
# Instructions

# You are going to write a program that tests the compatibility between two people.
# To work out the love score between two people:
#     Take both people's names and check for the number of times the letters in the word TRUE occurs. 
#     Then check for the number of times the letters in the word LOVE occurs. 
#     Then combine these numbers to make a 2 digit number.
# For Love Scores less than 10 or greater than 90, the message should be:
# "Your score is **x**, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:
# "Your score is **y**, you are alright together."
# Otherwise, the message will just be their score. e.g.:
# "Your score is **z**."
# e.g.
# name1 = "Angela Yu"
# name2 = "Jack Bauer"
# T occurs 0 times
# R occurs 1 time
# U occurs 2 times
# E occurs 2 times
# Total = 5

# L occurs 1 time
# O occurs 0 times
# V occurs 0 times
# E occurs 2 times

# Total = 3

# Love Score = 53

# Print: "Your score is 53."
# Example Input 1

# name1 = "Kanye West"
# name2 = "Kim Kardashian"

# Example Output 1

# Your score is 42, you are alright together.

# Example Input 2

# name1 = "Brad Pitt"
# name2 = "Jennifer Aniston"

# Example Output 2

# Your score is 73.

# e.g. When you hit run, this is what should happen:

# The testing code will check for print output that is formatted like one of the lines below:

# "Your score is 47, you are alright together."
# "Your score is 125, you go together like coke and mentos."
# "Your score is 54."

# Hint

#     The lower() function changes all the letters in a string to lower case.

# https://stackoverflow.com/questions/6797984/how-do-i-lowercase-a-string-in-python

#     The count() function will give you the number of times a letter occurs in a string.

# https://stackoverflow.com/questions/1155617/count-the-number-occurrences-of-a-character-in-a-string
# Test Your Code

# Check your code is doing what it is supposed to. When you're happy with your code, click submit to check your solution.
# Solution

# https://repl.it/@appbrewery/day-3-5-solution
# Files

