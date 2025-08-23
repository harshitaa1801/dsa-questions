'''
You are given an integer n. Return the integer formed by placing the digits of n in reverse order.


Examples:
    1.  Input: n = 25

        Output: 52

        Explanation: Reverse of 25 is 52.

    2.  Input: n = 123

        Output: 321

        Explanation: Reverse of 123 is 321.

'''

class Solution:
    def reverseNumber(self, n):
        
        rev_no = 0
        while n:
            r = n%10
            rev_no = (rev_no*10) + r
            n = n//10
        
        return rev_no



print(Solution().reverseNumber(25))  # Output: 52
print(Solution().reverseNumber(123))  # Output: 321
print(Solution().reverseNumber(1001))  # Output: 1001
print(Solution().reverseNumber(0))  # Output: 0
print(Solution().reverseNumber(456))  # Output: 654 
