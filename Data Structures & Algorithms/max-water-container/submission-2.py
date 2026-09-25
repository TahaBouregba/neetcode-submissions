
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len (heights)
        left = 0
        right = n-1
        prd =1
        max = 0
        while left < right :
            
            prd = min(heights[left], heights[right]) * (right - left)
            if max < prd :
                max = prd
            if heights[left] < heights[right]:
                left +=1
            else :
                right -= 1
        return max
