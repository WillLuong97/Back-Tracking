#Problem 1415. The k-th Lexicographical String of All Happy Strings of Length n

'''
A happy string is a string that:

consists only of letters of the set ['a', 'b', 'c'].
s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is 1-indexed).
For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings and strings "aa", "baa" and "ababbc" are not happy strings.

Given two integers n and k, consider a list of all happy strings of length n sorted in lexicographical order.

Return the kth string of this list or return an empty string if there are less than k happy strings of length n.

 Example 1:

Input: n = 1, k = 3
Output: "c"
Explanation: The list ["a", "b", "c"] contains all happy strings of length 1. The third string is "c".
Example 2:

Input: n = 1, k = 4
Output: ""
Explanation: There are only 3 happy strings of length 1.
Example 3:

Input: n = 3, k = 9
Output: "cab"
Explanation: There are 12 different happy string of length 3 ["aba", "abc", "aca", "acb", "bab", "bac", "bca", "bcb", "cab", "cac", "cba", "cbc"]. You will find the 9th string = "cab"
Example 4:

Input: n = 2, k = 7
Output: ""
Example 5:

Input: n = 10, k = 100
Output: "abacbabacb"
 

Constraints:

1 <= n <= 10
1 <= k <= 100

'''
def getHappyString(n, k):
	#base case:
	if not n: 
		return ""

	string = ['a', 'b', 'c']
	result = []

	#helper method to backtrack once the conditions has failed and look for other solution
	def backtracking(letters, choice, count, n):
		#base case: the word we are creating has reached its length limit: 
		if count == n:
			result.append(choice)
			return
		for i in  letters:
			if len(choice) == 0 or choice[-1] != i:
				backtracking(letters, choice+i, count+1, n)
			else:
				continue

	backtracking(string, "", 0, n)
	
	#if the kth element cannot be found
	if  k > len(result):
		return ""

	return result[k-1]


#main function to run the test cases: 
def main():
	print("TESTING KTH LEXICOGRAPHICAL STRING OF ALL HAPPY STRINGS OF LENGHT N...")
	
	n_1 = 1
	k_1 = 3

	n_2 = 1
	k_2 = 4

	n_3 = 3
	k_3 = 9

	n_4 = 2
	k_4 = 7

	n_5 = 10
	k_5 = 100
	
	print(getHappyString(n_1, k_1))
	print(getHappyString(n_2, k_2))
	print(getHappyString(n_3, k_3))
	print(getHappyString(n_4, k_4))
	print(getHappyString(n_5, k_5))



	print("END OF TESTING...")

	
main()
