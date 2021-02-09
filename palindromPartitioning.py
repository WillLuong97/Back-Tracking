#Problem 131. Palindrome Partitioning
'''
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
 

Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.
'''
def partition(s):
	#the result array that stores all the element
	result = []
	#the array to store the current partition in each recursive call
	part = []
	
	#helper method to perform dfs search on all substring combination
	def dfs(i):
		#base case: if this recursion falls on an index that is out of bound, then we will stop the recursion and append 
		#the current partition onto the result array
		if i >= len(s):
			result.append(part.copy())
			return
		for j in range(i, len(s)):
			#check to see if the current substring is a palindrome or not
			if isPalindrome(s, i, j):
				part.append(s[i:j+1])
				dfs(j+1)
				part.pop()
	
	dfs(0)
	return result

#Function to check if a string is a palindrome or not
def isPalindrome(string, left, right):
	while left <= right:
		if string[left] != string[right]:
			return False
		left += 1
		right -= 1
	return True	
#Main function to run the test cases: 
def main():
	print("TESTING PALINDROME PARTITIONING...")
	s_1 = "aab"
	s_2 = "a"
	print(partition(s_1))
	print(partition(s_2))
	print("END OF TESTING...")

main()
