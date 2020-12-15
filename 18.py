# 15 December 2020
'''

Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

'''
def sorting(arr,index):
    arr.sort(key = lambda x : x[index])
    return arr

N = int(input())
name = ''
score = 0.0
arr = []
for i in range(N):
    name = input()
    score = float(input())
    arr.append([name,score])

arr = sorting(arr,0)
arr = sorting(arr,1)
score = 0.0
for i in arr:
    if i[1] != arr[0][1]:
        if score == 0.0:
            score = i[1]
            print(i[0])
        elif score == i[1]:
            print(i[0])
        else:
            break

# DONE