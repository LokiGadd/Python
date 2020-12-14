# Problem 16

'''
On a mysterious island there are creatures known as Quxes which come in three colors: red, green, and blue. One power of the Qux is that if two of them are standing next to each other, they can transform into a single creature of the third color.

Given N Quxes standing in a line, determine the smallest number of them remaining after any possible sequence of such transformations.
'''

# 26 June 2020

qux = ['R', 'G', 'B', 'G', 'B']

stack = [qux[0]]
for i in qux[1:]:
	if stack[-1] == i:
		stack.append(i)
	else:
		a = stack.pop()
		stack.append('R') if a != 'R' and i != 'R' else stack.append('G') if a != 'G' and i != 'G' else stack.append('B')
if stack[-1] != stack[-2]:
	a = stack.pop()
	i = stack.pop()
	stack.append('R') if a != 'R' and i != 'R' else stack.append('G') if a != 'G' and i != 'G' else stack.append('B')
print(stack)

# Done