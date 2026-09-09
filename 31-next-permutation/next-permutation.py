class Solution:
    def nextPermutation(self, nums):
        n = len(nums)

        # 1. Find the first decreasing element from the right
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # 2. Find the element just larger than nums[i]
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1

            nums[i], nums[j] = nums[j], nums[i]

        # 3. Reverse the elements after i
        nums[i + 1:] = reversed(nums[i + 1:])