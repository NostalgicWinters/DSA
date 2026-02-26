# Sliding Window is of two types:-
# 1) Variable Length
# 2) Fixed Length

# Common Case:- Array/String: Subarray, Substring

# Variable Length
## Longest Substring without repeating characters
### For checking if the string has repeating characters use a Set

class Solution:
    def LongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        sett = set()
        n = len(s)

        for r in range(n):
            while s[r] in sett:
                sett.remove(s[l])
                l += 1
            
            w = (r - l) + 1
            longest = max(longest, w)
            sett.add(s[r])
        
        return longest