# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n

        while left < right:
            mid = left + (right - left) // 2

            if isBadVersion(mid):
                right = mid      # First bad version could be mid
            else:
                left = mid + 1   # First bad version is after mid

        return left