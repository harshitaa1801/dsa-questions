class Solution:
    def anagramStringsBrute(self, s, t):
        # Time Complexity : O(nlogn) + O(nlogn) (sorting both strings)
        # Space Complexity : O(n) + O(n) (sorted method uses extra space)
        
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)


    def anagramStringsOptimal(self, s, t):
        # Time Complexity : O(n) + O(n) + O(26)     ~    O(n)
        # Space Complexity : O(1)  (constant space for count array)
        count = [0]*27

        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1

        for i in range(len(t)):
            count[ord(t[i]) - ord('a')] -= 1

        for i in range(len(count)):
            if count[i] != 0:
                return False

        return True