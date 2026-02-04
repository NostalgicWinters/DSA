from typing import List
import math

class static_array:
    def __init__(self,size):
        self._size = size
        self._arr = [0 for n in range(size)]
        self._numOfActualElements = 0

    def update(self, lst):
        if(len(lst)==self._size ):
            self._arr = lst
            self._numOfActualElements = len(lst)
        elif(len(lst)<self._size):
            self._arr = lst + [0 for n in range(self._size-len(lst))]
            self._numOfActualElements = len(lst)
        else:
            print("This is an error. Updation failed.\n")

    def append(self, element):
        if self._numOfActualElements == self._size:
            print("Error: The array is already full.\n")
            return

        self._arr[self._numOfActualElements] = element
        self._numOfActualElements += 1


    def delete(self, index):
        if index >= self._numOfActualElements:
            print("Error: Index is not present.\n")
            return

        for i in range(index, self._numOfActualElements - 1):
            self._arr[i] = self._arr[i + 1]

        self._arr[self._numOfActualElements - 1] = 0
        self._numOfActualElements -= 1

    
    def display(self):
        real_arr = [self._arr[n] for n in range(self._numOfActualElements)]
        print(real_arr)


#Two Sum optimised
def twoSum( nums: List[int], target: int) -> List[int]:
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

# Longest Common Prefix brute Force
def longestCommonPrefix(strs: List[str]) -> str:
    if(len(strs)==1):
        return strs[0]
    if(len(strs)==0):
        return ""
    firststr = strs[0]
    for n in range(1,len(strs)):
        res = ''
        smaller = firststr if len(firststr)<= len(strs[n]) else strs[n]
        for k in range(len(smaller)):
            if(firststr[k] == strs[n][k]):
                res += firststr[k]
            else:
                break
        firststr = res
    return res

#Longest common prefix optimised
def longestCommonPrefixOpti(strs: List[str]) -> str:
    smallest = min(strs, key=len)
    for n in strs:
        if len(smallest) == 0:
            return ""
        while not n.startswith(smallest):
            smallest = smallest[:len(smallest)-1]
    return smallest
    
#Container with most water brute force
def maxArea(height: List[int]) -> int:
    pro = 0
    for n in range(len(height)-1):
        for k in range(1,len(height)):
            smaller = min(height[n],height[k])
            if(smaller*(abs(k-n))>pro):
                pro = smaller*(abs(k-n))
    return pro

#Container with most water optimized
def maxAreaOpti(height: List[int]) -> int:
    l, r = 0, len(height) - 1
    max_area = 0

    while l < r:
        h = min(height[l], height[r])
        max_area = max(max_area, h * (r - l))

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return max_area


a = maxAreaOpti([1,8,6,2,5,4,8,3,7])
print(a)