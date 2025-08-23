'''
You are given an integer n. You need to check whether the number is a palindrome number or not. Return true if it's a palindrome number, otherwise return false.
A palindrome number is a number which reads the same both left to right and right to left.


Examples:
    1.  Input: n = 121
        Output: true
        Explanation: When read from left to right : 121.
        When read from right to left : 121.

    2.  Input: n = 123
        Output: false
        Explanation: When read from left to right : 123.
        When read from right to left : 321.
'''

def isPalindrome(n):
    
    ori_no = n
    rev_no = 0
    while n:
        r = n%10
        rev_no = (rev_no*10) + r
        n = n//10
    
    return rev_no == ori_no



print(isPalindrome(121))  # Output: True
print(isPalindrome(123))  # Output: False
print(isPalindrome(12321))  # Output: True
print(isPalindrome(45654))  # Output: True
print(isPalindrome(1001))  # Output: True
print(isPalindrome(0))  # Output: True
print(isPalindrome(10))  # Output: False