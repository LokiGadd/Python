# Problem 18

'''
Given a clock time in hh:mm format, determine, to the nearest degree, the angle between the hour and the minute hands.

Bonus: When, during the course of a day, will the angle be zero?
'''

# 9 July 2020

time = '10:30'
arr = [int(a) for a in time.split(':')]

# angle with minute hand = 6*mm degrees.
angle_1 = 6*arr[1]
# angle with hour hand = 30*hh + 0.5*mm degrees
angle_2 = 30*arr[0] + arr[1]/2

print(angle_2 - angle_1)

# Done