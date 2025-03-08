# Solution for LeetCode Problem 649: Dota2 Senate
# Time Complexity: O(N), where N is the length of the senate string.
#   - Each senator is added and removed from the queue at most once.
#   - Processing each round takes O(1) per senator, leading to O(N) total.
# Space Complexity: O(N), as we use two queues to store senator indices.

from collections import deque
from typing import List

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        """
        Determines the winning party in the Dota2 Senate voting process.

        Parameters:
        senate (str): A string representing the sequence of senators ('R' for Radiant, 'D' for Dire).

        Returns:
        str: "Radiant" if the Radiant party wins, "Dire" if the Dire party wins.
        """
        n = len(senate)  # Total number of senators
        r_queue = deque()  # Queue to track Radiant senators
        d_queue = deque()  # Queue to track Dire senators

        # Initialize queues with the indices of Radiant ('R') and Dire ('D') senators
        for i, sen in enumerate(senate):
            if sen == "R":
                r_queue.append(i)
            else:
                d_queue.append(i)
                
        # Process the banning rounds until one party is eliminated
        while r_queue and d_queue:
            if r_queue[0] < d_queue[0]:  # Radiant senator acts first
                d_queue.popleft()  # Remove the first Dire senator
                r_queue.append(r_queue.popleft() + n)  # Move Radiant senator to the next round
            else:  # Dire senator acts first
                r_queue.popleft()  # Remove the first Radiant senator
                d_queue.append(d_queue.popleft() + n)  # Move Dire senator to the next round
        
        # The party with remaining senators wins
        return "Radiant" if r_queue else "Dire"
