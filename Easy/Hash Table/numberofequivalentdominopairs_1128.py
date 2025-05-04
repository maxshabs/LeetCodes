# Solution for LeetCode Problem 1128: Number of Equivalent Domino Pairs
# Time Complexity: O(n), where n is the number of dominoes
# Space Complexity: O(n), for storing counts of unique domino keys

from collections import defaultdict
from typing import List

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = defaultdict(int)  # Dictionary to count each unique domino configuration
        result = 0

        # Normalize each domino so that (a, b) and (b, a) are treated as the same key
        for a, b in dominoes:
            key = (min(a, b), max(a, b))  # Ensure consistent ordering
            count[key] += 1

        # For each group of identical dominoes, count the number of unique pairs
        for val in count.values():
            if val > 1:
                result += val * (val - 1) // 2  # Number of pairs from val identical dominoes

        return result
