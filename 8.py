'''

8. Write a Python program to convert the given string into a morse code.

'''
def morse(letter):
    if letter == 'A':
        return ('. _')
    if letter == 'B':
        return ('_ . . .')
    if letter == 'C':
        return ('_ . _ .')
    if letter == 'D':
        return ('_ . .')
    if letter == 'E':
        return ('.')
    if letter == 'F':
        return ('. . _ .')
    if letter == 'G':
        return ('_ _ .')
    if letter == 'H':
        return ('. . . .')
    if letter == 'I':
        return ('. .')
    if letter == 'J':
        return ('. _ _ _')
    if letter == 'K':
        return ('_ . _')
    if letter == 'L':
        return ('. _ . .')
    if letter == 'M':
        return ('_ _')
    if letter == 'N':
        return ('_ .')
    if letter == 'O':
        return ('_ _ _')
    if letter == 'P':
        return ('. _ _ .')
    if letter == 'Q':
        return ('_ _ . _')
    if letter == 'R':
        return ('. _ .')
    if letter == 'S':
        return ('. . .')
    if letter == 'T':
        return ('_')
    if letter == 'U':
        return ('. . _')
    if letter == 'V':
        return ('. . . _')
    if letter == 'W':
        return ('. _ _')
    if letter == 'X':
        return ('_ . . _')
    if letter == 'Y':
        return ('_ . _ _')
    if letter == 'Z':
        return ('_ _ . .')

print ("\n")
word = input("Enter the sentence : ")
for i in range(0,len(word)):
    if word[i] == ' ':
        print ("     ", end='')
    else:
        print(morse(word[i]), end='')
        print ("  ", end='')
print ("\n")
