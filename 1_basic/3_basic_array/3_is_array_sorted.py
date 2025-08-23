'''
Given an array arr of size n, the task is to check if the given array is sorted in (ascending / Increasing / Non-decreasing) order. If the array is sorted then return True, else return False.

Examples:
    1.  Input: n = 5, arr = [1,2,3,4,5]
        Output: True

        Explanation: The given array is sorted i.e Every element in the array is smaller than or equals to its next values, So the answer is True.

    2.  Input: n = 5, arr = [5,4,6,7,8]
        Output: False

        Explanation: The given array is Not sorted i.e Every element in the array is not smaller than or equal to its next values, So the answer is False. Here element 5 is not smaller than or equal to its future elements.
'''

print("Time Complexity: O(n)  Space Complexity: O(1)")
class Solution:
    def arraySortedOrNot(self, arr, n):
        
        if n == 1:
            return True

        for i in range(n-1):
            if arr[i] <= arr[i+1]:
                continue
            else:
                return False
        
        return True
    

print(Solution().arraySortedOrNot([1,2,3,4,5], 5))
print(Solution().arraySortedOrNot([5,4,6,7,8], 5))
print(Solution().arraySortedOrNot([1,1,1,1,1], 5))
print(Solution().arraySortedOrNot([1,2,2,2,3], 5))
print(Solution().arraySortedOrNot([1], 1))
print(Solution().arraySortedOrNot([], 0))
print(Solution().arraySortedOrNot([1,3,2,4,5], 5))
print(Solution().arraySortedOrNot([10,20,30,40,50], 5))
print(Solution().arraySortedOrNot([1,2,3,5,4], 5))
print(Solution().arraySortedOrNot([1,2,3,4,5,6,7,8,9,10], 10))
print(Solution().arraySortedOrNot([1,2,3,4,5,7,6,9,10,11], 11))
print(Solution().arraySortedOrNot([1,2,3,4,5,6,7,8,9,10,11,12], 12))
print(Solution().arraySortedOrNot([1,2,3,4,5,6,7,8,9,10,11,12,13], 13))
print(Solution().arraySortedOrNot([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], 15))
