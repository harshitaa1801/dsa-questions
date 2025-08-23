'''
    Given an integer n, write a function to print all numbers from 1 to n (inclusive) using recursion.

    You must not use any loops such as for, while, or do-while.
    The function should print each number on a separate line, in increasing order from 1 to n.

    Examples:
        1.  Input: n = 5
            Output:

                1  
                2  
                3 
                4  
                5

        2.  Input: n = 1
            Output:

                1

'''


class Solution:
    def printNumbers(self, n):
        # Your code goes here

        if n == 0:
            return

        self.printNumbers(n-1)
        print(n)

print("Output for n=5")
Solution().printNumbers(5)  # Output: 1 2 3 4 5

print("Output for n=1")
Solution().printNumbers(1)  # Output: 1

print("Output for n=10")
Solution().printNumbers(10)  # Output: 1 2 3 4 5 6 7 8 9 10

print("Output for n=0")
Solution().printNumbers(0)  # Output: (no output, as there are no numbers to print)
