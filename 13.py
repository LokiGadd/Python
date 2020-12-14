# Problem 13

'''
The transitive closure of a graph is a measure of which vertices are reachable from other vertices. It can be represented as a matrix M, where M[i][j] == 1 if there is a path between vertices i and j, and otherwise 0.
'''

# 21 May 2020

graph = [[0, 1, 3],[1, 2],[2],[3]]

def if_connected(i,j):
	if j in graph[i]:
		return 1
	else:
		for k in graph[i][1:]:
			if if_connected(k,j)==1:
				return 1
		return 0
length = len(graph)
arr = [[0]*length]*length
for i in range(length):
	for j in range(length):
		arr[i][j] = if_connected(i,j)
	print(arr[i])

# Done