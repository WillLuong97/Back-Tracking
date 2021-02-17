#Problem 526. Beautiful Arrangement
'''
Suppose you have n integers labeled 1 through n. A permutation of those n integers perm (1-indexed) is considered a beautiful arrangement if for every i (1 <= i <= n), either of the following is true:

perm[i] is divisible by i.
i is divisible by perm[i].
Given an integer n, return the number of the beautiful arrangements that you can construct.
Example 1:

Input: n = 2
Output: 2
Explanation: 
The first beautiful arrangement is [1,2]:
    - perm[1] = 1 is divisible by i = 1
    - perm[2] = 2 is divisible by i = 2
The second beautiful arrangement is [2,1]:
    - perm[1] = 2 is divisible by i = 1
    - i = 2 is divisible by perm[2] = 1
Example 2:

Input: n = 1
Output: 1
Constraints:

1 <= n <= 15
'''

'''
Backtracking approach:
The idea behind this approach is simple. We try to create all the permutations of numbers from 1 to N. We can fix one number at a particular position and check for the divisibility criteria of that number at the particular position. But, we need to keep a track of the numbers which have already been considered earlier so that they aren't reconsidered while generating the permutations. If the current number doesn't satisfy the divisibility criteria, we can leave all the permutations that can be generated with that number at the particular position. This helps to prune the search space of the permutations to a great extent. We do so by trying to place each of the numbers at each position.

We make use of a visited array of size NN. Here, visited[i]visited[i] refers to the i^{th}i 
th
  number being already placed/not placed in the array being formed till now(True indicates that the number has already been placed).

We make use of a calculate function, which puts all the numbers pending numbers from 1 to N(i.e. not placed till now in the array), indicated by a FalseFalse at the corresponding visited[i]visited[i] position, and tries to create all the permutations with those numbers starting from the pospos index onwards in the current array. While putting the pos^{th}pos 
th
  number, we check whether the i^{th}i 
th
  number satisfies the divisibility criteria on the go i.e. we continue forward with creating the permutations with the number ii at the pos^{th}pos 
th
  position only if the number ii and pospos satisfy the given criteria. Otherwise, we continue with putting the next numbers at the same position and keep on generating the permutations.
'''
def countArrangement(n):
	result = 0
	def backtrack(node, nums):
		if not nums:
			nonlocal result
			result += 1
		else:
			for num in nums:
				if num % node == 0 or node % num == 0:
					nums.remove(num)
					backtrack(node+1, nums)
					nums.add(num) 

	backtrack(1, set(range(1, n+1)))
	return result		
#Time complexity: O(k), k is the number of valid permutations
#Space complexity: O(n), the recursion stack will have to store  all n number to check for its conditions

#Main function to run the test cases:
def main():
	print("TESTING BEAUTIFUL ARRANGEMENT....")
	n = 2
	print(countArrangement(n))
	n = 1
	print(countArrangement(n))
	print("END OF TESTING...")

main()
