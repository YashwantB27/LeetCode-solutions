class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        low = min(nums)
        high = max(nums)

        num_set = set(nums)
        ans = []

        for i in range(low, high + 1):
            if i not in num_set:
                ans.append(i)

        return ans