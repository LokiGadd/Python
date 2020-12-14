# Problem 9

'''
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
'''

# 10 September 2019

k = 17
array = [10, 15, 3, 7]
def p1(k , array):
	for i in array:
		if k-i in array:
			return ("True")
	return ("False") 


print(p1(k, array))

# Done
