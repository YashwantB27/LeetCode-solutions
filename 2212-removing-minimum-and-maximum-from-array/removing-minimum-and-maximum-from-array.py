class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        minIndex = nums.index(min(nums))
        maxIndex = nums.index(max(nums))

        left = min(minIndex, maxIndex)
        right = max(minIndex, maxIndex)

        # 1. Remove both from the left
        from_left = right + 1

        # 2. Remove both from the right
        from_right = n - left

        # 3. Remove one from left and one from right
        from_both = (left + 1) + (n - right)

        return min(from_left, from_right, from_both)