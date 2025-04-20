# Solution for LeetCode Problem 781: Rabbits in Forest
# Time Complexity: O(n), where n is the number of answers
# Space Complexity: O(n), for the hashmap to track remaining group space

from collections import defaultdict

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        same_color_count = defaultdict(int)  # Tracks remaining "slots" in each group of (answer + 1)

        for answer in answers:
            # If this is the start of a new group (i.e., no group with this answer exists)
            if same_color_count[answer] == 0:
                # Create a new group of size (answer + 1), and reserve (answer) more spots
                same_color_count[answer] += answer
            else:
                # Fill an existing group by using one of the remaining spots
                same_color_count[answer] -= 1

        # Total rabbits is:
        # - len(answers) accounts for one rabbit per answer
        # - sum(same_color_count.values()) adds remaining unfilled group sizes
        return len(answers) + sum(same_color_count.values())
