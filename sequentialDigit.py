#Problem 1291. Sequential Digits

'''
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

 

Example 1:

Input: low = 100, high = 300
Output: [123,234]
Example 2:

Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]
 

Constraints:

10 <= low <= high <= 10^9
'''
#We will construct each number by looping through the range 1-9, at each number, check to see if they are within the boundary or not,
#if not, we skip it
def sequentialDigits(low, high):
	#base case: 
	if not low and not high:
		return []
	result = []
	current_number = 0
	#Loop through 1-9 inclusive to construct the senquential digit
	#the outer loop, will be used to construct the 1st digit and the inner loop would be used to grow the rest of the number based on the first digit
	for i in range(1, 10):
		current_number = i
		for j in range(i+1, 10):
			current_number = current_number * 10 + j
			#append the number into the result list, if the current number is within the boundary
			if low <= current_number <= high: 
				result.append(current_number)
	return sorted(result)

	
#Main function to run the test cases: 
def main():
	print("TESTING SEQUENTIAL DIGITS...")
	low_1 = 100
	high_1 = 300
	low_2 = 1000
	high_2 = 13000
	print(sequentialDigits(low_1, high_1))
	print(sequentialDigits(low_2, high_2))	
	print("END OF TESTING...")


main()
