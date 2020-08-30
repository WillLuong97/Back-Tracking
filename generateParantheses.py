# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# For example, given n = 3, a solution set is:
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]
#first approach - Brute Force
def generateParenthesis(n):
    def generate(A = []):
        # print(A)
        if len(A) == 2*n:
            if valid(A):
                ans.append("".join(A))
        else:
            A.append('(')
            generate(A)
            A.pop()
            A.append(')')
            generate(A)
            A.pop()

    def valid(A):
        bal = 0
        for c in A:
            if c == '(': bal += 1
            else: bal -= 1
            if bal < 0: return False
        return bal == 0

    ans = []
    generate()
    return ans


#second approach - using back tracking: 
def generateParenthesis_BackTracking(n):
    retStr = []
    
    #back tracking 
    def backTracking(parenString = "", opening_bracket_index = 0 , closing_bracket_index = 0):
        #if the parentheses string finally reaches number of parentheses pairs: 
        if(len(parenString) == 2 * n):
            retStr.append(parenString)
        
        #add a opening parentheses to the string parenthese string: 
        if opening_bracket_index < n:
            backTracking(parenString + '(', opening_bracket_index + 1, closing_bracket_index)
        #add a closing parenthese to string
        if closing_bracket_index < opening_bracket_index:
            backTracking(parenString + ')', opening_bracket_index, closing_bracket_index + 1)
    backTracking()

    return retStr

def main():
    print(generateParenthesis(2))
    print("")
    print(generateParenthesis_BackTracking(2))


    pass
main()

