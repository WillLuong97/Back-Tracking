#Python implmenentation of the backtracking algorithm in Computer Science


#Example 1: The Knight Tour problem: 
# The knight is placed on the first block of an empty board and, moving according to the rules of chess, must visit each square exactly once.

#Naive approach: is to generate all tours one by one and check if the generated tours satisfies the constraints: 

#Backtracking approach: 
#If all squares are visited: print the solution

#Else: 
#1. Add one of the next moves to the solution vector and recursively check if this move leads to a solution. (A knight can make maximum eight moves. We choose one of the 8 moves in this step)
#2. If the move chosen in the above step doesn't lead to a solution then remove this move from the solution vector and try other alternative moves
#3. If none of the alternatives work then return the false (Returning fase will remove the previously added item in recursion and if false is returned by the initial call of recursion then "no solution exists")
##chessboard size
n = 8

def isSafe(x, y, board):
    '''
    A utility function to check if i, j are valid indexes for N*N chessboard
    '''
    if(x>=0 and y>=0 and x < n and y < n and board[x][y] == -1):
        return True

    return False

def printSolution(n, board):
    '''
        A utility function to print the chessboards matrix
    '''
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=' ')
        print()

def solveKT(n):
    '''
        This function solves the Knight Tour prblem using BackTracking.
        This function mainly uses solveKTUtil() to solve the problem. It returns 
        false if no complete tour is possible, otherwise, return true and prints the tour. 
    '''

    #Initialization of the board matrix: 
    board = [[-1 for i in range(n)]for i in range(n)]

    #move_x and move_y define the next move of the Knight
    #move_x is for the next value in the x coordinate
    #move_y is for the next value in the y coordinate
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    #Since the Knight is initially at the first block 
    board[0][0] = 0

    #Step counter for knight's position
    position = 1

    #Checking if the solution exist or not:
    if not solveKTUtil(n, board, 0, 0, move_x, move_y, position):
        print("Solution does not exist!")

    else:
        printSolution(n, board)

def solveKTUtil(n, board, curr_x, curr_y, move_x, move_y, position):
    '''
        A recursive utility function to solve Knight Tour problem
    '''

    if(position == n**2):
        return True

    #Try all next moves from the current coordinate x, y:
    for i in range(8):
        new_x = curr_x + move_x[i]
        new_y = curr_y + move_y[i]
        if(isSafe(new_x, new_y, board)):
            board[new_x][new_y] = position
            if(solveKTUtil(n, board, new_x, new_y, move_x, move_y, position+1)):
                return True

            #Backtracking: 
            board[new_x][new_y] = -1

    return False

# solveKT(n)



# Problem #2: N-queens problem: Given a chess board N x N cells, we need to place N queens in such a place that no queen is attacked at all 
#by any other queen. A queen can be attack horizontally, vertically, and diagonally. 
global N 
N = 4

#Helper method to draw out the board with queen being placed on it
def printBoardOut(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j])

#A utility function to check if a queen can 
# be placed on board[row][col]. Note that this 
# function is called when "col" queens are 
# already placed in columns from 0 to col - 1. 
# So we need to check only the left side of the attacking queens
def isSafe(board, row, col):

    #Check on this row on the left side
    for i in range(col):
        if(board[row][i] == 1):
            return False

    #check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    #Check lower diagonal on the left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

#helper method to solve the problem
def solveNQUtil(board, col):
    #base case: If all queens are placed then return true
    if col >= N:
        return True

    #Consider this column and try placing 
    #this queen in all rows one by one
    for i in range(N):

        if isSafe(board, i, col):
            #place this queen in the board[i][col]
            board[i][col] = 1

            #recur to place rest of the queens: 
            if solveNQUtil(board, col + 1) == True:
                return True

            #if placing queen in boards[i][col]
            # doesnt lead to a solution, then check queen in the 
            board[i][col] = 0

    #if the queen cannot be placed in any row
    # in this col then return false

    return False


def solveNQ():
    board = [[0,0,0,0],
             [0,0,0,0],
             [0,0,0,0],
             [0,0,0,0]]

    if solveNQUtil(board, 0) == False:
        print ("Solution does not exist")


    printBoardOut(board)

    return True

# solveNQ()

#Problem 3: Leetcode 79: Word Search
#Problem statement:
'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.

'''

#we will approach this problem with a dfs approach
def exist(board, word):
    # #base case: 
    # if not board: 
    #     return False

    # if not word: 
    #     return False
    #getting the dimension of the board
    m = len(board)
    n = len(board[0])

    if len(word) == 0 or m == 0 or n == 0:
        return False
    #create a visited arrat to keep track of the visited neighbors of a node
    visited = [[False for _ in range(n)] for _ in range(m)]

    #create a helper method to handle dfs alogrithm:
    def dfs(i, row , column):
        #base case: 
        if i == len(word):
            return True

        #confirm that the current node has been visited: 
        visited[row][column] = True

        #valid move that node can take to make the word
        moves = [(1,0),(0,1),(-1,0),(0,-1)]
        #begin the moves
        for move in moves:
            new_row = row + move[0]
            new_col = column + move[1]
            #skip the element that are out of bound: 
            validBound = 0 <= new_row < m and 0 <= new_col < n
            #if the moves are out of bound, and the neighbor is not in the word list and the current node has been visited
            if not validBound or not board[new_row][new_col] == word[i] or visited[new_row][new_col]:
                #Then skip it
                continue
            #recurse until all element are found
            if dfs(i+1, new_row, new_col):
                return True

        visited[row][column] = False
        return False

    #Loop through the array until the first word in the word list is found, then we will run the dfs to check the list generation
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == word[0] and dfs(1, i, j):
                return True
    return False


#driver code: 
test_board =[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

test_word = "ABCCED"
test_word_2 = "SEE"
test_word_3 = "ABCB"

print(exist(test_board, test_word))
print(exist(test_board, test_word_2))
print(exist(test_board, test_word_3))

#backtracking problem: #77. Combination
#Problem statement: 
'''
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

You may return the answer in any order.
Example 1:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
Example 2:

Input: n = 1, k = 1
Output: [[1]]
 

Constraints:

1 <= n <= 20
1 <= k <= n
'''
def combine(n, k):
    #base case: 
    if not n or not k: 
        return None
    
    res = []

    dfs([], 0, res, n, k)
    return res

#DFS method to construct the combination array from the list
def dfs(searchArray, index, result, n, k):
    #base case: 
    if len(searchArray) == k:
        result.append(searchArray)
        return 

    for i in range(index + 1, n +1):
        dfs(searchArray + [i], i, result, n, k)

    
#helper method to find the 



#driver code: 
num = 4
k = 2

# print(combine(num, k))

#Leetcode problem 40. Combination Sum II

#Problem statement: 

'''
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]

'''
#Approach DFS + BACKTRACKING
def combinationSum2(candidates, target): 
    #Base case: 
    if not candidates:
        return None

    if not target: 
        return [candidates]

    visited = set()

    #depth first search algorithm to find the sum
    def dfs(array, path):
        #base case: the current sum in the path or queue is greater than the target
        if sum(path) > target:
            return
        #if the current sum adds up to the target so we will store them as a list within the result queue
        if sum(path) == target and tuple(path) not in visited:
            result.append(tuple(path))
            visited.add(tuple(path))
        #Loop through the search space to find the sum of each element in the array recursively
        for i in range(len(array)):
            dfs(array[i+1:], path + [array[i]])
        

    #sort the candiate for optimal approach
    sortedArr = sorted(candidates)

    result=[]
    dfs(sortedArr, [])
    return result


def main():
    print("TESTING COMBINATION SUM 2...")
    test_candidate = [10,1,2,7,6,1,5]
    target01 = 8

    test_candidate_1 = [2,5,2,1,2]
    target = 5
    print(combinationSum2(test_candidate, target01))
    print(combinationSum2(test_candidate_1, target))

    print("END OF TESTING...")
main()