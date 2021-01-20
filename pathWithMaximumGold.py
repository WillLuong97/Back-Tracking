# 1219. Path with Maximum Gold

'''
In a gold mine grid of size m * n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:

Every time you are located in a cell you will collect all the gold in that cell.
From your position you can walk one step to the left, right, up or down.
You can't visit the same cell more than once.
Never visit a cell with 0 gold.
You can start and stop collecting gold from any position in the grid that has some gold.
Example 1:

Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
Output: 24
Explanation:
[[0,6,0],
 [5,8,7],
 [0,9,0]]
Path to get the maximum gold, 9 -> 8 -> 7.
Example 2:

Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
Output: 28
Explanation:
[[1,0,7],
 [2,0,6],
 [3,4,5],
 [0,3,0],
 [9,0,20]]
Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.
 

Constraints:

1 <= grid.length, grid[i].length <= 15
0 <= grid[i][j] <= 100
There are at most 25 cells containing gold.
'''
from collections import deque
def getMaximumGold(grid):
	#base case: 
	if not grid: 
		return None
	#result array to store all the sum of each paths 
	sumArray = []
	#valid moves to init a path
	dx = [-1, 1, 0, 0]
	dy = [0, 0, 1, -1]
	greatest = 0
	#helper method to perform bfs on each node
	def bfs(i,j):
		#visited array to check if the current node has been visited or not and this
		#array is restarted every time we look at a new node element altogether
		visited = [[False for i  in range(len(grid[0]))] for j in range(len(grid))]
		queue = deque([])
		queue.append(((i,j), grid[i][j]))
		tmpMax = 0
		while queue:
			queueSize = len(queue)
			#looping through each level of the queue
			#for level in range(queueSize):
			current, curr_total = queue.popleft()
			x = current[0]
			y = current[1]
			visited[x][y] = True
			tmpMax = max(tmpMax, curr_total)
			#getting the valid moves to get to the next element
			for i in range(len(dx)): 
				new_x = x + dx[i]
				new_y = y + dy[i]
				if(checkValidNeighbors(new_x, new_y, grid) and not visited[new_x][new_y]):
					queue.append(((new_x, new_y), curr_total + grid[new_x][new_y]))
		sumArray.append(tmpMax)
		#loop through the matrix to run the bfs on it
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] != 0:
				bfs(i, j)
	return max(sumArray)
	
#helper method to check if a position is good to go or not
def checkValidNeighbors(x, y, grid):
	if 0 <= x <len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != 0:
		return True

	return False


#main function to run the program: 
def main():
	print("TESTING PATH WITH MAXIMUM GOLD...")
	#Test cases: 
	grid_1 = [[0,6,0],[5,8,7],[0,9,0]]
	grid_2 =  [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
	
	print(getMaximumGold(grid_1))
	print(getMaximumGold(grid_2))

	print("END OF TESTING...")


main()
