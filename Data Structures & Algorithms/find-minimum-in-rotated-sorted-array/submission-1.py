class Solution:
    def findMin(self, nums: List[int]) -> int:
        min = 1000
        for i in nums:
            if i < min:
                min = i
        return min