'''
Highest Occurring Element in an Array

Given an array nums of n integers, find the most frequent element in it i.e., the element that occurs the maximum number of times. If there are multiple elements that appear a maximum number of times, find the smallest of them.


Examples:
    1.  Input: nums = [1, 2, 2, 3, 3, 3]
        Output: 3

        Explanation: The number 3 appears the most (3 times). It is the most frequent element.

    2.  Input: nums = [4, 4, 5, 5, 6]
        Output: 4

        Explanation: Both 4 and 5 appear twice, but 4 is smaller. So, 4 is the most frequent element.

'''




class Solution:
    # Time Complexity - O(n^2)   Space Complexity - O(1)
    def mostFrequentElementBrute(self, nums):
        max_count = 0
        max_ele = 0
        for i in range(len(nums)):
            elem = nums[i]
            elem_count = 1
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    elem_count += 1
            
            if elem_count>max_count:
                max_ele = elem
                max_count = elem_count
            elif elem_count==max_count:
                if elem < max_ele:
                    max_ele = elem


        return max_ele

    # Time Complexity - O(n)+O(unique elements in array)   Space Complexity - O(unique elements in array)
    def mostFrequentElementOptimal(self, nums):
        mapping = {}

        for i in range(len(nums)):
            if nums[i] in mapping.keys():
                mapping[nums[i]] += 1
            else:
                mapping.update({nums[i]:1})

        max_ele = 0
        max_count = 0
        for elem, ecount in mapping.items():
            if ecount>max_count:
                max_count = ecount
                max_ele = elem
            elif ecount == max_count:
                if elem < max_ele:
                    max_count = ecount
                    max_ele = elem
            

        return max_ele



print("Using Brute Force")
arr1 = [1, 2, 2, 3, 3, 3]
print(Solution().mostFrequentElementBrute(arr1))    
arr2 = [4, 4, 5, 5, 6]
print(Solution().mostFrequentElementBrute(arr2))    
arr3 = [1,1,2,2,3,3]
print(Solution().mostFrequentElementBrute(arr3))    
arr4 = [1,2,3,4,5]
print(Solution().mostFrequentElementBrute(arr4))    
arr5 = [5,5,5,5,5]
print(Solution().mostFrequentElementBrute(arr5))


print("Using Optimal")
arr1 = [1, 2, 2, 3, 3, 3]
print(Solution().mostFrequentElementOptimal(arr1))    
arr2 = [4, 4, 5, 5, 6]
print(Solution().mostFrequentElementOptimal(arr2))    
arr3 = [1,1,2,2,3,3]
print(Solution().mostFrequentElementOptimal(arr3))    
arr4 = [1,2,3,4,5]
print(Solution().mostFrequentElementOptimal(arr4))    
arr5 = [5,5,5,5,5]
print(Solution().mostFrequentElementOptimal(arr5))