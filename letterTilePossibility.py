#Problem 1079. Letter Tile Possibilities
'''
You have n  tiles, where each tile has one letter tiles[i] printed on it.

Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.

Example 1:

Input: tiles = "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
Example 2:

Input: tiles = "AAABBC"
Output: 188
Example 3:

Input: tiles = "V"
Output: 1

Constraints:

1 <= tiles.length <= 7
tiles consists of uppercase English letters.
'''
from itertools import permutations
def numTilePossibilities(tiles):
    #base case:
    if not tiles:
        return None
    perms = []
    for i in range(1, len(tiles)+1):
        perms += list(set(permutations(tiles, i)))
    return len(perms)


#Approach using backtracking: 
#The idea is to create a set to store all permutation created from the tiles string, and we call recursion for the next char in the array but
# backtrack if the same permutation have been created before. 
#Time complexity: O(n), where n is every character in the tile string
#Space complexity: O(n), the recursion stack would need to run until all char in the string has been processed.
def numTilePossibilities_BACKTRACKING(tiles):
    #base case:
    if not tiles:
        return None

    perms = set()
    stringList = []
    #helper method to backtrack the process:
    def backtrack(li, currStr, perms):
        if not li: 
            return
        
        for char in li: 
            newStr = currStr + char
            if newStr not in perms: 
                perms.add(newStr)
                l1 = li.copy()
                l1.remove(char)
                backtrack(l1, newStr, perms)
    
    #converting the string tiles into a list
    for i in tiles: 
        stringList.append(i)

    backtrack(stringList, "", perms)
    return len(perms)

#main function to run the test cases: 
def main():
    print("TESTING LETTER TILE POSSIBILITY...")
    tiles = input()
    # print(numTilePossibilities(tiles))
    print(numTilePossibilities_BACKTRACKING(tiles))
    print("END OF TESTING...")
main()