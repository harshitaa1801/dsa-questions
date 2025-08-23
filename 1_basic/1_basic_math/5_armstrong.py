'''

You are given an integer n. You need to check whether it is an armstrong number or not. Return true if it is an armstrong number, otherwise return false.
An armstrong number is a number which is equal to the sum of the digits of the number, raised to the power of the number of digits.


Examples:
    1.  Input: n = 153
        Output: true
        Explanation: Number of digits : 3.

        13 + 53 + 33 = 1 + 125 + 27 = 153.

        Therefore, it is an Armstrong number.

    2.  Input: n = 12
        Output: false
        Explanation: Number of digits : 2.

        12 + 22 = 1 + 4 = 5.

        Therefore, it is not an Armstrong number.
'''

# using string conversion to check if a number is an Armstrong number
# space complexity : O(digits in n) - for storing the string
def isArmstrong_str(n):
    s_num = str(n)
    s_len = len(s_num)

    sum = 0

    for i in range(s_len):
        digit = int(s_num[i])
        sum += digit**s_len

    return sum == n

# using arithmetic operations to check if a number is an Armstrong number
# space complexity : O(1) - no extra space used
def isArmstrong(n):

    len_of_no = 0
    ori_no = n 

    while n:
        n = n//10
        len_of_no += 1

    num = ori_no
    sum = 0
    while ori_no:
        r = ori_no%10
        sum += r**len_of_no
        ori_no = ori_no//10

    return sum == num
        



print("------Method 1: Using String Conversion------")
print(isArmstrong_str(153))  # Output: True
print(isArmstrong_str(370))  # Output: True
print(isArmstrong_str(371))  # Output: True
print(isArmstrong_str(9474))  # Output: True
print(isArmstrong_str(123))  # Output: False
print(isArmstrong_str(0))  # Output: True
print(isArmstrong_str(1))  # Output: True
print(isArmstrong_str(2))  # Output: True
print(isArmstrong_str(10))  # Output: False
print(isArmstrong_str(100))  # Output: False
print(isArmstrong_str(407))  # Output: True
print(isArmstrong_str(1634))  # Output: True
print(isArmstrong_str(8208))  # Output: True
print(isArmstrong_str(9475))  # Output: False
print(isArmstrong_str(1000))  # Output: False
print(isArmstrong_str(371293))  # Output: False
print(isArmstrong_str(1000000))  # Output: False
print(isArmstrong_str(1000001))  # Output: False


print("------Method 2: Using Arithmetic Operations------")
print(isArmstrong(153))  # Output: True
print(isArmstrong(370))  # Output: True
print(isArmstrong(371))  # Output: True
print(isArmstrong(9474))  # Output: True
print(isArmstrong(123))  # Output: False
print(isArmstrong(0))  # Output: True
print(isArmstrong(1))  # Output: True
print(isArmstrong(2))  # Output: True
print(isArmstrong(10))  # Output: False
print(isArmstrong(100))  # Output: False
print(isArmstrong(407))  # Output: True
print(isArmstrong(1634))  # Output: True
print(isArmstrong(8208))  # Output: True
print(isArmstrong(9475))  # Output: False
print(isArmstrong(1000))  # Output: False
print(isArmstrong(371293))  # Output: False
print(isArmstrong(1000000))  # Output: False
print(isArmstrong(1000001))  # Output: False
print(isArmstrong(10000000))  # Output: False
print(isArmstrong(100000000))  # Output: False
