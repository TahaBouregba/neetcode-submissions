class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        S = set(nums)
        longest = 0

        for j in S:

            if j - 1 not in S:

                count = 1

                while j + count in S:
                    count += 1

                longest = max(longest, count)

        return longest
            









