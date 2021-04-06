#Problem 89. Gray Code

'''
The gray code is a binary numeral system where two successive values differ in only one bit.

Given an integer n representing the total number of bits in the code, return any sequence of gray code.

A gray code sequence must begin with 0.

 

Example 1:

Input: n = 2
Output: [0,1,3,2]
Explanation:
00 - 0
01 - 1
11 - 3
10 - 2
[0,2,3,1] is also a valid gray code sequence.
00 - 0
10 - 2
11 - 3
01 - 1
Example 2:

Input: n = 1
Output: [0,1]
 

Constraints:
1 <= n <= 16

Approach:  Bit manipulation, we will generate the search space based on n and as we generate the binary number, we will 
use the bitwise operator in python to make sure that any two successive values must only be different by 1
'''
def grayCode(n):
	#generating the search space
	search_space = 2 ** n
	result = []
	for i in range(search_space):
		result.append(i^(i >> 1))
	return result

#We will use DFS to generate each  binary sequence from the search space and then parse them together
def grayCode_DFS(n):
	#base case: 
	if n == 1:
		return [0,1]
	if n == 0:
		return [0]
	result = []	
	prevBinaryNumber = '0' * n
	
	visited = set()
	sequence = [prevBinaryNumber]
	
	while sequence:
		binaryNumber = sequence.pop()
		if binaryNumber not in visited:
			result.append(int(binaryNumber,2))
			visited.add(binaryNumber)
		#stop if we have maxed out all possible n-length binary sequence number
		if len(visited) == 2**n:
			break
		
		#loop through each binary number generated and move 1 bit
		for i in range(n):
			newCh = "0" if binaryNumber[i] == "1" else "1"
			newBinaryNumber = binaryNumber[:i] + newCh + binaryNumber[i+1:]

			if newBinaryNumber not in visited:
				sequence.append(newBinaryNumber)	
	return result

#Main function: 
def main():
	print("TESTING GRAY CODE...")
	n = 2
	print(grayCode(n))
	n = 1
	print(grayCode(n))

	n = 2
	print(grayCode_DFS(n))
	n = 1
	print(grayCode_DFS(n))
	print("END OF TESTING....")


main()
