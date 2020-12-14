# Problem 14

'''
A fixed point in an array is an element whose value is equal to its index. Given a sorted array of distinct elements, return a fixed point, if one exists. Otherwise, return False.

For example, given [-6, 0, 2, 40], you should return 2. Given [1, 5, 7, 8], you should return False.
'''

# 8 June 2020
arr = [-6,0,2,40]
length = len(arr)

def fixed(arr,length):
	i = 0
	for j in arr:
		if i == j or i-length == j:
			return(j)
		i = i + 1
	return(False)

print(fixed(arr,length))

# Done