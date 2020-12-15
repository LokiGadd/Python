# Problem 26

'''

My friend John and I are members of the "Fat to Fit Club (FFC)". John is worried because each month a list with the weights of members is published and each month he is the last on the list which means he is the heaviest.

I am the one who establishes the list so I told him: "Don't worry any more, I will modify the order of the list". It was decided to attribute a "weight" to numbers. The weight of a number will be from now on the sum of its digits.

For example 99 will have "weight" 18, 100 will have "weight" 1 so in the list 100 will come before 99. Given a string with the weights of FFC members in normal order can you give this string ordered by "weights" of these numbers?

Example:

"56 65 74 100 99 68 86 180 90" ordered by numbers weights becomes: "100 180 90 56 65 74 68 86 99"
When two numbers have the same "weight", let us class them as if they were strings (alphabetical ordering) and not numbers: 100 is before 180 because its "weight" (1) is less than the one of 180 (9) and 180 is before 90 since, having the same "weight" (9), it comes before as a string.
All numbers in the list are positive numbers and the list can be empty.

'''
def order_weight(strng):
    if strng == "":
        return strng
    number = list(map(int, strng.split(" ")))
    l = len(number)
    num = [0]*l
    dig = 0
    n=0
    i=0

    for i in range(l):
        num[i] = number[i]
        tot=0
        n=num[i]
        while(n>0):
            dig=n%10
            tot=tot+dig
            n=n//10
        num[i] = tot
    i=l-1
    j=0
    temp=0
    while i>=1:
        j=i-1
        while j>=0:
            if (num[j]>num[i]):
                temp = num[j]
                num[j] = num[i]
                num[i] = temp
                temp = number[j]
                number[j] = number[i]
                number[i] = temp
            elif (num[j] == num[i] and str(number[j]) > str(number[i])):
                temp = number[j]
                number[j] = number[i]
                number[i] = temp
            j -= 1
        i -= 1
    for i in range(l):
        number[i] = str(number[i])
    return " ".join(number)

print(order_weight("56 65 74 100 99 68 86 180 90"))

# Done