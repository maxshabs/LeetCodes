# Solution for LeetCode Problem 2071: Maximum Number of Tasks You Can Assign
# Time Complexity: O(n log n + m log m + log(min(n, m)) * (n + m)), where:
#   - n = len(tasks), m = len(workers)
#   - Sorting and binary search dominate runtime
# Space Complexity: O(m), for the deque used in checking feasibility

from typing import List
from collections import deque

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()   # Sort tasks in ascending order of difficulty
        workers.sort() # Sort workers in ascending order of strength

        # Helper to check if it's possible to assign `mid` tasks
        def canAssign(mid):
            made_stronger = deque()        # Queue of workers who can do a task with a pill
            remaining_pills = pills
            worker_index = len(workers) - 1

            # Try to assign the `mid` easiest tasks to the strongest available workers
            for task in reversed(tasks[:mid]):
                # Case 1: Use a previously saved worker boosted by a pill
                if made_stronger and made_stronger[0] >= task:
                    made_stronger.popleft()
                # Case 2: Directly assign a worker who is strong enough
                elif worker_index >= 0 and workers[worker_index] >= task:
                    worker_index -= 1
                # Case 3: Try to use a pill to boost a weaker worker
                else:
                    while worker_index >= 0 and workers[worker_index] + strength >= task:
                        made_stronger.append(workers[worker_index])
                        worker_index -= 1
                    
                    if not made_stronger or remaining_pills == 0:
                        return False  # Can't assign this task

                    made_stronger.pop()
                    remaining_pills -= 1

            return True

        # Binary search for the maximum number of tasks that can be assigned
        left, right = 0, min(len(tasks), len(workers))
        while left < right:
            mid = (right + left + 1) // 2
            if canAssign(mid):
                left = mid
            else:
                right = mid - 1

        return left
