from typing import List

#Contains Duplicate
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if(len(nums)==0 or len(nums)==1):
            return False
        a = set(nums)
        if(len(a)==len(nums)):
            return False
        else:
            return True

    #Valid Anagram
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        hashs = sorted(s)
        hasht = sorted(t)
        if hashs == hasht:
            return True
        return False

    #Two Sum
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        res = []
        for n in range(len(nums)):
            hash[nums[n]] = n
        for n in range(len(nums)):
            diff = target - nums[n]
            if (diff in hash and hash[diff]!=n):
                res.append(n)
                res.append(hash[target-nums[n]])
                return res