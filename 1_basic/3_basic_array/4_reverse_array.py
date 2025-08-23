'''
Given an array arr of n elements. The task is to reverse the given array. The reversal of array should be inplace.

Examples:
    1.  Input: n=5, arr = [1,2,3,4,5]
        Output: [5,4,3,2,1]

        Explanation: The reverse of the array [1,2,3,4,5] is [5,4,3,2,1]

    2.  Input: n=6, arr = [1,2,1,1,5,1]
        Output: [1,5,1,1,2,1]

        Explanation: The reverse of the array [1,2,1,1,5,1] is [1,5,1,1,2,1].
'''






class Solution:
    # Time Complexity - O(2n)   Space Complexity - O(n)
    def reverse_brute(self, arr, n):

        new_arr = []

        for i in range(n-1, -1, -1):
            new_arr.append(arr[i])

        for j in range(n):
            arr[j] = new_arr[j]

    # Time Complexity - O(n//2)  Space Complexity - O(1)
    def reverse_optimal(self, arr, n):

        i = 0
        j = n-1

        while i < j:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

            i += 1
            j -= 1

    # Time Complexity - O(n//2)  Space Complexity - O(1)
    # Pythonic way of swapping        
    def reverse_pythonic(self, arr, n):
        for i in range(n//2):
            arr[i], arr[n-i-1] = arr[n-i-1], arr[i]




print("Using Brute Force")
arr1 = [1,2,3,4,5]
Solution().reverse_brute(arr1, 5)
print(arr1)

arr2 = [1,2,1,1,5,1]
Solution().reverse_brute(arr2, 6)
print(arr2)


print("Using Optimal")
arr1 = [1,2,3,4,5]
Solution().reverse_optimal(arr1, 5)
print(arr1)

arr2 = [1,2,1,1,5,1]
Solution().reverse_optimal(arr2, 6)
print(arr2)


print("Using Pythonic")
arr1 = [1,2,3,4,5]
Solution().reverse_pythonic(arr1, 5)
print(arr1)

arr2 = [1,2,1,1,5,1]
Solution().reverse_pythonic(arr2, 6)
print(arr2)
