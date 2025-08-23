'''
Given an integer N, return the sum of first N natural numbers. Try to solve this using recursion.


Examples:
    1.  Input : N = 4
        Output : 10
        Explanation : first four natural numbers are 1, 2, 3, 4.
        Sum is 1 + 2 + 3 + 4 => 10.

    2.  Input : N = 2
        Output : 3
        Explanation : first two natural numbers are 1, 2.
        Sum is 1 + 2 => 3.

'''
class Solution:
    def NnumbersSum(self, N):
        #your code goes here       
        if N==0:
            return 0
        return N + self.NnumbersSum(N-1)

    
print("Output for N=4: ", Solution().NnumbersSum(4))  # Output: 10
print("Output for N=2: ", Solution().NnumbersSum(2))  # Output: 3
print("Output for N=1: ", Solution().NnumbersSum(1))  # Output: 1
print("Output for N=0: ", Solution().NnumbersSum(0))  # Output: 0 (if we consider sum of first 0 natural numbers as 0)
print("Output for N=5: ", Solution().NnumbersSum(5))  # Output: 15
print("Output for N=10: ", Solution().NnumbersSum(10))  # Output: 55