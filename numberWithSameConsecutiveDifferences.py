#Problem 967. Numbers With Same Consecutive Differences
'''
Return all non-negative integers of length n such that the absolute difference between every two consecutive digits is k.

Note that every number in the answer must not have leading zeros. For example, 01 has one leading zero and is invalid.

You may return the answer in any order.
Example 1:

Input: n = 3, k = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.
Example 2:

Input: n = 2, k = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
Example 3:

Input: n = 2, k = 0
Output: [11,22,33,44,55,66,77,88,99]
Example 4:

Input: n = 2, k = 2
Output: [13,20,24,31,35,42,46,53,57,64,68,75,79,86,97]
Constraints:

2 <= n <= 9
0 <= k <= 9

As a base case, when N=0 i.e. no more remaining digits to complete, we could return the current num as the result.

Otherwise, there are still some remaining digits to be added to the current number, e.g. 13. There are two potential cases to explore, based on the last digit of the current number which we denote as tail_digit.

Adding the difference K to the last digit, i.e. tail_digit + K.

Deducting the difference K from the last digit, i.e. tail_digit - K.

If the result of either above case falls into the valid digit range (i.e. [0, 9][0,9]), we then continue the exploration by invoking the function itself.
'''
def numsSameConsecDiff(n, k):
	#result array to store all solution
	result = []
	if not n: 
		return []
	#base case: if the n is only 1 number , then there would be no k conditions	 
	if n == 1:
		return [i for i in range(10)]
	#helper method to use dfs to build a the solution
	def dfs(n, curr_num):
		#base case: if n == 0, then we have found the number, add it into the result array
		if n == 0:
			return result.append(curr_num)
		
		#otherwise, we will keep checking the solution by continuing to buld out the tree
		tail_digit = curr_num % 10
		next_picks = set([tail_digit + k, tail_digit - k])
		#loop through the available digits and repeat the process until the the solution have been found
		for next_pick in next_picks: 
			if 0 <= next_pick < 10:
				nextDigit = curr_num * 10 + next_pick
				dfs(n-1, nextDigit)
		


	#loop through the search space from 1 -> 9 to build the solution, we cannot have leading 0
	for i in range(1, 10):
		dfs(n-1 ,i)

	return list(result)
	



#Main function to run the test case: 
def main():
	print("TESTING NUMBER WITH SAME CONSECUTIVE DIFFERENCES....")
	n = 3
	k = 7
	print(numsSameConsecDiff(n, k))
	n = 2
	k = 1
	print(numsSameConsecDiff(n, k))
	n = 2
	k = 0
	print(numsSameConsecDiff(n, k))
	
	n = 2
	k = 2
	print(numsSameConsecDiff(n, k))
	print("END OF TESTING...")

main()
