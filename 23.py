# Problem 23 ||||||| Basic Sequence Practice

'''

Complete the function that takes an integer n and returns a list/array of length abs(n) + 1 of the arithmetic series explained above. Whenn < 0 return the sequence with negative terms.

Example:    5  -->  [0,  1,  3,  6,  10,  15]
            -5  -->  [0, -1, -3, -6, -10, -15]
            7  -->  [0,  1,  3,  6,  10,  15,  21,  28]

'''
def sum_of_n(n):
    value = abs(n)
    sign = 0
    if value != 0:
        sign = n//value
    a = [0]
    for i in range(1,value+1):
        a.append(i*(i+1)*sign/2)
    return a

print(sum_of_n(5))

# Done