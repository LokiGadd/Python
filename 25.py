# Problem 25 ||||||||    Simple string expansion
'''

Given a string, return the expansion of that string.

Input will consist of only lowercase letters and numbers (1 to 9) in valid parenthesis. There will be no letters or numbers after the last closing parenthesis.

Example:
solve("3(ab)") = "ababab"     -- because "ab" repeats 3 times
solve("2(a3(b))") = "abbbabbb" -- because "a3(b)" == "abbb", which repeats twice.

'''
def solve(st):
    stack = [i for i in st]
    ans = ""
    for i in stack[::-1]:
        if i != "(" and i != ")":
            if i in "123456789":
                ans = ans*int(i)
            else:
                ans = ans + i
            
    return ans[::-1]

print(solve("3(ab)"))

# Done