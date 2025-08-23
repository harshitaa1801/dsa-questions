'''
You are given an integer n. You need to return the number of digits in the number.
The number will have no leading zeroes, except when the number is 0 itself.


Examples:
Input: n = 4

Output: 1

Explanation: There is only 1 digit in 4.

Input: n = 14

Output: 2

Explanation: There are 2 digits in 14.

'''

def countDigit(n):
    digit_count = 0

    while n:
        r = n%10
        n = n//10
        digit_count += 1

    return digit_count



print(countDigit(4))  # Output: 1
print(countDigit(14))  # Output: 2
print(countDigit(12345))  # Output: 5
print(countDigit(100))  # Output: 3
print(countDigit(0))  # Output: 1
print(countDigit(999999))  # Output: 6
print(countDigit(1234567890))  # Output: 10
print(countDigit(1000000000))  # Output: 10
print(countDigit(7))  # Output: 1