# Back Tracking 

## Definition

- Backtracking: is a technique for solving problem RECURSIVELY by trying to build a solution incrementally, once piece at a time, while removing those solutions that fails to satisfy the constraints of the problem at any point of time ((by time, here, is referred to the time elapsed till reaching any level of the search tree)). 

- In order words, the algorithm tries different solutions untl it finds a solution that "works". The problem that used backtracking can only be solved by trying every possible configuration and each configuration is tried at only once.

## Prerequsite

- To be able to work on Backtracking, you will need to be able to understand "Recursion". Recursion is when a function call itself, similar to the movie Inception. Leonardo had a dream, in that dream he had another dream, in that dream he had yet another dream, and that goes on. So it's like there is a function called , and we are just calling it in itself.

```
function dream(){
    dream()
}
```

- Recursion is good for solving problems which can be broken down into smaller problems of the same kinds. 
- Base case: Any recursive method must have a terminating condition. Terminating condition is one for which the answer is already known and we just need to return that. For example, for the factorial problem, we know that factorial(0) = 1, so when x is 0 we simply return 1, otherwise, we break into smaller problem. If we dont include a base case, the function keep calling itself, and ultimately will result in the stack over flow.
For example, the dream() function given above has no base case, so it will keep calling itself until return a runtime error. 

- So if we want to solve a problem using recursion, we have to make sure that: 
    + The problem can be broken down into smaller problems of the same type
    + Problem has some base case to end the recursion
    + Base case is reached before the stack size limits exceed. 

## Approach to Back Tracking:

- Recursion can break the given problem into smaller ones. However, sometimes the solution to the big problem A does not depend on the solution B and C. 
- Let's take a situation. Suppose you are standing in front of three tunnels, one of which is having a bag of gold at its end, but you don't know which one. So you'll try all three. First go in tunnel , if that is not the one, then come out of it, and go into tunnel , and again if that is not the one, come out of it and go into tunnel . So basically in backtracking we attempt solving a subproblem, and if we don't reach the desired solution, then undo whatever we did for solving that subproblem, and try solving another subproblem.


=> Whenever a problem requires many different decision key points, that is when we will use back tracking as a solution 

- 3 keys to backtracking: 
    + Choices      (Recursion Represents Decision)
    + Constraints on those choices (When do we stop a path?)
    + Goal gained from those choices (When you reach the base case)

## Example:

### The N queen problem

- Choice: What cells do we place the queen in? 

- Constaints: We cannot place the queen right next to another queen or below it or diagonally 

- Goals: To find the Nth placement of tree in the recursion 



