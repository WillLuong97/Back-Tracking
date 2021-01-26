#78. Subsets
'''
Given an integer array nums of unique elements, return all possible subsets (the power set).

Power set is all possible combinations of all possible lengths, from 0 to n.
The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
'''
#class Solution:
#	def __init__(self, numArray):
#		self.numArray = numArray

def subsets_CASCADING(nums):
	#base case:
	if not nums: 
		return [[]]

	result = [[]]
	
	#loop through the nums array and combine its value with the existing subsets currently in the array
	for num in nums:
		result += (curr + [num] for curr in result)
	return result
'''
Time complexity: O(n * 2^n) we have to generate all subsets of the numbers and then add them into the array 
Space complexity: O(n * 2^n) This is exactly the number of solutions for subsets multiplied by the number NN of elements to keep for each subset.
FAILED - TIME LIMIT EXCEEED...
'''	

'''
We define a backtrack function named backtrack(first, curr) which takes the index of first element to add and a current combination as arguments.

If the current combination is done, we add the combination to the final output.

Otherwise, we iterate over the indexes i from first to the length of the entire sequence n.

Add integer nums[i] into the current combination curr.

Proceed to add more integers into the combination : backtrack(i + 1, curr).

Backtrack by removing nums[i] from curr.

'''

def subsets_BACKTRACKING(nums):
	#base case:
	if not nums:
		return [[]]

	#helper method to backtrack to the previous element if the current combination 
	#has run out of spaces
	def backtrack(index, curr_comb):
		result.append(curr_comb[:])

		for j in range(index, N):
			curr_comb.append(nums[j])
			#backtrack to add the next element to the array if the current combonation has not been done
			backtrack(j+1, curr_comb)
			curr_comb.pop()			

	N = len(nums)
	result = []
	backtrack(0, [])

	return result
'''
Time complexity: O(n *2^n) generate all subsets and copy them into the output list
Space complexity: O(n* 2^n) to keep all the subsets of length N, since each of N elements could be present or absent.
'''





#main function to run the test cases: 
def main():
	print("TESTING SUBSETS...")
	#test cases: 
	nums_1 = [1,2,3]
	nums_2 = [0]
#	print(subsets_CASCADING(nums_1))
#	print(subsets_CASCADING(nums_2))
	print(subsets_BACKTRACKING(nums_1))
	print(subsets_BACKTRACKING(nums_2))
	print(subsets_BITMASKING(nums_1))
	print(subsets_BITMASKING(nums_2))


	print("END OF TESTING...")

main()
