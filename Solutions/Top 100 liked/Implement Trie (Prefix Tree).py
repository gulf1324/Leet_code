class Trie:
    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node[self.end_symbol] = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return self.end_symbol in node
        # == return node.get(self.end_symbol, False)    

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True
###################################################################                
s = Trie()
s.insert("apple")
print(s.search("apple"))  # True
print(s.search("app"))    # False
print(s.startsWith("app")) # True
