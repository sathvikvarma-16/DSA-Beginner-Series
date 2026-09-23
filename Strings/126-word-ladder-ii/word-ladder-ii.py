class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
        words = set(wordList)
        if endWord not in words:
            return []
        queue = deque([beginWord])
        parents = defaultdict(list)
        visited = {beginWord}
        found = False
        while queue and not found:
            level_visited = set()
            for _ in range(len(queue)):
                word = queue.popleft()
                for i in range(len(word)):
                    for ch in "abcdefghijklmnopqrstuvwxyz":
                        newWord = word[:i] + ch + word[i + 1:]
                        if newWord in words and newWord not in visited:
                            parents[newWord].append(word)
                            if newWord not in level_visited:
                                level_visited.add(newWord)
                                queue.append(newWord)
                            if newWord == endWord:
                                found = True
            visited.update(level_visited)
        ans = []
        path = [endWord]
        def backtrack(word):
            if word == beginWord:
                ans.append(path[::-1])
                return
            for prev in parents[word]:
                path.append(prev)
                backtrack(prev)
                path.pop()
        if found:
            backtrack(endWord)
        return ans
        


"""
1. Understand the problem simply

In Word Ladder I, we had to return the length of the shortest transformation.

In Word Ladder II, we must return all the shortest transformation sequences from beginWord to endWord.

Rules
Change only one letter at a time.
Every new word must exist in wordList.
Reach endWord.
Return only the sequences that use the minimum number of transformations.
If no transformation is possible, return an empty list [].
Example
beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

There are two shortest sequences:

hit → hot → dot → dog → cog
hit → hot → lot → log → cog

Both sequences contain 5 words, so the answer is:

[
    ["hit", "hot", "dot", "dog", "cog"],
    ["hit", "hot", "lot", "log", "cog"]
]

We need BFS to find the shortest paths and backtracking to build all those paths
"""