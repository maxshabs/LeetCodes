# Solution for LeetCode Problem 2179: Count Good Triplets in an Array
# Time Complexity: O(n log n), due to BIT (Fenwick Tree) updates and queries
# Space Complexity: O(n), for storing BITs and helper arrays

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)

        # Map each value in nums2 to its index for fast lookup
        index_in_nums2 = [0] * n
        for i, val in enumerate(nums2):
            index_in_nums2[val] = i

        # Transform nums1 into the position mapping based on nums2
        transformed = [index_in_nums2[val] for val in nums1]

        # Binary Indexed Tree (Fenwick Tree) utility to add value at a position
        def update(bit_tree, index, value):
            while index < len(bit_tree):
                bit_tree[index] += value
                index += index & -index

        # BIT query utility to compute prefix sum up to `index`
        def query(bit_tree, index):
            result = 0
            while index > 0:
                result += bit_tree[index]
                index -= index & -index
            return result

        # Count how many elements to the left of i are smaller than transformed[i]
        smaller_on_left = [0] * n
        bit_tree = [0] * (n + 2)
        for i in range(n):
            # How many elements less than transformed[i] we've seen so far
            smaller_on_left[i] = query(bit_tree, transformed[i])
            update(bit_tree, transformed[i] + 1, 1)

        # Count how many elements to the right of i are greater than transformed[i]
        greater_on_right = [0] * n
        bit_tree = [0] * (n + 2)
        for i in reversed(range(n)):
            # Total seen - elements <= transformed[i]
            greater_on_right[i] = query(bit_tree, n) - query(bit_tree, transformed[i] + 1)
            update(bit_tree, transformed[i] + 1, 1)

        # Count the number of good triplets:
        # For each middle index i, the number of valid triplets is:
        # count of valid left elements * count of valid right elements
        return sum(smaller_on_left[i] * greater_on_right[i] for i in range(n))
