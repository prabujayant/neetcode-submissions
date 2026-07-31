class WordDictionary:

    def __init__(self):
        self.children = {}
        self.word = False

    def addWord(self, word: str) -> None:
        root = self
        for ch in word:
            if ch not in root.children:
                root.children[ch] = WordDictionary()
            root = root.children[ch]
        root.word = True

    def search(self, word: str) -> bool:
        def dfs(i, root):
            if i == len(word):
                return root.word

            ch = word[i]

            if ch != '.':
                if ch not in root.children:
                    return False
                return dfs(i + 1, root.children[ch])
            else:
                for child in root.children.values():
                    if dfs(i + 1, child):
                        return True
                return False

        return dfs(0, self)
