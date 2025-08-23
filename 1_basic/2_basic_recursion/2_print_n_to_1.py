'''

    Given an integer n, write a function to print all numbers from n to 1 (inclusive) using recursion.

    You must not use any loops such as for, while, or do-while.
    The function should print each number on a separate line, in decreasing order from n to 1

    Examples:
        1.  Input: 5
            Output:

                5
                4
                3
                2
                1

        2.  Input: 1
            Output:

                1
'''

class Solution:
    def printNumbers(self, n):
        # Your code goes here

        if n==0:
            return
        print("n = ", n)
        self.printNumbers(n-1)


    

print("Output for n=5")
Solution().printNumbers(5)  # Output: 1 2 3 4 5

print("Output for n=1")
Solution().printNumbers(1)  # Output: 1

print("Output for n=10")
Solution().printNumbers(10)  # Output: 1 2 3 4 5 6 7 8 9 10

print("Output for n=0")
Solution().printNumbers(0)  # Output: (no output, as there are no numbers to print)
