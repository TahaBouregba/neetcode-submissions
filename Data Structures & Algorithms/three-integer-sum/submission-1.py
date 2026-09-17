class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len (nums)
        s = set ()
        nums.sort()

        for i in range (n):
            right = n-1
            left = i+1
            while left < right:
                if nums [i] + nums [right] + nums [left] == 0:
                    T = (nums [i] , nums [right] , nums [left])
                    s.add(T)
                    left += 1
                    right -=1
                elif nums [i] + nums [right] + nums [left] < 0:
                    left += 1
                else:
                    right -=1
        return [list(x) for x in s]


                        
                        




        