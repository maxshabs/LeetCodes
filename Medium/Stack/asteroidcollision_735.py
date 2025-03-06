# Solution for LeetCode Problem 735: Asteroid Collision
# Time Complexity: O(N), where N is the number of asteroids.
#   - Each asteroid is processed once and added/removed from the stack at most once.
# Space Complexity: O(N), as we use a stack to store surviving asteroids.

from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        Simulates asteroid collisions where:
        - A positive asteroid moves to the right.
        - A negative asteroid moves to the left.
        - When two asteroids collide, the smaller one is destroyed; if equal, both are destroyed.

        Parameters:
        asteroids (List[int]): A list of integers representing asteroid directions and sizes.

        Returns:
        List[int]: The state of asteroids after all collisions.
        """
        passed_asteroids = []  # Stack to store asteroids that survived collisions

        for asteroid in asteroids:
            # Collision occurs when the last asteroid is moving right (positive) and the new asteroid moves left (negative)
            while passed_asteroids and asteroid < 0 and passed_asteroids[-1] > 0:
                if abs(asteroid) > passed_asteroids[-1]:  # New asteroid is larger, destroy the last one
                    passed_asteroids.pop()
                    continue  # Continue checking for further collisions
                elif abs(asteroid) == passed_asteroids[-1]:  # Both asteroids are equal, destroy both
                    passed_asteroids.pop()
                break  # New asteroid is destroyed, exit loop
            else:
                passed_asteroids.append(asteroid)  # No collision, asteroid survives

        return passed_asteroids  # Return the list of surviving asteroids
