class Solution:  
    # Brute force - Time Complexity - O(n*m) where n is number of strings and m is length of smallest string
    # Space Complexity - O(1)
    def longestCommonPrefix(self, st):

        if len(st) == 1:
            return st[0]

        first_ele = st[0]
        max_pref = ''

        for i in range(len(first_ele)):
            pref = first_ele[i]
            for elem in st:

                if len(elem) <= i:
                    return max_pref

                if elem[i] != pref:
                    return max_pref
                
            max_pref = max_pref + pref

        return max_pref            

    
    # Time Complexity - O(n log n) + O(m) where n is number of strings and m is length of smallest string
    # Space Complexity - O(1)
    def longestCommonPrefixOptimal(self, st):

        # O(n log n)
        st.sort()

        first_element = st[0]
        last_element = st[-1]
        max_pref = ''

        # O(m)
        for i in range(len(first_element)):
            if i >= len(last_element):
                return max_pref

            if first_element[i] == last_element[i]:
                max_pref = max_pref + first_element[i]

            else:
                return max_pref

        return max_pref


print(Solution().longestCommonPrefixOptimal(["flower","flow","flight"]))  # Output: "fl"
print(Solution().longestCommonPrefixOptimal(["dog","racecar","car"]))     # Output: ""
print(Solution().longestCommonPrefixOptimal(["a"]))                       # Output: "a" 
print(Solution().longestCommonPrefixOptimal(["ab", "a"]))                 # Output: "a"
print(Solution().longestCommonPrefixOptimal(["cir","car"]))                # Output: "c"
print(Solution().longestCommonPrefixOptimal(["aa","a"]))                # Output: "a"
print(Solution().longestCommonPrefixOptimal(["","b"]))                # Output: ""
print(Solution().longestCommonPrefixOptimal(["a","a","b"]))                # Output: ""
print(Solution().longestCommonPrefixOptimal(["a","a","a"]))                # Output: "a"
print(Solution().longestCommonPrefixOptimal(["abca","abc"]))                # Output: "abc"
print(Solution().longestCommonPrefixOptimal(["abca","abca","abc"]))                # Output: "abc"
print(Solution().longestCommonPrefixOptimal(["abca","abca","abca"]))                # Output: "abca"
print(Solution().longestCommonPrefixOptimal(["abca","abca","ab"]))                # Output: "ab"
print(Solution().longestCommonPrefixOptimal(["abca","abca","a"]))                # Output: "a"
print(Solution().longestCommonPrefixOptimal(["abca","abca","abca","ab"]))                # Output: "ab"
print(Solution().longestCommonPrefixOptimal(["abca","abca","abca","abca","abc"]))                # Output: "abc"
print(Solution().longestCommonPrefixOptimal(["abca","abca","abca","abca","abca","abca"]))                # Output: "abca"
print(Solution().longestCommonPrefixOptimal(["abca","abca","abca","abca","abca","ab"]))                # Output: "ab"



