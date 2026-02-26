# Sliding Window is of two types:-
# 1) Variable Length
# 2) Fixed Length

# Common Case:- Array/String: Subarray, Substring

# Variable Length
## 3. Longest Substring without repeating characters
### For checking if the string has repeating characters use a Set
from typing import List


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
    
# Fixed Length
## 643. Maximum average Subarray 1
    def MaxAvg(self, nums: List[int], k: int) -> float:
        
        cur_sum = 0
        n = len(nums)

        for i in range(k):
            cur_sum += nums[i]

        max_avg = cur_sum / k

        for i in range(k, n):
            cur_sum += nums[i]
            cur_sum -= nums[i-k]

            cur_avg = cur_sum/k

            max_avg = max(cur_avg, max_avg)
        
        return max_avg