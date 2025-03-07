# Solution for LeetCode Problem 933: Number of Recent Calls
# Time Complexity: O(N), where N is the number of calls made.
#   - Each call is added to the deque once and removed at most once.
# Space Complexity: O(N), as the deque stores calls within the last 3000 milliseconds.

from collections import deque

class RecentCounter:
    """
    Implements a recent counter that tracks the number of requests received in the last 3000 milliseconds.
    """

    def __init__(self):
        """
        Initializes the RecentCounter with an empty queue to store timestamps of requests.
        """
        self.time_q = deque()  # Deque to store timestamps of valid pings

    def ping(self, t: int) -> int:
        """
        Records a new request and returns the number of requests received in the last 3000 milliseconds.

        Parameters:
        t (int): The timestamp of the incoming request.

        Returns:
        int: The number of requests within the time window [t - 3000, t].
        """
        # Remove outdated requests (requests older than t - 3000)
        while self.time_q and self.time_q[0] < t - 3000:
            self.time_q.popleft()

        # Add the new request
        self.time_q.append(t)

        # Return the count of valid requests
        return len(self.time_q)
