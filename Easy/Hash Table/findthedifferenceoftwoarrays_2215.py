# Solution for LeetCode Problem 2215: Find the Difference of Two Arrays
# Time Complexity: O(N + M), where N is the length of nums1 and M is the length of nums2.
#   - Converting lists to sets takes O(N + M).
#   - Iterating through the sets to find differences takes O(N + M).
# Space Complexity: O(N + M), as we store the unique elements of nums1 and nums2 in sets.

from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        """
        Finds the elements that are unique to each list.

        Parameters:
        nums1 (List[int]): The first list of integers.
        nums2 (List[int]): The second list of integers.

        Returns:
        List[List[int]]: A list containing two sublists:
            - The first sublist contains elements that are unique to nums1.
            - The second sublist contains elements that are unique to nums2.
        """
        nums1_set = set(nums1)  # Convert nums1 to a set to remove duplicates
        nums2_set = set(nums2)  # Convert nums2 to a set to remove duplicates
        res_one = []  # Stores elements unique to nums1
        res_two = []  # Stores elements unique to nums2

        # Find elements that are in nums1 but not in nums2
        for num in nums1_set:
            if num not in nums2_set:
                res_one.append(num)

        # Find elements that are in nums2 but not in nums1
        for num in nums2_set:
            if num not in nums1_set:
                res_two.append(num)

        return [res_one, res_two]  # Return the result as two separate lists
