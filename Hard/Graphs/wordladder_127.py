# Solution for LeetCode Problem 127: Word Ladder
# Time Complexity: O(M^2 * N), where M is the length of each word, and N is the number of words in the wordList. 
# - Constructing the adjacency list takes O(M^2 * N).
# - BFS traversal visits each word at most once and explores its neighbors in O(M^2) time.
# Space Complexity: O(M^2 * N), as the adjacency list can contain M^2 patterns for N words, and the queue may store all words.

from collections import defaultdict, deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        # Create an adjacency list for all words based on patterns with one wildcard "*"
        nei = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                nei[pattern].append(word)
        
        visited = set([beginWord])  # Track visited words
        queue = deque([beginWord]) # Queue for BFS
        result = 0                 # Level counter for BFS
        
        while queue:
            result += 1
            q_len = len(queue)
            for _ in range(q_len):
                cur = queue.popleft()  # Current word
                if cur == endWord:
                    return result      # Found the shortest transformation path
                
                for j in range(len(cur)):
                    pattern = cur[:j] + "*" + cur[j + 1:]
                    for word in nei[pattern]:
                        if word not in visited:
                            visited.add(word)
                            queue.append(word)
        
        return 0  # Return 0 if no transformation sequence exists
