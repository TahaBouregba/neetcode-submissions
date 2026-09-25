class Solution:
    def trap(self, height: List[int]) -> int:
        n = len (height)
        left = 0
        right = n-1
        maxleft = 0
        maxright = 0
        water = 0
        while left < right:
            if height[left] <= height [right]:
                if height[left] >= maxleft :
                    maxleft = height[left]
                else :
                    water += maxleft - height[left]
                left += 1
            else :
                if height[right] >= maxright:
                    maxright = height[right]
                else: 
                    water += maxright - height[right]
                right -=1
        return water

        
        
