# Problem 21

'''

Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging its digits. For example:
12 ==> 21
513 ==> 531
2017 ==> 2071


'''
def next_bigger(n):
    ind = -1
    arr = [int(d) for d in str(n)]
    length = len(arr)
    for i in range(1,length):
        if (arr[-i] > arr[-(i+1)]):
            ind = i+1
            break
    if (ind == -1):
        return (-1)
    index = 0
    b_arr = [0]*ind
    for i in range(ind):
        b_arr[i] = arr[-ind+i]
    b_arr.sort()
    for i in range(ind-1):
        if (b_arr[i] == arr[-(ind)]):
            index = i+1
    temp = b_arr[index]
    del b_arr[index]
    arr = arr[:length-ind] + [temp] + b_arr
    answer = ''
    for c in arr:
        answer += str(c)
    return int(answer)

print(next_bigger(12))

# Done