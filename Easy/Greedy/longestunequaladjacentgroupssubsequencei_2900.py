# Solution for LeetCode Problem 2900: Longest Unequal Adjacent Groups Subsequence
# Time Complexity: O(n), where n is the length of the input list
# Space Complexity: O(n), for storing the result subsequence

from typing import List

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        # Initialize result with the first word and set its group as the previous group
        result = [words[0]]
        prev = groups[0]

        # Iterate through the remaining words
        for i in range(1, len(words)):
            # If the current word belongs to a different group than the previous,
            # add it to the result and update the previous group
            if groups[i] != prev:
                prev = groups[i]
                result.append(words[i])

        return result
