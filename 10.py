# Problem 10

'''
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
'''

# 11 September 2019

array = [1, 2, 3, 4, 5]
arr1 = [3, 2, 1]
def p2(array):
	product = 1
	for i in array:
		product = product*i
	for i in range(len(array)):
		array[i] = product//array[i]
	return (array) 


print(p2(array))
print(p2(arr1))

# Done
