'''

Ref https://takeuforward.org/plus/dsa/beginner-problem/basic-strings/largest-odd-number-in-a-string

Given a string s, representing a large integer, the task is to return the largest-valued odd integer (as a string) that is a substring of the given string s.
The number returned should not have leading zero's. But the given input string may have leading zero. (If no odd number is found, then return empty string.)

Examples:
    1.  Input : s = "5347"
        Output : "5347"

        Explanation : 
            The odd numbers formed by given strings are --> 5, 3, 53, 347, 5347.
            So the largest among all the possible odd numbers for given string is 5347.

            
    2.  Input : s = "0214638"
        Output : "21463"
        
        Explanation : 
            The different odd numbers that can be formed by the given string are --> 1, 3, 21, 63, 463, 1463, 21463.
            We cannot include 021463 as the number contains leading zero.
            So largest odd number in given string is 21463.

'''

class Solution:  
    # Time Complexity - O(n**2) + O(number of substrings)
    # Space Complexity - O(number of substrings)
    def largeOddNumBrute(self, s):

        # brute force - create all substrings, return max substring

        substring_list = []

        # O(n**2)
        for i in range(len(s)):
            if s[i] == 0:
                continue

            for j in range(i+1, len(s)+1):                
                substring = s[i:j]
                substring_list.append(substring)

        # O(number of substrings)
        max_substring = 0
        for sub in substring_list:
            sub_int = int(sub)
            if sub_int%2==0:
                continue
            
            max_substring = max(max_substring, sub_int)
        
        if max_substring:
            return max_substring 
        else:
            return ''



    # Time Complexity - O(n**2)
    # Space Complexity - O(0)
    def largeOddNumBetter(self, s):

        max_substring = 0
        for i in range(len(s)):
            if s[i] == 0:
                continue

            for j in range(i+1, len(s)+1):                
                substring = s[i:j]                
                sub_int = int(substring)
                if sub_int%2==0:
                    continue
                
                max_substring = max(max_substring, sub_int)
        
        if max_substring:
            return max_substring 
        else:
            return ''




    def largeOddNumOptimal(self, s):

        ind = -1

        for i in range(len(s)-1, -1, -1):
            sub = s[i]
            sub_int = int(sub)

            if sub_int % 2 == 1:
                ind = i
                break

        j = 0
        while j<=ind and s[j] == '0':
            j+=1

        return s[j: ind+1]

print("Using Brute Force")
s1 = "5347"
print(Solution().largeOddNumBrute(s1))    
s2 = "0214638"
print(Solution().largeOddNumBrute(s2))    
s3 = "4206"
print(Solution().largeOddNumBrute(s3))
s4 = "0000"
print(Solution().largeOddNumBrute(s4))
s5 = "123456"
print(Solution().largeOddNumBrute(s5))    
s6 = "23540"
print(Solution().largeOddNumBrute(s6))    
s7 = "235046"
print(Solution().largeOddNumBrute(s7))
s8 = "000123450"
print(Solution().largeOddNumBrute(s8))    
s9 = "0000"
print(Solution().largeOddNumBrute(s9))    
s10 = "0"
print(Solution().largeOddNumBrute(s10))


print("Using Better")
s1 = "5347"
print(Solution().largeOddNumBetter(s1))    
s2 = "0214638"
print(Solution().largeOddNumBetter(s2))    
s3 = "4206"
print(Solution().largeOddNumBetter(s3))
s4 = "0000"
print(Solution().largeOddNumBetter(s4))
s5 = "123456"
print(Solution().largeOddNumBetter(s5))    
s6 = "23540"
print(Solution().largeOddNumBetter(s6))    
s7 = "235046"
print(Solution().largeOddNumBetter(s7))
s8 = "000123450"
print(Solution().largeOddNumBetter(s8))    
s9 = "0000"
print(Solution().largeOddNumBetter(s9))    
s10 = "0"
print(Solution().largeOddNumBetter(s10))


print("Using Optimal")
s1 = "5347"
print(Solution().largeOddNumOptimal(s1))    
s2 = "0214638"
print(Solution().largeOddNumOptimal(s2))    
s3 = "4206"
print(Solution().largeOddNumOptimal(s3))    
s4 = "0000"
print(Solution().largeOddNumOptimal(s4))
s5 = "123456"
print(Solution().largeOddNumOptimal(s5))    
s6 = "23540"
print(Solution().largeOddNumOptimal(s6))    
s7 = "235046"
print(Solution().largeOddNumOptimal(s7))
s8 = "000123450"
print(Solution().largeOddNumOptimal(s8))    
s9 = "0000"
print(Solution().largeOddNumOptimal(s9))    
s10 = "0"
print(Solution().largeOddNumOptimal(s10))