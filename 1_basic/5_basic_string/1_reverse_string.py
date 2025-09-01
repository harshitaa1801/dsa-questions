'''
Given a string, the task is to reverse it. The string is represented by an array of characters s. Perform the reversal in place with O(1) extra memory.

Note: no need to return anything, modify the given list.


Examples:
    1.  Input : s = ["h", "e" ,"l" ,"l" ,"o"]
        Output : ["o", "l", "l", "e", "h"]

        Explanation : The given string is s = "hello" and after reversing it becomes s = "olleh".

    2.  Input : s = ["b", "y" ,"e" ]
        Output : ["e", "y", "b"]

        Explanation : The given string is s = "bye" and after reversing it becomes s = "eyb".

'''


class Solution: 

    def reverseStringBrute(self, s):
        '''
        LIFO - Last In First Out
        Using Stack Data Structure

        Time Complexity - O(2n)
        Space Complexity - O(n)
        '''

        stack = []

        for i in range(len(s)-1, -1, -1):
            stack.append(s[i])

        for j in range(len(s)):
            s[j] = stack.pop()



    def reverseStringOptimal(self, s):
        start = 0
        end = len(s)-1

        while start<end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1


# Testing the code
arr1 = ["h", "e" ,"l" ,"l" ,"o"]
Solution().reverseStringBrute(arr1)
print(arr1)  # Output: ["o", "l", "l", "e", "h"]
print() 

arr2 = ["b", "y" ,"e" ]
Solution().reverseStringOptimal(arr2)
print(arr2)  # Output: ["e", "y", "b"]
print()

arr3 = ["a"]
Solution().reverseStringOptimal(arr3)
print(arr3)  # Output: ["a"]
print()

arr4 = ["a", "b"]
Solution().reverseStringOptimal(arr4)
print(arr4)  # Output: ["b", "a"]
print()

arr5 = ["a", "b", "c"]
Solution().reverseStringOptimal(arr5)
print(arr5)  # Output: ["c", "b", "a"]
print() 

arr6 = ["a", "b", "c", "d"]
Solution().reverseStringOptimal(arr6)
print(arr6)  # Output: ["d", "c", "b", "a"]
print()
