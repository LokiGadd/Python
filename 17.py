# Problem 17

'''
A girl is walking along an apple orchard with a bag in each hand. She likes to pick apples from each tree as she goes along, but is meticulous about not putting different kinds of apples in the same bag.

Given an input describing the types of apples she will pass on her path, in order, determine the length of the longest portion of her path that consists of just two types of apple trees.

For example, given the input [2, 1, 2, 3, 3, 1, 3, 5], the longest portion will involve types 1 and 3, with a length of four.
'''

# 4 July 2020

arr = [2, 1, 2, 3, 3, 1, 3, 5]
types = [arr[0]]
max_types = types[:]
length = 1
max_length = length
for a in arr[1:]:
	if a in types:
		length = length + 1
	elif len(types) == 1:
		length = length + 1
		types.append(a)
	else:
		length = 1
		types = [a]
	if max_length < length:
		max_length = length
		max_types = types[:]
print(max_length)
print(max_types)

# Done