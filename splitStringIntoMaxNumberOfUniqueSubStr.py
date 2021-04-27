#Problem 1593. Split a String Into the Max Number of Unique Substrings

'''
Given a string s, return the maximum number of unique substrings that the given string can be split into.

You can split string s into any list of non-empty substrings, where the concatenation of the substrings forms the original string. However, you must split the substrings such that all of them are unique.

A substring is a contiguous sequence of characters within a string.
Example 1:

Input: s = "ababccc"
Output: 5
Explanation: One way to split maximally is ['a', 'b', 'ab', 'c', 'cc']. Splitting like ['a', 'b', 'a', 'b', 'c', 'cc'] is not valid as you have 'a' and 'b' multiple times.
Example 2:

Input: s = "aba"
Output: 2
Explanation: One way to split maximally is ['a', 'ba'].
Example 3:

Input: s = "aa"
Output: 1
Explanation: It is impossible to split the string any further.
 

Constraints:

1 <= s.length <= 16

s contains only lower case English letters.

Approach: use backtracking and dfs to check each element in the string and match them with a set that contains other element in the string, 
if an element is already in the set() we will back out of the current recursion and mutated the current string with the next elemnt in
the original array and keep repeating this process until we have found all substring
'''
def maxUniqueSplit(s):
	#helper method to check each element in the string
	def backtracking(string, strSoFar = set()):
		#base case: if the string has a lenght of 1 and it is also in the set, so we do not
		# have to look anymore as it is the last element
		if len(string) == 1 and string in strSoFar:
			return 0 
		
		maxLen = len(strSoFar) + 1
		#loop through each element in the string and put them into the set to
		for i in range(1, len(string)):
			a = string[:i]
			b = string[i:]
			if a not in strSoFar:
				maxLen = max(maxLen, backtracking(b, strSoFar|{a}))
		return maxLen

	return backtracking(s)
	




#Main function to run the test case: 
def main():
	print("TESTING Split a String Into the Max Number of Unique Substrings...")
	s = "ababccc"
	print(maxUniqueSplit(s))
	s = "aba"
	print(maxUniqueSplit(s))
	s = "aa"
	print(maxUniqueSplit(s))


	print("END OF TESTING...")

main()
