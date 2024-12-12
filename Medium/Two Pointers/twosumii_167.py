# Solution for LeetCode Problem 167: Two Sum II - Input Array Is Sorted
# Time Complexity: O(n), where n is the length of the input list `numbers`
#   - The two-pointer approach ensures each element is processed at most once.
# Space Complexity: O(1), as no additional data structures are used, only two pointers.
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Initialize two pointers: i at the start and j at the end of the list
        i, j = 0, len(numbers) - 1

        # Loop until the pointers meet
        while i < j:
            # Calculate the current sum of the numbers at i and j
            cur_sum = numbers[i] + numbers[j]

            # If the current sum equals the target, return the 1-based indices
            if cur_sum == target:
                return [i + 1, j + 1]

            # If the current sum is greater than the target, move the right pointer left
            elif cur_sum > target:
                j -= 1

            # If the current sum is less than the target, move the left pointer right
            else:
                i += 1
