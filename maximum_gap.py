import math
from typing import List

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        minVal, maxVal = min(nums), max(nums)
        if minVal == maxVal:
            return 0

        bucket_size = math.ceil((maxVal - minVal) / (n - 1))
        bucket_count = n - 1

        buckets_min = [math.inf] * bucket_count
        buckets_max = [-math.inf] * bucket_count

        # Place numbers into buckets
        for num in nums:
            if num == minVal or num == maxVal:
                continue
            idx = (num - minVal) // bucket_size
            buckets_min[idx] = min(buckets_min[idx], num)
            buckets_max[idx] = max(buckets_max[idx], num)

        max_gap = 0
        prev = minVal

        for i in range(bucket_count):
            if buckets_min[i] == math.inf:
                continue
            max_gap = max(max_gap, buckets_min[i] - prev)
            prev = buckets_max[i]

        max_gap = max(max_gap, maxVal - prev)

        return max_gap
