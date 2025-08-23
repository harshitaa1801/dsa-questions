'''
Given an array of n elements. The task is to return the count of the number of odd numbers in the array.

Examples:
        1.  Input: n=5, array = [1,2,3,4,5]
            Output: 3

            Explanation: The three odd elements are (1,3,5).

        2.  Input: n=6, array = [1,2,1,1,5,1]
            Output: 5

            Explanation: The five odd elements are one 5 and four 1's.
'''



class Solution:
    def countOdd(self, arr, n):
        # Your code goes here
        
        count_odd = 0
        for i in range(n):
            if arr[i]%2==1:
                count_odd += 1
        return count_odd


print(Solution().countOdd([1,2,3,4,5], 5))
print(Solution().countOdd([1,2,1,1,5,1], 6))
print(Solution().countOdd([2,4,6,8], 4))
print(Solution().countOdd([1,3,5,7], 4))
print(Solution().countOdd([], 0))