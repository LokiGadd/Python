# Problem 15

'''
A classroom consists of N students, whose friendships can be represented in an adjacency list.

Each student can be placed in a friend group, which can be defined as the transitive closure of that student's friendship relations. In other words, this is the smallest set such that no student in the group has any friends outside this group.

Given a friendship list such as the one above, determine the number of friend groups in the class.
'''

# 14 June 2020

group = {0: [1, 2], 1: [0, 5], 2: [0], 3: [6], 4: [], 5: [1], 6: [3]}

def listmerge(list1,list2):
	return(list(set(list1+list2)))

def fri(group,n):
	arr = group[n] + [n]
	for i in group[n]:
		if i>n:
			arr = listmerge(arr,fri(group,i))
	return(arr)

over = fri(group,0)
b = over
print(over)
for i in group.keys():
	if i not in over:
		b = fri(group,i)
		print(b)
		over = listmerge(over,b)

# Done