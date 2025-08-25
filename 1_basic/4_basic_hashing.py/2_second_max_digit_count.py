'''
Given an array of n integers, find the second most frequent element in it.

If there are multiple elements that appear second most frequent times, find the smallest of them.

If second most frequent element does not exist return -1.


Examples:
    1.  Input: arr = [1, 2, 2, 3, 3, 3]
        Output: 2

        Explanation:

            The number 2 appears the second most (2 times) and number 3 appears the most(3 times). 

    2.  Input: arr = [4, 4, 5, 5, 6, 7]
        Output: 6

        Explanation:

            Both 6 and 7 appear second most times, but 6 is smaller.


'''
class Solution:
    def secondMostFrequentElementBrute(self, nums):
        max_elem = -1
        second_max_elem = -1
        max_count = 0
        second_max_count = 0

        visited = [False]*len(nums)

        if len(nums) == 1:
            return -1
        for i in range(len(nums)):
            
            if visited[i]:
                continue
            elem = nums[i]
            elem_count = 0

            for j in range(i, len(nums)):
                if elem == nums[j]:
                    elem_count += 1
                    visited[j] = True
            
            if elem_count > max_count:
                second_max_elem = max_elem
                max_elem = elem
                second_max_count = max_count
                max_count = elem_count

            elif elem_count == max_count:                
                max_elem = min(elem, max_elem)
            elif elem_count > second_max_count:
                second_max_count = elem_count
                second_max_elem = elem

            elif elem_count == second_max_count:
                second_max_elem = min(elem, second_max_elem)
        return second_max_elem



    def secondMostFrequentElementOptimal(self, nums):

        second_max_elem = -1
        max_elem = -1
        max_freq=0
        second_max_freq=0
        mapping = {}

        for i in range(0, len(nums)):
            if nums[i] in mapping:
                mapping[nums[i]] +=1
            else:
                mapping[nums[i]] = 1

        
        for elem,freq in mapping.items():
            if freq > max_freq:
                second_max_elem = max_elem
                second_max_freq = max_freq
                max_freq = freq
                max_elem = elem

            elif freq == max_freq:
                if elem < max_elem:
                    max_elem = elem

            elif freq > second_max_freq:
                second_max_freq = freq
                second_max_elem = elem

            elif freq == second_max_freq:
                if elem < second_max_elem:
                    second_max_elem = elem

        return second_max_elem




print("Using Brute Force")
arr1 = [1,2,2,3,3,3]
print(Solution().secondMostFrequentElementBrute(arr1))    
arr2 = [4,4,5,5,6]
print(Solution().secondMostFrequentElementBrute(arr2))    
arr3 = [1,1,2,2,3,3]
print(Solution().secondMostFrequentElementBrute(arr3))    
arr4 = [1,1,1]
print(Solution().secondMostFrequentElementBrute(arr4))    
arr5 = [1,2,3,4,5]
print(Solution().secondMostFrequentElementBrute(arr5))    
arr6 = [5,5,5,5,5]
print(Solution().secondMostFrequentElementBrute(arr6))    
arr7 = [1]
print(Solution().secondMostFrequentElementBrute(arr7))    
arr8 = [1,2]
print(Solution().secondMostFrequentElementBrute(arr8))    
arr9 = [2,1]
print(Solution().secondMostFrequentElementBrute(arr9))    
arr10 = [1,2,2,3,3,3,4,4,4,4]
print(Solution().secondMostFrequentElementBrute(arr10))    
arr11 = [1,2,2,3,3,3,4,4,4,4,5,5,5,5]
print(Solution().secondMostFrequentElementBrute(arr11))    
arr12 = [1,2,2,3,3,4,4,4,4,5,5,5,5,6,6,6]
print(Solution().secondMostFrequentElementBrute(arr12))



print("Using Optimal")
arr1 = [1,2,2,3,3,3]
print(Solution().secondMostFrequentElementOptimal(arr1))    
arr2 = [4,4,5,5,6]
print(Solution().secondMostFrequentElementOptimal(arr2))    
arr3 = [1,1,2,2,3,3]
print(Solution().secondMostFrequentElementOptimal(arr3))    
arr4 = [1,1,1]
print(Solution().secondMostFrequentElementOptimal(arr4))    
arr5 = [1,2,3,4,5]
print(Solution().secondMostFrequentElementOptimal(arr5))    
arr6 = [5,5,5,5,5]
print(Solution().secondMostFrequentElementOptimal(arr6))    
arr7 = [1]
print(Solution().secondMostFrequentElementOptimal(arr7))    
arr8 = [1,2]
print(Solution().secondMostFrequentElementOptimal(arr8))    
arr9 = [2,1]
print(Solution().secondMostFrequentElementOptimal(arr9))    
arr10 = [1,2,2,3,3,3,4,4,4,4]
print(Solution().secondMostFrequentElementOptimal(arr10))    
arr11 = [1,2,2,3,3,3,4,4,4,4,5,5,5,5]
print(Solution().secondMostFrequentElementOptimal(arr11))    
arr12 = [1,2,2,3,3,4,4,4,4,5,5,5,5,6,6,6]
print(Solution().secondMostFrequentElementOptimal(arr12))