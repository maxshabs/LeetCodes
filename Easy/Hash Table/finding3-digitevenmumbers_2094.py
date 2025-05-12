# Solution for LeetCode Problem 2094: Finding 3-Digit Even Numbers
# Time Complexity: O(1), since at most 1000 3-digit numbers are iterated and checked
# Space Complexity: O(1) for frequency map and output list (bounded size)

from collections import defaultdict
from typing import List

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        result = []
        freq = defaultdict(int)

        # Count digit frequencies
        for d in digits:
            freq[d] += 1

        # Try all valid 3-digit even numbers
        for i in range(1, 10):  # hundreds place cannot be zero
            if freq[i] == 0:
                continue
            freq[i] -= 1

            for j in range(10):  # tens place
                if freq[j] == 0:
                    continue
                freq[j] -= 1

                for k in range(0, 10, 2):  # units place must be even
                    if freq[k] == 0:
                        continue
                    result.append(100 * i + 10 * j + k)

                freq[j] += 1
            freq[i] += 1

        return result