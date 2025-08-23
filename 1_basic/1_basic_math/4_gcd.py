'''

You are given two integers n1 and n2. You need find the Greatest Common Divisor (GCD) of the two given numbers. Return the GCD of the two numbers.
The Greatest Common Divisor (GCD) of two integers is the largest positive integer that divides both of the integers.


Examples:
    1.  Input: n1 = 4, n2 = 6
        Output: 2
        Explanation: Divisors of n1 = 1, 2, 4, Divisors of n2 = 1, 2, 3, 6
        Greatest Common divisor = 2.

    2.  Input: n1 = 9, n2 = 8
        Output: 1
        Explanation: Divisors of n1 = 1, 3, 9 Divisors of n2 = 1, 2, 4, 8.
        Greatest Common divisor = 1.


'''


# BRUTE - TC - O(min(n1, n2))
def GCD(n1, n2):

    smaller = min(n1, n2)

    for i in range(smaller//2, 0, -1):
        if n1%i == 0 and n2%i==0:
            return i 

    return -1


# OPTIMAL - TC - O(log(min(n1, n2)))
def gcd(n1, n2):
    smaller = min(n1, n2)
    larger = max(n1, n2)

    if smaller == 0:
        return larger
    else:
        return gcd(smaller, larger%smaller)
    


print(gcd(4, 6))  # Output: 2
print(gcd(9, 8))  # Output: 1
print(gcd(48, 18))  # Output: 6
print(gcd(56, 98))  # Output: 14
print(gcd(101, 10))  # Output: 1
print(gcd(0, 5))  # Output: 5