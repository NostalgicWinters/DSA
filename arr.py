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

#Three Sum
def threeSum(nums):
    res = []
    nums = sorted(nums)
    
    for n in range(len(nums)-2):
        if nums[n] > 0:
            break
        if n > 0 and nums[n] == nums[n - 1]:
            continue
        l = n+1
        r = len(nums) - 1
        while(l<r):
            s = nums[n] + nums[l] + nums[r]
            if(s==0):
                res.append([nums[n],nums[l],nums[r]])
                r-=1
                l+=1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1
            elif(s>0):
                r-=1
            else:
                l+=1

    return res

def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        res = []
        start = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                if start == nums[i - 1]:
                    res.append(str(start))
                else:
                    res.append(f"{start}->{nums[i - 1]}")
                start = nums[i]

        if start == nums[-1]:
            res.append(str(start))
        else:
            res.append(f"{start}->{nums[-1]}")

        return res

#Suduko checker
def isValidSudoku(self, board: List[List[str]]) -> bool:

    for row in board:
        nums = [n for n in row if n != "."]
        if len(nums) != len(set(nums)):
            return False

        # Check columns
    for col in zip(*board):
        nums = [n for n in col if n != "."]
        if len(nums) != len(set(nums)):
            return False

    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            seen = set()
            for i in range(3):
                for j in range(3):
                    val = board[box_row + i][box_col + j]
                    if val != ".":
                        if val in seen:
                            return False
                        seen.add(val)

    return True


#Best Time to buy or sell a stock
def maxProfit(self, prices: List[int]) -> int:
    l,r = 0,1
    diff = 0
    while r < len(prices):
        if prices[r]>prices[l]:
            profit = prices[r]-prices[l]
            diff = max(profit,diff)
        else:
            l=r
        r+=1
    return diff

    
matrix = [[1,2,3],[4,5,6],[7,8,9]]
grid = matrix[0:2]
b = matrix[0][0]
c = "2"
print(grid)