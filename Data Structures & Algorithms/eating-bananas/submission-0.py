class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        maxx = 0

        # Find the biggest pile
        for i in piles:
            if i > maxx:
                maxx = i

        left = 1
        right = maxx

        # Binary search for the minimum k
        while left < right:

            mid = (left + right) // 2
            count = 0

            # Calculate total hours for speed mid
            for i in piles:
                count += (i + mid - 1) // mid

            # mid is fast enough → try a smaller speed
            if count <= h:
                right = mid

            # mid is too slow → increase speed
            else:
                left = mid + 1

        return left



            
        