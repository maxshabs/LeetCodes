# Solution for LeetCode Problem 1: Two Sum
# Time Complexity: O(n), where n is the size of the input array
# Space Complexity: O(n), as we store at most n elements in the dictionary (in the worst case, all elements are distinct).
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Initialize an empty dictionary to store number and its index
        nums_dict = {}
        # Iterate over the array with both index and value
        for i, num in enumerate(nums):
            # Calculate the complement required to reach the target
            if nums_dict.get(target - num) is not None:
                # If found, return the indices of the complement and the current number
                return [nums_dict.get(target - num), i]
            # Store the current number with its index in the dictionary
            nums_dict[num] = i
