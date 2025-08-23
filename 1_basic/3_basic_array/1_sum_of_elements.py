'''
Given an array arr of size n, the task is to find the sum of all the elements in the array.


Examples:
        1.  Input: n=5, arr = [1,2,3,4,5]    
            Output: 15

            Explanation: Sum of all the elements is 1+2+3+4+5 = 15

        2.  Input: n=6, arr = [1,2,1,1,5,1]
            Output: 11
            
            Explanation: Sum of all the elements is 1+2+1+1+5+1 = 11

            
'''

# Using Iteration
class Solution:
    def sum(self,arr, n): 
        s = 0
        for i in arr:
            s += i 
        return s


# Using Recursion
    def rec_sum(self, arr, n, i=0):
        if n == 0:
            return 0

        if i == n:
            return 0
        
        return arr[i] + self.rec_sum(arr, n, i+1)

        

print("Using Iteration")
print(Solution().sum([1,2,3,4,5], 5))
print(Solution().sum([1,2,1,1,5,1], 6))

print("Using Recursion")
print(Solution().rec_sum([1,2,3,4,5], 5))
print(Solution().rec_sum([1,2,1,1,5,1], 6))