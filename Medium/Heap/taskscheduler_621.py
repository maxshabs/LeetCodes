# Solution for LeetCode Problem 621: Task Scheduler
# Time Complexity: O(n), where n is the number of tasks and 26 is the maximal number of unique tasks.
# - Counting task frequencies takes O(n).
# - Heapify operation takes O(26), and each push/pop operation on the heap takes O(log 26).
# - Processing all tasks and cooldowns takes O(n).
# Space Complexity: O(1), because there are at most 26 unique tasks, for the heap and cooldown queue.

import heapq
from typing import List
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Calculates the least number of units of time required to complete all tasks
        given a cooldown period between identical tasks.

        :param tasks: List of tasks represented as uppercase English letters.
        :param n: Non-negative integer representing the cooldown period.
        :return: The least number of time units required to complete all tasks.
        """
        # Step 1: Initialize variables
        time_passed = 0
        cooldown_queue = deque()
        
        # Step 2: Calculate task frequencies
        freq = [0] * 26
        for char in tasks:
            freq[ord(char) - 65] += 1
        
        # Step 3: Create a max-heap with task frequencies
        task_and_freq = []
        for i in range(26):  # 26 uppercase English letters
            if freq[i] > 0:
                task_and_freq.append(-freq[i])  # Use negative frequencies for max-heap behavior
        
        heapq.heapify(task_and_freq)
        
        # Step 4: Process tasks and cooldowns
        while task_and_freq or cooldown_queue:
            if not task_and_freq:
                # Fast-forward to the next available task in the cooldown queue
                time_passed = cooldown_queue[0][1]
            else:
                # Execute the most frequent task
                cur_freq = 1 + heapq.heappop(task_and_freq)  # Decrement frequency
                if cur_freq < 0:
                    cooldown_queue.append([cur_freq, time_passed + n])  # Add task to cooldown queue
            
            # Check if the cooldown period of the first task in the queue has expired
            if cooldown_queue and cooldown_queue[0][1] == time_passed:
                heapq.heappush(task_and_freq, cooldown_queue.popleft()[0])
                
            time_passed += 1
        
        # Step 5: Return total time passed
        return time_passed
