'''

3. Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14

'''
import datetime
now = datetime.datetime.now()
print("Date and time:")
print(now)
#print(now.strftime("%Y-%m-%d %H:%M:%S"))

'''
The datetime module supplies classes for manipulating dates and times in both simple and complex ways. datetime.now(tz=None) returns the current local date and time. If optional argument tz is None or not specified, this is like today().
'''