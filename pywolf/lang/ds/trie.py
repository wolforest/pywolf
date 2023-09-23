
from typing import Self

class TrieNode:

    def __init__(self, char: str, isLeaf: bool=False) -> None:
        if char is None:
            raise SystemError("TrieNoe.char can't be None")

        self.char = char
        self.isLeaf = isLeaf
        self.children = {}
        self.counter = 0
    
    def add_children(self, node) -> Self:
        self.children[node.char] = node
        self.counter += 1

        return self

        

class Trie:

    def __init__(self) -> None:
        self.root = TrieNode('')

    def insert(self, word:str) -> Self:
        node: TrieNode = self.root

        for char in word:
            node = self._insert_char(node, char)

        node.isLeaf = True
        return self

    def exists(self, word:str) -> bool:
        node: TrieNode = self.root

        for char in word:
            node = self._match_char(node, char)
            if node is None:
                return False

        return node.isLeaf
    
    def search(self, prefix:str) -> list:
        node: TrieNode = self.root

        for char in prefix:
            node = self._match_char(node, char)
            if node is None:
                return []
        
        output: list = []

        # the matched node contains the last char of prefix
        # so the prefix to be traversed should delete the last char
        self._deep_first_traverse(output, node, prefix[:-1])

        return output

    ########## private methods begin ##########
    def _insert_char(self, node: TrieNode, char: str) -> TrieNode:
        if char in node.children:
            return node.children[char]
        
        newNode = TrieNode(char)
        node.add_children(newNode)

        return newNode

    def _match_char(self, node: TrieNode, char: str) -> TrieNode:
        if char in node.children:
            return node.children[char]

        return None
    
    def _deep_first_traverse(self, output: list, node: TrieNode, prefix) -> None:
        word = prefix + node.char
        if node.isLeaf:
            output.append((word, node.counter))
        
        for child in node.children.values():
            self._deep_first_traverse(output, child, word)


# if __name__=='__main__':
#     t = Trie()
#     t.insert("abc")
#     t.insert("abcd")
#     t.insert("abcde")
#     t.insert("abcdef")
#     t.insert("abcdefg")
#     t.insert("abcdefgi")

#     print(t.search("ab"))