#Leetcode 1286. Iterator for Combination
'''
Design the CombinationIterator class

CombinationIterator(string characters, int combinationLength) Initializes the object with a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
next() Returns the next combination of length combinationLength in lexicographical order.
hasNext() Returns true if and only if there exists a next combination.
Example 1:

Input
["CombinationIterator", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[["abc", 2], [], [], [], [], [], []]
Output
[null, "ab", true, "ac", true, "bc", false]

Explanation
CombinationIterator itr = new CombinationIterator("abc", 2);
itr.next();    // return "ab"
itr.hasNext(); // return True
itr.next();    // return "ac"
itr.hasNext(); // return True
itr.next();    // return "bc"
itr.hasNext(); // return False

Constraints:

1 <= combinationLength <= characters.length <= 15
All the characters of characters are unique.
At most 104 calls will be made to next and hasNext.
It's guaranteed that all calls of the function next are valid.
'''
class CombinationIterator:
    #this init function will return the full list of all combination from the character string
    def __init__(self, characters: str, combinationLength: int):
        #create a list of all possible combinations sent in from the input
        self.combination = []
        #helper method to generate the combinations using backtracking
        def backtrack(character, index):
            #generating the character based on the combination length
            if len(character) == combinationLength:
                self.combination.append(character)
            elif len(character) < combinationLength:
                #look at the next character in the combination to generate the next combinations
                for nextChar in range(index+1, len(characters)):
                    backtrack(character + characters[nextChar], nextChar)

        for i in range(len(characters)):
            backtrack(characters[i], i)

    #return the next combination 
    def next(self) -> str:
        return self.combination.pop(0)
    
    #return true if there is more combination to find 
    def hasNext(self) -> bool:
        if self.combination:
            return True
        return False
'''
CombinationIterator itr = new CombinationIterator("abc", 2);
itr.next();    // return "ab"
itr.hasNext(); // return True
itr.next();    // return "ac"
itr.hasNext(); // return True
itr.next();    // return "bc"
itr.hasNext(); // return False
'''
#main function to run the test cases: 
def main():
    print("TESTING ITERATOR FOR COMBINATION...")
    itr = CombinationIterator("abc", 2)
    print(itr.next())
    print(itr.hasNext())
    print(itr.next())
    print(itr.hasNext())
    print(itr.next())
    print(itr.hasNext())
    print("END OF TESTING")
main()