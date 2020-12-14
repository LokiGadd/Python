# Problem 12

'''
Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
'''

# 6 October 2019

string = str(input("Give a bracket string:"))

arr = [string[0]]
for i in string[1:]:
	if i == ")" and arr[-1] == "(":
		del arr[-1]
	elif i == "]" and arr[-1] == "[":
		del arr[-1]
	elif i == "}" and arr[-1] == "{":
		del arr[-1]
	else:
		arr.append(i)
if len(arr) == 0:
	print(True)
else:
	print(False)

# Done
