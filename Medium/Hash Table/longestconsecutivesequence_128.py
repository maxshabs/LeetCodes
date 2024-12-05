# Solution for LeetCode Problem 128: Longest Consecutive Sequence
# Time Complexity: O(n), where n is the number of elements in the input list `nums`
#   - Inserting all elements into a set takes O(n).
#   - Each number is visited at most twice, and set lookups are O(1) on average.
# Space Complexity: O(n), as we store all elements of the input list in a set.
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Step 1: Convert the list to a set for O(1) lookups
        nums_set = set(nums)

        # Initialize the maximum sequence length
        max_sequence = 0

        # Step 2: Iterate through the list to find the start of sequences
        for num in nums:
            cur_sequence = 0

            # Check if the current number is the start of a sequence
            if num - 1 not in nums_set:
                # If it is, count the length of the sequence
                cur_sequence += 1
                while num + cur_sequence in nums_set:
                    cur_sequence += 1

                # Update the maximum sequence length
                max_sequence = max(max_sequence, cur_sequence)

        return max_sequence
