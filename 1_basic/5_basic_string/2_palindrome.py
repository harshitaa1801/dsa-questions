'''
You are given a string s. Return true if the string is palindrome, otherwise false. A string is called palindrome if it reads the same forward and backward.

Examples:
    1.  Input : s = "hannah"
        Output : true

        Explanation : The given string when read backward is -> "hannah", which is same as when read forward.
        Hence answer is true.

    2.  Input : s = "aabbaaa"
        Output : false

        Explanation : The given string when read backward is -> "aaabbaa", which is not same as when read forward.
        Hence answer is false.
'''


class Solution:    
    def palindromeCheckBrute(self, s):

        #brute force - create reversed string, match with original string

        s2=''

        for i in range(len(s)-1, -1, -1):
            s2 += (s[i])

        for j in range(len(s)):
            if s[j] != s2[j]:
                return False
        return True



    def palindromeCheckOptimal(self, s):
        # optimal - start while loop, check for s,e index, after loop - s++, e--

        start = 0
        end = len(s)-1

        while start<end:
            if s[start]!=s[end]:
                return False
            start += 1
            end -= 1

        return True


# Testing the code
print("Brute Force")
print(Solution().palindromeCheckBrute("hannah"))    # Output: True
print(Solution().palindromeCheckBrute("aabbaaa"))   # Output: False
print(Solution().palindromeCheckBrute("a"))         # Output: True
print(Solution().palindromeCheckBrute(""))          # Output: True
print(Solution().palindromeCheckBrute("ab"))        # Output: False
print(Solution().palindromeCheckBrute("aa"))        # Output: True
print()
print("Optimal")
print(Solution().palindromeCheckOptimal("hannah"))   # Output: True
print(Solution().palindromeCheckOptimal("aabbaaa"))  # Output: False
print(Solution().palindromeCheckOptimal("a"))        # Output: True
print(Solution().palindromeCheckOptimal(""))         # Output: True 
print(Solution().palindromeCheckOptimal("ab"))       # Output: False
print(Solution().palindromeCheckOptimal("aa"))       # Output: True