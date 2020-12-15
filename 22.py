# Problem 22 ||||||   Least Larger
'''

Given an array of numbers and an index, return the index of the least number larger than the element at the given index, or -1 if there is no such index ( or, where applicable, Nothing or a similarly empty value ).

'''
def least_larger(a, i): 
    if max(a) == a[i]:
        return -1
    else:
        temp = a[i]
        b = a[:]
        b.sort()
        for i in b:
            if i > temp:
                break
        return a.index(i)

print(least_larger( [4, 1, 3, 5, 6], 0 ))

# Done