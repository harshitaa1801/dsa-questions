from math import sqrt

# Brute Force Approach
# Time Complexity: O(n/2)
class Solution:
    def isPrime(self, n):

        if n == 1:
            return False

        if n == 2:
            return True

        for i in range(2, n//2+1):
            if n%i==0:
                return False

        return True


    # Optimal Solution
    # Time Complexity = O(sqrt(n))
    def isPrimeOptimal(self, n):

        if n == 1:
            return False

        if n == 2:
            return True

        sqr = int(sqrt(n))

        for i in range(2, sqr+1):
            if n%i==0:
                return False


        return True

print(Solution().isPrime(2))  # Output: True
print(Solution().isPrime(3))  # Output: True
print(Solution().isPrime(4))  # Output: False
print(Solution().isPrime(5))  # Output: True
print(Solution().isPrime(6))  # Output: False
print(Solution().isPrime(7))  # Output: True
print(Solution().isPrime(8))  # Output: False
print(Solution().isPrime(9))  # Output: False
print(Solution().isPrime(10))  # Output: False
print(Solution().isPrime(11))  # Output: True
print(Solution().isPrime(13))  # Output: True
print(Solution().isPrime(17))  # Output: True
print(Solution().isPrime(19))  # Output: True
print(Solution().isPrime(23))  # Output: True
print(Solution().isPrime(29))  # Output: True
print(Solution().isPrime(31))  # Output: True
print(Solution().isPrime(37))  # Output: True
print(Solution().isPrime(41))  # Output: True
print(Solution().isPrime(43))  # Output: True
print(Solution().isPrime(47))  # Output: True
print(Solution().isPrime(53))  # Output: True
print(Solution().isPrime(59))  # Output: True
print(Solution().isPrime(61))  # Output: True
print(Solution().isPrime(67))  # Output: True
print(Solution().isPrime(71))  # Output: True
print(Solution().isPrime(73))  # Output: True
print(Solution().isPrime(78))  # Output: False



print('--------------Optimal Solution-------------- ')
print(Solution().isPrimeOptimal(2))  # Output: True
print(Solution().isPrimeOptimal(3))  # Output: True
print(Solution().isPrimeOptimal(4))  # Output: False
print(Solution().isPrimeOptimal(5))  # Output: True
print(Solution().isPrimeOptimal(6))  # Output: False
print(Solution().isPrimeOptimal(7))  # Output: True
print(Solution().isPrimeOptimal(8))  # Output: False
print(Solution().isPrimeOptimal(9))  # Output: False
print(Solution().isPrimeOptimal(10))  # Output: False
print(Solution().isPrimeOptimal(11))  # Output: True
print(Solution().isPrimeOptimal(13))  # Output: True
print(Solution().isPrimeOptimal(17))  # Output: True
print(Solution().isPrimeOptimal(19))  # Output: True
print(Solution().isPrimeOptimal(23))  # Output: True
print(Solution().isPrimeOptimal(29))  # Output: True    
print(Solution().isPrimeOptimal(31))  # Output: True
print(Solution().isPrimeOptimal(37))  # Output: True
print(Solution().isPrimeOptimal(41))  # Output: True
print(Solution().isPrimeOptimal(43))  # Output: True
print(Solution().isPrimeOptimal(47))  # Output: True
print(Solution().isPrimeOptimal(53))  # Output: True
print(Solution().isPrimeOptimal(59))  # Output: True
print(Solution().isPrimeOptimal(61))  # Output: True