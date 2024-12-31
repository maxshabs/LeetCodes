# Solution for LeetCode Problem 208: Implement Trie (Prefix Tree)
# Time Complexity:
# - Insert Operation: O(L), where L is the length of the word being inserted. Each character is processed once.
# - Search Operation: O(L), where L is the length of the word being searched. Each character is checked in the Trie.
# - StartsWith Operation: O(L), where L is the length of the prefix being searched. Each character of the prefix is checked in the Trie.
# Space Complexity: Trie Construction: O(N * L), where N is the total number of words inserted, and L is the average length of the words. 

class TrieNode:
    """
    Represents a single node in the Trie.
    Each node contains:
      - A dictionary (`children`) to store its child nodes.
      - A boolean (`endOfWord`) indicating if this node marks the end of a valid word.
    """
    def __init__(self):
        self.children = {}  # Maps characters to TrieNode
        self.endOfWord = False  # Marks the end of a word

class Trie:
    """
    A Trie (Prefix Tree) data structure for efficient string operations:
      - Insert words.
      - Search for exact words.
      - Check for prefixes.
    """

    def __init__(self):
        """
        Initializes the root of the Trie.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the Trie.

        :param word: The word to be inserted.
        """
        ptr = self.root  # Start from the root node
        for char in word:
            if char not in ptr.children:  # If the character doesn't exist, create a new node
                ptr.children[char] = TrieNode()
            ptr = ptr.children[char]  # Move to the child node
        ptr.endOfWord = True  # Mark the end of the word

    def search(self, word: str) -> bool:
        """
        Searches for a word in the Trie.

        :param word: The word to search for.
        :return: True if the word exists, False otherwise.
        """
        ptr = self.root  # Start from the root node
        for char in word:
            if char not in ptr.children:  # If any character is missing, return False
                return False
            ptr = ptr.children[char]  # Move to the child node
        return ptr.endOfWord  # Check if it's the end of a word

    def startsWith(self, prefix: str) -> bool:
        """
        Checks if there is any word in the Trie that starts with the given prefix.

        :param prefix: The prefix to search for.
        :return: True if any word starts with the prefix, False otherwise.
        """
        ptr = self.root  # Start from the root node
        for char in prefix:
            if char not in ptr.children:  # If any character is missing, return False
                return False
            ptr = ptr.children[char]  # Move to the child node
        return True  # The prefix exists in the Trie
