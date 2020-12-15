# Problem 20

'''

Given two words consisting of english letters (uppercase and lowercase) determine whether they are anagrams. In this task assume that small and big letters are indistinguishable. A word is an anagram if it can be formed by rearranging the letters of another word.

Please write a function anagrams(word1, word2) that returns True if word2 is an anagram of word1, or False otherwise.

Length of word1 and word2 is between 11 and 50,00050,000.

'''
# 15 December 2020
def anagrams(word1, word2):
    arr1 = [i for i in word1]
    arr2 = [i for i in word2]
    arr1.sort()
    arr2.sort()
    return arr1 == arr2


word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

print(anagrams(word1.lower(),word2.lower()))

# Done