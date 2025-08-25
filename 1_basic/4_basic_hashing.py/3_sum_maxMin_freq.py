'''
Given an array of n integers, find the sum of the frequencies of the highest occurring number and lowest occurring number.


Examples:
    1.  Input: arr = [1, 2, 2, 3, 3, 3]
        Output: 4

        Explanation: The highest frequency is 3 (element 3), and the lowest frequency is 1 (element 1). Their sum is 3 + 1 = 4.

    2.  Input: arr = [4, 4, 5, 5, 6]
        Output: 3

        Explanation: The highest frequency is 2 (elements 4 and 5), and the lowest frequency is 1 (element 6). Their sum is 2 + 1 = 3.

'''


class Solution:
    def sumHighestAndLowestFrequencyBrute(self, nums):
        max_count = 0
        min_count = len(nums) + 1

        visited = [False]*len(nums)

        for i in range(len(nums)):
            elem_count = 0
            if visited[i]:
                continue

            for j in range(i, len(nums)):
                if nums[i] == nums[j]:
                    elem_count += 1
                    visited[j] = True
            
            max_count = max(max_count, elem_count)
            min_count = min(min_count, elem_count)


        return max_count + min_count
    


    def sumHighestAndLowestFrequencyOptimal(self, nums):
        mapping = {}

        for i in range(len(nums)):
            if nums[i] in mapping.keys():
                mapping[nums[i]] += 1
            else:
                mapping.update({nums[i]:1})

        max_count = 0
        min_count = len(nums) + 1

        for elem, ecount in mapping.items():

            max_count=max(ecount, max_count)
            min_count = min(ecount, min_count)

        return max_count + min_count




print("Using Brute Force")
arr1 = [1,2,2,3,3,3]
print(Solution().sumHighestAndLowestFrequencyBrute(arr1))    
arr2 = [4,4,5,5,6]
print(Solution().sumHighestAndLowestFrequencyBrute(arr2))    
arr3 = [1,1,2,2,3,3]
print(Solution().sumHighestAndLowestFrequencyBrute(arr3))   
print("Using Optimal")
arr1 = [1,2,2,3,3,3]
print(Solution().sumHighestAndLowestFrequencyOptimal(arr1))    
arr2 = [4,4,5,5,6]
print(Solution().sumHighestAndLowestFrequencyOptimal(arr2))    
arr3 = [1,1,2,2,3,3]
print(Solution().sumHighestAndLowestFrequencyOptimal(arr3))