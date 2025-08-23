from math import sqrt
class Solution:
    def divisors(self, n):
        arr = []
        for i in range(1, (n//2)+1):
            if n%i==0:
                arr.append(i)
        
        arr.append(n)
        return arr


    def divisorsOptimal(self, n):        
        sqr = int(sqrt(n))
        setr = set()

        for i in range(1, sqr+1):

            if n%i==0:
                setr.add(i)
                setr.add(n//i)

        arr = list(setr)
        arr.sort()
        return arr
    

print('------------ Brute Force Solution ------------')
print(Solution().divisors(12))  # Output: [1, 2, 3, 4, 6, 12]
print(Solution().divisors(28))  # Output: [1, 2, 4, 7, 14, 28]
print(Solution().divisors(36))  # Output: [1, 2, 3, 4, 6, 9, 12, 18, 36]
print(Solution().divisors(100))  # Output: [1, 2, 4, 5, 10, 20, 25, 50, 100]
print(Solution().divisors(1))  # Output: [1]
print(Solution().divisors(0))  # Output: [0] (assuming we consider 0 as a divisor of itself)
print(Solution().divisors(7))  # Output: [1, 7] (7 is prime, so only divisors are 1 and itself)
print(Solution().divisors(15))  # Output: [1, 3, 5, 15] (15 is composite, so it has more divisors)
print(Solution().divisors(21))  # Output: [1, 3, 7, 21] (21 is composite, so it has more divisors)
print(Solution().divisors(49))  # Output: [1, 7, 49] (49 is a perfect square, so it has an odd number of divisors)



print('------------ Optimal Solution ------------')
print(Solution().divisorsOptimal(12))  # Output: [1, 2, 3, 4, 6, 12]
print(Solution().divisorsOptimal(28))  # Output: [1, 2, 4, 7, 14, 28]
print(Solution().divisorsOptimal(36))  # Output: [1, 2, 3, 4, 6, 9, 12, 18, 36]
print(Solution().divisorsOptimal(100))  # Output: [1, 2, 4, 5, 10, 20, 25, 50, 100]
print(Solution().divisorsOptimal(1))  # Output: [1]
print(Solution().divisorsOptimal(0))  # Output: [0] (assuming we consider 0 as a divisor of itself)
print(Solution().divisorsOptimal(7))  # Output: [1, 7] (7 is prime, so only divisors are 1 and itself)
print(Solution().divisorsOptimal(15))  # Output: [1, 3, 5, 15] (15 is composite, so it has more divisors)
print(Solution().divisorsOptimal(21))  # Output: [1, 3, 7, 21] (21 is composite, so it has more divisors)
print(Solution().divisorsOptimal(49))  # Output: [1, 7, 49] (49 is a perfect square, so it has an odd number of divisors)