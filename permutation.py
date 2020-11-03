#problem 46. Permutations

#Problem statement:

'''
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

'''
#Backtracking and recursion: The idea is each number will take turn and become the non-swapping number in a permutation and we recursion would run through
# the rest of element to swap each of them with each other, once we have swap all the combination, we will backtrack out and pick the next element in the array to 
# become the non-swapping element 
def permute(nums):
  #base case: 
  if not nums:
    return []

  result = []

  #loop through the entire array to permute each element
  for index, num in enumerate(nums):
    #We will isolate the current element, as it is being placed as the non-moving element
    #We create a new list with everything from the left side and right side of the current element 
    new_nums = nums[:index] + nums[index+1:]
    #The search space will be reduced as each element has been permmute
    if len(new_nums) == 0:
      result.append([num])

    else:
      #loop through the new_nums and permute themselves as well
      for j in permute(new_nums):
        result.append([num] + j)
  return result


#Problem 47: Permutations II
'''
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10

'''
from collections import Counter
#function to provide the soltuion to the problem
def permuteUnique(nums):
  #base case:
  if not nums:  #no list, no return
    return None
  
  result = []

  #a helper method to dfs through the list of number and duplicates to generate the unique permutation
  def backtracking(vistied, numsFreq):
    #base case: 
    if len(vistied) == len(numsFreq):
      #make a deep copy of the permutation as we would backtrack and check on it 
      result.append(list(vistied))
      return

    #loop through the nums list 
    for num in numsFreq: 
      #the number currently has element to be processed
      if numsFreq[num] > 0:
        #add it into the visited array and processed it 
        vistied.append(num)
        numsFreq[num] -= 1

        #continue to explore 
        backtracking(vistied, numsFreq)

        #revert the choice for the next iteration
        vistied.pop()
        numsFreq[num] += 1

  backtracking([], Counter(nums))
  return result





#main function to run the program 
def main():
  print("GENERATING PERMUTATION...")
  test_nums_1 = [1,2,3]
  test_nums_2 = [4,5,6,8]
  print(permute(test_nums_1))
  print(permute(test_nums_2))

  print("TESTING PERMUTATION II...")
  test_nums_3 = [1,1,2]
  test_nums_4 = [1,2,3]
  print(permuteUnique(test_nums_3))
  print(permuteUnique(test_nums_4))
  print("END OF TESTING....")
main()
