#Problem 216. Combination Sum III
'''
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.
Example 3:

Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations. [1,2,1] is not valid because 1 is used twice.
Example 4:

Input: k = 3, n = 2
Output: []
Explanation: There are no valid combinations.
Example 5:

Input: k = 9, n = 45
Output: [[1,2,3,4,5,6,7,8,9]]
Explanation:
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45
there are no other valid combinations.

Constraints:

2 <= k <= 9
1 <= n <= 60
'''
def combinationSum3(k, n):
	result = []
	searchSpace = [1,2,3,4,5,6,7,8,9]
	#helper method to recursively checking for all possible combinations from 1 to 9:
	def backtrack(path, k, n, search, pos):
		#if the sub array has reached the size limit, then we will check to see how if it could be sum to n or not
		#if it is, append the current path into the result and backtrack out and check for the next element
		if len(path) == k:
			if sum(path) == n:
				result.append(path)
				return 
		#otherwise, stil backtrack out to check for the next element
			else: 
				return
		
		#if the path is not yet reached the maximum length, then we will keep building the solution
		for x in search[pos+1:]:
			pos += 1
			#recurse further into the rest of the array
			if len(path) <= k and x not in path:
				backtrack(path + [x], k, n, search, pos)
			else:
				return  
				 

	#loop through the array and compose the first number in the sub array
	for i in range(1, 10):
		backtrack([i], k, n, searchSpace, 0) 
	return result

#Main function to run the test case: 
def main():
	print("TESTING COMBINATION SUM III...")
	k = 3
	n = 7	
	print(combinationSum3(k, n))
	k = 3
	n = 9
	print(combinationSum3(k, n))

	k = 4
	n = 1
	print(combinationSum3(k, n))
	k = 3
	n = 2
	print(combinationSum3(k, n))
	k = 9
	n = 45
	print(combinationSum3(k, n))

	print("END OF TESTING...")

main()

