# Solution for LeetCode Problem 416: Partition Equal Subset Sum
# Time Complexity: O(n * target), where n is the length of the `nums` list and `target` is the half of the total sum.
# Space Complexity: O(target), where `target` is the half of the total sum, due to the use of a set for subset sums.

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        Determines if the given array `nums` can be partitioned into two subsets
        such that the sum of elements in both subsets is equal.

        :param nums: List of positive integers.
        :return: True if the array can be partitioned into two subsets with equal sum, otherwise False.
        """
        # Step 1: Calculate the total sum of the array
        total_sum = sum(nums)

        # Step 2: If the total sum is odd, partitioning is not possible
        if total_sum % 2:
            return False
        
        # Step 3: Define the target subset sum (half of the total sum)
        target = total_sum // 2

        # Step 4: Use a set to store possible subset sums
        subset_sums = set()
        subset_sums.add(0)

        # Step 5: Iterate through each number in the array
        for num in nums:
            next_set = set()
            for current_sum in subset_sums:
                # If the current number added to a subset sum equals the target, return True
                if num + current_sum == target:
                    return True
                
                # Retain the current subset sum
                next_set.add(current_sum)
                
                # If the current number added to the subset sum exceeds the target, skip it
                if num + current_sum > target:
                    continue
                
                # Add the new subset sum
                next_set.add(num + current_sum)
            
            # Update the subset sums for the next iteration
            subset_sums = next_set
        
        # Step 6: If no subset with the target sum is found, return False
        return False
