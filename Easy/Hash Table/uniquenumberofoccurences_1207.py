# Solution for LeetCode Problem 1207: Unique Number of Occurrences
# Time Complexity: O(n), where n is the length of the input list `arr`
#   - Counting occurrences takes O(n).
#   - Checking for duplicate occurrences also takes O(n).
# Space Complexity: O(n), due to storing the occurrences in a dictionary and the `occ_count` list.

from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # Step 1: Create a dictionary to count occurrences of each number
        occ_dict = {}
        for num in arr:
            if num not in occ_dict:
                occ_dict[num] = 1
            else:
                occ_dict[num] += 1

        # Step 2: Create a list to track occurrence counts
        occ_count = [0] * len(arr)

        # Step 3: Check if any occurrence count appears more than once
        for key in occ_dict:
            occ_count[occ_dict[key] - 1] += 1
            # If any count appears more than once, return False
            if occ_count[occ_dict[key] - 1] > 1:
                return False

        # Step 4: If no duplicate counts are found, return True
        return True
