class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len (heights)
        right = n-1
        left = 0
        prd = 1
        max = 0
        while left < right:
            prd = (right-left) * min(heights[right] , heights[left])
            if max < prd :
                max = prd
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max

