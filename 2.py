from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i in range(len(nums)):
            for j in range(len(nums)-1):
                if nums[i] < nums[j]:
                    nums[j], nums[i] = nums[i], nums[j]
        return nums