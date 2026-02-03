from typing import List

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


def twoSum( nums: List[int], target: int) -> List[int]:
    res = []
    a = None
    for n in range(len(nums)-1):
        if(((target - nums[n]) in nums)):
            if(nums.index(target - nums[n])!=n):
                a = nums.index(target - nums[n])
                res.append(n)
                res.append(a)
                return res
            elif(nums.index(target - nums[n])==n):
                if(nums.count(target - nums[n])>1):
                    a = nums.index(target-nums[n],n+1)
                    res.append(n)
                    res.append(a)
                    return res

a = twoSum([3,3],6)
print(a)