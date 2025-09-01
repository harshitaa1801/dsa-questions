'''
    Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
    A shift on s consists of moving the leftmost character of s to the rightmost position.

    For example, if s = "abcde", then it will be "bcdea" after one shift.


    Examples:
        1.  Input : s = "abcde" , goal = "cdeab"
            Output : true

            Explanation : 
                After performing 2 shifts we can achieve the goal string from string s.
                After first shift the string s is => bcdea
                After second shift the string s is => cdeab.

        2.  Input : s = "abcde" , goal = "adeac"
            Output : false

            Explanation : 
                Any number of shift operations cannot convert string s to string goal.

'''

list
class Solution:    

    # Time Complexity : O(n^2)
    # Space Complexity : O(n)
    def rotateStringBrute(self, s, goal):

        if len(s)==0 and len(goal)==0:
            return True
        if len(s)!=len(goal):
            return False

        for rotation in range(len(s)):
            arr = ['']*len(s)
            temp = s[0]
            for i in range(len(s)-1):
                arr[i] = s[i+1]
            arr[-1] = temp

            is_rotated = True
            for j in range(len(s)):
                if arr[j]!=goal[j]:
                    is_rotated = False
            
            if is_rotated:
                return True
            else:
                new_s = ''
                for i in range(len(arr)):
                    new_s += arr[i]
                s = new_s

        return False
                
            


    def rotateStringBetter(self, s, goal):
        # Time Complexity : O(n^2)
        # Space Complexity : O(n*2)

        if len(s)==0 and len(goal)==0:
            return True

        if len(s)!=len(goal):
            return False

        # O(n) time
        for i in range(len(s)):
            # O(n) time
            rotated = s[i:] + s[:i]
                # O(n) space  O(n) space

            if rotated == goal:
                return True

        return False


    def rotateStringOptimal(self, s, goal):
        # Time Complexity : O(n) + O(2n)
        # Space Complexity : O(2n)

        if len(s)!=len(goal):
            return False

        # O(n) time
        # O(2n) space
        s2 = s+s

               # O(2n) time
        return goal in s2
            




        
print("Brute: ", Solution().rotateStringBrute("abcde", "cdeab"), " Better: ", Solution().rotateStringBetter("abcde", "cdeab"), " Optimal: ", Solution().rotateStringOptimal("abcde", "cdeab"))   # Output: True
print("Brute: ", Solution().rotateStringBrute("abcde", "adeac"), " Better: ", Solution().rotateStringBetter("abcde", "adeac"), " Optimal: ", Solution().rotateStringOptimal("abcde", "adeac"))   # Output: False
print("Brute: ", Solution().rotateStringBrute("abcde", "abced"), " Better: ", Solution().rotateStringBetter("abcde", "abced"), " Optimal: ", Solution().rotateStringOptimal("abcde", "abced"))   # Output: False
print("Brute: ", Solution().rotateStringBrute("abcde", "abcde"), " Better: ", Solution().rotateStringBetter("abcde", "abcde"), " Optimal: ", Solution().rotateStringOptimal("abcde", "abcde"))   # Output: True
print("Brute: ", Solution().rotateStringBrute("a", "a"), " Better: ", Solution().rotateStringBetter("a", "a"), " Optimal: ", Solution().rotateStringOptimal("a", "a"))   # Output: True
print("Brute: ", Solution().rotateStringBrute("a", "b"), " Better: ", Solution().rotateStringBetter("a", "b"), " Optimal: ", Solution().rotateStringOptimal("a", "b"))   # Output: False
print("Brute: ", Solution().rotateStringBrute("", ""), " Better: ", Solution().rotateStringBetter("", ""), " Optimal: ", Solution().rotateStringOptimal("", ""))   # Output: True
print("Brute: ", Solution().rotateStringBrute("aa", "aa"), " Better: ", Solution().rotateStringBetter("aa", "aa"), " Optimal: ", Solution().rotateStringOptimal("aa", "aa"))   # Output: True
print("Brute: ", Solution().rotateStringBrute("aa", "ab"), " Better: ", Solution().rotateStringBetter("aa", "ab"), " Optimal: ", Solution().rotateStringOptimal("aa", "ab"))   # Output: False
print("Brute: ", Solution().rotateStringBrute("aaaaa", "aaaaa"), " Better: ", Solution().rotateStringBetter("aaaaa", "aaaaa"), " Optimal: ", Solution().rotateStringOptimal("aaaaa", "aaaaa"))   # Output: True
print("Brute: ", Solution().rotateStringBrute("aaaaa", "aaaab"), " Better: ", Solution().rotateStringBetter("aaaaa", "aaaab"), " Optimal: ", Solution().rotateStringOptimal("aaaaa", "aaaab"))   # Output: False
print("Brute: ", Solution().rotateStringBrute("abc", "cab"), " Better: ", Solution().rotateStringBetter("abc", "cab"), " Optimal: ", Solution().rotateStringOptimal("abc", "cab"))   # Output: True
print("Brute: ", Solution().rotateStringBrute("abc", "cba"), " Better: ", Solution().rotateStringBetter("abc", "cba"), " Optimal: ", Solution().rotateStringOptimal("abc", "cba"))   # Output: False
print("Brute: ", Solution().rotateStringBrute("waterbottle", "erbottlewat"), " Better: ", Solution().rotateStringBetter("waterbottle", "erbottlewat"), " Optimal: ", Solution().rotateStringOptimal("waterbottle", "erbottlewat"))   # Output: True
print("Brute: ", Solution().rotateStringBrute("waterbottle", "bottlewater"), " Better: ", Solution().rotateStringBetter("waterbottle", "bottlewater"), " Optimal: ", Solution().rotateStringOptimal("waterbottle", "bottlewater"))   # Output: True