#Problem 1239. Maximum Length of a Concatenated String with Unique Characters

'''
Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.

Return the maximum possible length of s.
Example 1:
Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
Maximum length is 4.
Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible solutions are "chaers" and "acters".
Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
 

Constraints:

1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] contains only lower case English letters.

arr = ["un","iq","ue"]

approach: 

recusive function to loop through the arr: (index, path)
index: the index from an array 
path contains all valid character that are unique from the array at each recursion. 
if len(path) == len(set(path)):
	retunr max(len(path)) 

else: call the same function recursively on the rest of the element in the array from index to len(array)


Time complexity: O(n), the recursive function will run through all element in the array. 
Space complexity: O(n), n is the number of all element in the array because the recursion stack will have to run through all element in the mentioned array. 
'''

def maxLength(arr): 
	MAX_LEN = 0
	#helper method to traverse the array recursively
	def traverse(index, path):
		nonlocal MAX_LEN
		#base case: if the current path is a unique path, then we will check to see if the current path 	
		#length is the maximum or not
		if len(path) == len(set(path)):
			MAX_LEN = max(len(path), MAX_LEN)
		
		else: 
			return
		for j in range(index, len(arr)):
			traverse(j, path + arr[j])

	traverse(0, "")
	return MAX_LEN
	
	



#Main function to run the test cases: 
def main():
	print("TESTING Maximum Length of a Concatenated String with Unique Characters...")
	#test cases: 
	arr = ["un","iq","ue"]
	print(maxLength(arr))

	arr = ["cha","r","act","ers"]
	print(maxLength(arr))

	arr = ["abcdefghijklmnopqrstuvwxyz"]
	print(maxLength(arr))
	print("END OF TESTING...")

main()
