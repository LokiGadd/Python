# Problem 27

'''

A number m of the form 10x + y is divisible by 7 if and only if x − 2y is divisible by 7. In other words, subtract twice the last digit from the number formed by the remaining digits. Continue to do this until a number known to be divisible or not by 7 is obtained; you can stop when this number has at most 2 digits because you are supposed to know if a number of at most 2 digits is divisible by 7 or not.

Example:
m = 371 -> 37 − (2×1) -> 37 − 2 = 35 ; thus, since 35 is divisible by 7, 371 is divisible by 7.

seven(371) should return [35, 1]
seven(1603) should return [7, 2]
seven(477557101) should return [28, 7]
seven(109) should return [-8, 1]

'''
def seven(m):
    n=0
    while m//10 >= 10:
        m = m//10 - 2*(m%10)
        n += 1
    
    number = (m,n)
    return number

print(seven(371))

# Done