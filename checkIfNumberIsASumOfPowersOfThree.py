#Problem 1780. Check if Number is a Sum of Powers of Three

'''
Given an integer n, return true if it is possible to represent n as the sum of distinct powers of three. Otherwise, return false.

An integer y is a power of three if there exists an integer x such that y == 3x.
Example 1:

Input: n = 12
Output: true
Explanation: 12 = 31 + 32
Example 2:

Input: n = 91
Output: true
Explanation: 91 = 30 + 32 + 34
Example 3:

Input: n = 21
Output: false
 

Constraints:

1 <= n <= 10**7


3 ** 15 <= 10 ** 7


#Appraoch: create an array to store all precompute values of power of 3s from 3^1 to 3^15, as 10^7 is the limit of possible input. Then loop that array and check for any element that are smaller than n 
#store those elements into another array and start looping through the entire to find if n can be created from those sum 
'''
def checkPowersOfThree(n):
	#base case: 
	if not n:
		return False
	#creating an array to store all value of power of threes
	possible_power = []
	m = 1 
	for i in range(15):
		while m <= n:
			possible_power.append(m)
			m *= 3
	answer = [False] 
	#recursive method to loop through all the possible the value of three and check to see if 
	#n can be summed from there
	def check_power_of_three_values(num, start = 0):
		#base case: 
		#if num is lesser than 0, which means we cannot find any sum in the power of three values 
		#to make up n, just back track and look for other cases
		if num < 0:
			return

		#if num is 0, the we have found the sum
		if num == 0:
			answer[0] = True
			return

		#loop through the list of power values to check for the ability of sum
		for i in range(start, len(possible_power)):
			curr = possible_power[start]
			start += 1
			check_power_of_three_values(num - curr, start)
	
	check_power_of_three_values(n)
	return answer[0]
			



#Main function to run the test cases: 
def main():
	print("TESTING CHECK IF NUMBER IS A SUM OF POWER OF THREE...")
	n = 12
	print(checkPowersOfThree(n))
	n = 91
	print(checkPowersOfThree(n))
	n = 21
	print(checkPowersOfThree(n))
	print("END OF TESTING...")



main()
