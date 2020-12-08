#Leetcode 1641. Count Sorted Vowel Strings

'''
Problem statement: 
Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.

A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.

 

Example 1:

Input: n = 1
Output: 5
Explanation: The 5 sorted strings that consist of vowels only are ["a","e","i","o","u"].
Example 2:

Input: n = 2
Output: 15
Explanation: The 15 sorted strings that consist of vowels only are
["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.
Example 3:

Input: n = 33
Output: 66045
Constraints:

1 <= n <= 50 
'''
#Approach: math:
'''
The solution is purely based on observations when building the desired strings :

String of length n is constructed based on string of length n-1. So we can think of what are available options based on the character at position n-1th.
There are 5 options after a (i.e (a, e, i, o, u).
There are 4 options after e (i.e (e, i, o, u).
There are 3 options after i (i.e (i, o, u).
There are 2 options after o (i.e (o, u).
There is 1 option after u (i.e (u).
This solution beats 95.95% but I believe it's quite optimal unless there is a way to improve my python3 code. So, any comments are much appreciated.


'''
def countVowelStrings(n):
    #base case:
    if not n: 
        return None
    if n == 1:
        return 5
    #available options to build a vowel strings
    count = [5,4,3,2,1]
    while n > 2:
        count = [sum(count[i:]) for i in range(5)]
        n-=1

    return sum(count)


#DP approach: through recursion

def countVowelStrings_DP(n):
    #base case: 
    if not n: 
        return 1

    #helper method to recursively counting the vowel string
    def recursion(k, n):
        if  k == 1: 
            return 1
        if n == 1:
            return k

        result = 0 
        while k >= 1: 
            result += recursion(k, n-1)
            k-=1

        return result
    return recursion(5, n)


#Main function to run the program: 
def main():
    print("TESTING COUNT SORTED VOWEL STRING...")
    n_1 = 1
    n_2 = 2 
    n_3 = 33
    print(countVowelStrings(n_1))
    print(countVowelStrings(n_2))
    print(countVowelStrings(n_3))
    print(countVowelStrings_DP(n_3))
    print("END OF TESTING...")

main()