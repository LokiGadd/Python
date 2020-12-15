# Problem 24 |||||||  Reverser
'''

Impliment the reverse function, which takes in input n and reverses it. For instance, reverse(123) should return 321. You should do this without converting the inputted number into a string.

'''
def reverse(n):
    return int(str(n)[::-1])

print(reverse(1234))

# Done