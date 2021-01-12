#Problem 784. Letter Case Permutation

'''
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. You can return the output in any order.

 

Example 1:

Input: S = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
Example 2:

Input: S = "3z4"
Output: ["3z4","3Z4"]
Example 3:

Input: S = "12345"
Output: ["12345"]
Example 4:

Input: S = "0"
Output: ["0"]
 

Constraints:

S will be a string with length between 1 and 12.
S will consist only of letters or digits.
'''
def letterCasePermutation(S):
	#storing the status of each character
	S = S.lower()
	result = []
	result.append(S)

	for i in range(len(S)):
		if S[i].isalpha():
			for j in range(len(result)):
				temp = result[j][:i] + S[i].upper() + result[j][i+1:]
				result.append(temp)
	return result






#Main function to run the test cases: 
def main():
	print("TESTING LETTER CASE PERMUTATION...")
	S_1 = "a1b2"
	S_2 = "3z4"
	S_3 = "12345"
	S_4 = "0"

	print(letterCasePermutation(S_1))
	print(letterCasePermutation(S_2))
	print(letterCasePermutation(S_3))
	print(letterCasePermutation(S_4))
	

	print(parser(S_1))
	print("END OF TESTING...")
	
main()
