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

#Main function: 
def main():
	print("TESTING GRAY CODE...")
	n = 2
	print(grayCode(n))
	n = 1
	print(grayCode(n))

	print("END OF TESTING....")


main()
