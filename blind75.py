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