# Solution for LeetCode Problem 15: 3Sum
# Time Complexity: O(n^2), where n is the length of the input list `nums`
#   - Sorting the list takes O(n log n)
#   - The two-pointer approach runs in O(n) for each element, leading to an overall O(n^2) complexity.
# Space Complexity: O(1), not including the output list, as no additional data structures are used.
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Step 1: Sort the input list to facilitate the two-pointer approach
        nums.sort()

        # Initialize the result list to store the triplets
        result = []
        len_nums = len(nums)

        # Iterate through the list, fixing one number at a time
        for i in range(len_nums - 2):
            # Skip duplicate values for the outer loop to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Set the target to the negative of the current number
            target = -nums[i]

            # Initialize two pointers: left and right
            left, right = i + 1, len_nums - 1

            # Two-pointer approach to find pairs that sum to the target
            while left < right:
                couple_sum = nums[left] + nums[right]

                if couple_sum < target:
                    # Increase the left pointer to increase the sum
                    left += 1
                elif couple_sum > target:
                    # Decrease the right pointer to decrease the sum
                    right -= 1
                else:
                    # Found a valid triplet that sums to zero
                    result.append([nums[i], nums[left], nums[right]])

                    # Move both pointers to skip duplicate values
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        # Return the list of unique triplets
        return result
