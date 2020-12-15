# 14 December 2020
'''

Problem 19

Write a Python program for a rock-paper-scissors game

'''
import random

print("\n")
print("Let's play ROCK PAPER SCISSORS\n")
n = int(input("How many games do you want to play:"))
print("\n")
comp = 0
val = ''
score = 0

# for ROCK = 0; PAPER = 1; SCISSORS = -1

for i in range(n):
	comp = random.randint(-1,1)
	val = input("Enter (r) for ROCK, (p) for PAPER and (s) for SCISSORS:")
	if val == 'r' and comp == -1:
		score = score + 1
		print("You win, the computer was SCISSORS")
	elif val == 'p' and comp == 0:
		score = score + 1
		print("You win, the computer was ROCK")
	elif val == 's' and comp == 1:
		score = score + 1
		print("You win, the computer was PAPER")
	elif val == 'r' and comp == 1:
		score = score - 1
		print("You lose, the computer was PAPER")
	elif val == 'p' and comp == -1:
		score = score - 1
		print("You lose, the computer was SCISSORS")
	elif val == 's' and comp == 0:
		score = score - 1
		print("You lose, the computer was ROCK")
	else:
		print("Draw")
print("\n")
print("Total score is", score)
print("\n")

# DONE
