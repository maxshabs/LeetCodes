# Solution for LeetCode Problem 212: Word Search II
# Time Complexity: O(N * 4^L), where:
# - N is the number of cells in the board.
# - L is the length of the longest word.
# - 4^L represents the exploration of 4 directions for L levels of recursion.
# Space Complexity: O(W * L), where:
# - W is the number of words in the dictionary.
# - L is the average length of the words (space used by the Trie).

class TrieNode:
    def __init__(self):
        """
        Initializes a TrieNode with a dictionary for children and a flag indicating
        the end of a word.
        """
        self.children = {}
        self.end_of_word = False
    
    def insert(self, word: str) -> None:
        """
        Inserts a word into the Trie starting from this node.
        
        :param word: The word to insert into the Trie.
        """
        cur_node = self
        for char in word:
            if char not in cur_node.children:
                cur_node.children[char] = TrieNode()
            cur_node = cur_node.children[char]
        cur_node.end_of_word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        Finds all the words in the given board that exist in the provided dictionary.
        
        :param board: 2D grid of characters.
        :param words: List of words to search for in the board.
        :return: List of found words.
        """
        # Initialize the Trie with the given words
        trie = TrieNode()
        for word in words:
            trie.insert(word)
        
        # Initialize variables
        visited = set()  # Tracks visited cells in the current path
        result = set()   # To avoid duplicate words
        num_rows, num_cols = len(board), len(board[0])  # Board dimensions
            
        def recursive(row: int, col: int, word: str, node: TrieNode) -> None:
            """
            Backtracking function to explore the board and find words.
            
            :param row: Current row index in the board.
            :param col: Current column index in the board.
            :param word: Current word being formed.
            :param node: Current Trie node being explored.
            """
            # Boundary conditions
            if row < 0 or col < 0 or row >= num_rows or col >= num_cols:
                return
            if (row, col) in visited:
                return
            if board[row][col] not in node.children:
                return
            
            # Add the cell to the visited set and update the word and node
            visited.add((row, col))
            node = node.children[board[row][col]]
            word += board[row][col]
            
            # If a valid word is found, add it to the result set
            if node.end_of_word:
                result.add(word)
            
            # Explore all 4 directions
            recursive(row + 1, col, word, node)
            recursive(row - 1, col, word, node)
            recursive(row, col + 1, word, node)
            recursive(row, col - 1, word, node)
            
            # Backtrack: remove the cell from the visited set
            visited.remove((row, col))
        
        # Start the backtracking process from every cell in the board
        for row in range(num_rows):
            for col in range(num_cols):
                recursive(row, col, "", trie)
        
        return list(result)
