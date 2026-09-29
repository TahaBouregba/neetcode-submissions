class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        scan = nums1 + nums2
        scan.sort()

        n = len(scan)

        if n % 2 == 1:
            return scan[n // 2]
        else:
            return (scan[n // 2 - 1] + scan[n // 2]) / 2