class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)

        INF = float('inf')
        best = [INF] * n

        ans = INF
        left = 0
        curr_sum = 0

        for right in range(n):
            curr_sum += arr[right]

            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1

            # Carry forward the best subarray found so far
            if right > 0:
                best[right] = best[right - 1]

            # Found a subarray [left ... right]
            if curr_sum == target:
                length = right - left + 1

                # Need another subarray completely before 'left'
                if left > 0 and best[left - 1] != INF:
                    ans = min(ans, length + best[left - 1])

                # This is the best subarray ending at 'right'
                best[right] = min(best[right], length)

        return -1 if ans == INF else ans