class Solution:

    def ladderLength(self, beginWord: str, endWord: str,
                     wordList: List[str]) -> int:
        begin = []
        for letter in beginWord:
            begin.append(letter)
        end = []
        for letter in endWord:
            end.append(letter)

        wordDict = set(wordList)

        parents = collections.deque([])
        children = collections.deque([])
        visited = set()

        visited.add(beginWord)
        parents.append([beginWord, 1])

        level = 0
        while parents or children:
            # print("next time")
            while parents:
                # print("got in")
                parent = parents.popleft()
                level = parent[1]

                working = []
                for letter in parent[0]:
                    working.append(letter)
                if parent[0] == endWord:
                    return level

                for j in range(len(working)):
                    new = copy.deepcopy(working)
                    for idx in range(26):
                        new[j] = chr(idx + 97)

                        final = "".join(new)
                        # print("this is final", final)

                        if final in wordDict and final not in visited:
                            # print("jus got in for     ",final,"with level",level + 1)
                            children.append([final, level + 1])
            while children:
                child = children.popleft()
                if child:
                    # print("child is existent")
                    if child[0] not in visited:
                        # print("the child is not visited",child)
                        visited.add(child[0])
                        parents.append(child)
        # print(parents)
        return 0
