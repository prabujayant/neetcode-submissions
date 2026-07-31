from collections import defaultdict, deque

class Solution:
    def foreignDictionary(self, words: list[str]) -> str:
        # Step 1: build graph
        adj = defaultdict(set)   # use set to avoid duplicate edges
        indegree = {c: 0 for w in words for c in w}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            # invalid case: prefix issue (e.g. ["abc", "ab"])
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break

        # Step 2: topological sort
        q = deque([c for c in indegree if indegree[c] == 0])
        topo = []

        while q:
            node = q.popleft()
            topo.append(node)
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return "".join(topo) if len(topo) == len(indegree) else ""
