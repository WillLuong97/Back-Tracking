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



#main function to run the program 
def main():
  print("GENERATING PERMUTATION...")
  test_nums_1 = [1,2,3]
  test_nums_2 = [4,5,6,8]
  print(permute(test_nums_1))
  print(permute(test_nums_2))
  print("END OF TESTING....")
main()
