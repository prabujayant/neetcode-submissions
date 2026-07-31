class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Step 1: Build adjacency list (graph)
        graph = {char: set() for word in words for char in word}

        # Step 2: Add edges between characters
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            minLen = min(len(word1), len(word2))

            # Edge case: word2 is a prefix of word1 (invalid)
            if len(word1) > len(word2) and word1[:minLen] == word2[:minLen]:
                return ""

            # Add the first difference as a directed edge
            for j in range(minLen):
                if word1[j] != word2[j]:
                    graph[word1[j]].add(word2[j])
                    break

        # Step 3: Visit all nodes using DFS
        visited = {}  # char -> True (visiting), False (visited)
        result = []

        def dfs(char):
            if char in visited:
                return visited[char]  # if True, cycle detected

            visited[char] = True  # mark as visiting

            for neighbor in graph[char]:
                if dfs(neighbor):
                    return True  # cycle detected

            visited[char] = False  # mark as visited
            result.append(char)    # add to result after visiting all neighbors

            return False

        # Step 4: Run DFS for all characters
        for char in graph:
            if char not in visited:
                if dfs(char):
                    return ""  # cycle detected, invalid order

        # Step 5: Reverse the result to get correct order
        result.reverse()
        return "".join(result)
