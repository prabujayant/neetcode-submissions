class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {char: set() for word in words for char in word}

        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            minLen = min(len(word1), len(word2))

            if len(word1) > len(word2) and word1[:minLen] == word2[:minLen]:
                return ""

            for j in range(minLen):
                if word1[j] != word2[j]:
                    graph[word1[j]].add(word2[j])
                    break

        visited = {}
        result = []
        def dfs(char):
            if char in visited:
                return visited[char]
            visited[char] = True

            for neighbor in graph[char]:
                if dfs(neighbor):
                    return True
            visited[char] = False
            result.append(char)
            return False

        for char in graph:
            if char not in visited:
                if dfs(char):
                    return ""
        result.reverse()
        return "".join(result)
