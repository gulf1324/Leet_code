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
        
############################################################################################
trie = Trie()
operations = ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
inputs = [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
expected_output = [None, None, True, False, True, None, True]

results = [None]

# Perform operations
for op, args in zip(operations[1:], inputs[1:]):
    if op == "insert":
        trie.insert(*args)
        results.append(None) 
    elif op == "search":
        results.append(trie.search(*args))
    elif op == "startsWith":
        results.append(trie.startsWith(*args))

# Print results
print("Output:", results)
print("Expected:", expected_output)
print("Test Passed:", results == expected_output)