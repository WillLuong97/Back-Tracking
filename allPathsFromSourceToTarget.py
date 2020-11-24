#Leetcode 797: All Paths From Source to Target


'''
Problem statment: 
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1, and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).
Example 1:

Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
Example 2:


Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
Example 3:

Input: graph = [[1],[]]
Output: [[0,1]]
Example 4:

Input: graph = [[1,2,3],[2],[3],[]]
Output: [[0,1,2,3],[0,2,3],[0,3]]
Example 5:

Input: graph = [[1,3],[2],[3],[]]
Output: [[0,1,2,3],[0,3]]
 

Constraints:

n == graph.length
2 <= n <= 15
0 <= graph[i][j] < n
graph[i][j] != i (i.e., there will be no self-loops).
The input graph is guaranteed to be a DAG.

'''
#function to solve the problem: 
def allPathsSourceTarget(graph):
    #base case: 
    if not graph: 
        return None
    #visited array to check all element that has been visitied
    visited = [None] * len(graph)
    #helper method to run dfs on the nodes of the graph
    def dfs(startNodePosition, graph):
        #base case: 
        if startNodePosition == len(graph) - 1: 
            return [[startNodePosition]]
        if visited[startNodePosition]:
            return visited[startNodePosition]
            
        result = []
        #looping through the neighbor nodes of the current starting node
        for neighbor in graph[startNodePosition]:
            array = dfs(neighbor, graph)
            #if the array has element: 
            if not array:
                continue

            else: 
                #append all the path that leads to the final points in the array
                for nodePath in array:
                    result.append([startNodePosition] + nodePath)
        return result
    return dfs(0, graph)


#main function to run the program
def main():
    print("TESTING ALL PATHS FROM SOURCE TO TARGET...")
    graph_01 = [[1,2],[3],[3],[]]
    graph_02 = [[4,3,1],[3,2,4],[3],[4],[]]
    graph_03 = [[1],[]]
    graph_04 = [[1,2,3],[2],[3],[]]
    graph_05 = [[1,3],[2],[3],[]]
    print(allPathsSourceTarget(graph_01))
    print(allPathsSourceTarget(graph_02))
    print(allPathsSourceTarget(graph_03))
    print(allPathsSourceTarget(graph_04))
    print(allPathsSourceTarget(graph_05))
    
    
    print("END OF TESTING...")
main()
