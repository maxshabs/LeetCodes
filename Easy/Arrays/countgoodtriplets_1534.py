# Solution for LeetCode Problem 1534: Count Good Triplets
# Time Complexity: O(n^3), where n is the length of the input list `arr`
#   - Three nested loops to evaluate all possible triplets (i, j, k)
# Space Complexity: O(1), using constant extra space

from typing import List


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        count = 0

        # Iterate through all possible triplets (i, j, k)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                # Check first condition: |arr[i] - arr[j]| <= a
                if abs(arr[i] - arr[j]) <= a:
                    for k in range(j + 1, n):
                        # Check all conditions for a good triplet
                        if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                            count += 1  # Valid triplet found

        return count
