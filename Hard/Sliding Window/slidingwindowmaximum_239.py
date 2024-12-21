# Solution for LeetCode Problem 239: Sliding Window Maximum
# Time Complexity: O(n), where n is the length of the input array `nums`
#   - Each element is added to and removed from the deque at most once, making the operations linear.
# Space Complexity: O(k), where k is the size of the sliding window
#   - The deque stores at most k indices at any time.

from typing import List
import collections

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Output list to store the maximum values for each window
        output = []

        # A deque to store the indices of elements in `nums`
        # The deque maintains a decreasing order of values in the current window
        q = collections.deque()

        # Left pointer for the sliding window
        left = 0

        # Iterate through the array with the right pointer
        for right in range(len(nums)):
            # Remove elements from the back of the deque that are smaller than the current element
            # These elements are not useful as the current element is larger and will dominate
            while q and nums[q[-1]] < nums[right]:
                q.pop()

            # Add the current element's index to the deque
            q.append(right)

            # Remove the index from the front of the deque if it is out of the current window
            if left > q[0]:
                q.popleft()

            # When the window size is at least `k`, calculate the maximum for the current window
            if right + 1 >= k:
                # The maximum is at the front of the deque
                output.append(nums[q[0]])

                # Slide the window by incrementing the left pointer
                left += 1

        # Return the list of maximum values for all sliding windows
        return output
