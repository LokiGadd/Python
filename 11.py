# Problem 11

'''
Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
'''

# 30 September 2019

arr = [(30, 75), (0, 50), (60, 150)]

start = []
end = []
ans = 0
for i in arr:
	ans = ans + 1
	start = start + [i[0]]
	end = end + [i[1]]

for i in start:
	for j in end:
		if i >= j:
			ans = ans - 1

print(ans)

# Done
