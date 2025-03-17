# Solution for LeetCode Problem 841: Keys and Rooms
# Time Complexity: O(N + E), where N is the number of rooms and E is the number of keys.
#   - We visit each room once (O(N)).
#   - We process each key exactly once (O(E)).
# Space Complexity: O(N), as we store visited rooms in a set.

from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        """
        Determines if all rooms in a given structure can be visited starting from room 0.

        Parameters:
        rooms (List[List[int]]): A list of rooms, where each room contains a list of keys to other rooms.

        Returns:
        bool: True if all rooms can be visited, False otherwise.
        """
        visited = {0}  # Set to track visited rooms
        available = []  # Stack for DFS traversal

        # Add keys from the first room to the available list
        for key in rooms[0]:
            available.append(key)

        # Perform DFS traversal using a stack
        while available:
            cur_room = available.pop()  # Visit the next available room
            visited.add(cur_room)  # Mark room as visited

            # Add new keys to the available list if they lead to unvisited rooms
            for key in rooms[cur_room]:
                if key not in visited:
                    available.append(key)

        # If we have visited all rooms, return True; otherwise, return False
        return len(visited) == len(rooms)
