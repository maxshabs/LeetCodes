# Solution for LeetCode Problem 763: Partition Labels
# Time Complexity: O(n), where n is the length of the input string `s`.
# Space Complexity: O(1), as the dictionary `last_app` will have at most 26 entries (one for each letter of the English alphabet).

from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Step 1: Record the last occurrence of each character in the string
        last_app = {}
        for i, char in enumerate(s):
            last_app[char] = i
        
        # Step 2: Initialize variables for managing partitions
        lengths = []
        cur_end = 0   # End index of the current partition
        cur_len = 0   # Length of the current partition
        
        # Step 3: Iterate through the string to determine partitions
        for i, char in enumerate(s):
            cur_end = max(cur_end, last_app[char])  # Update the end of the current partition
            cur_len += 1  # Increment the current partition length
            
            # If the current index reaches the end of the partition, finalize it
            if i == cur_end:
                lengths.append(cur_len)
                cur_len = 0  # Reset for the next partition
        
        return lengths
