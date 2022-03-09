class Solution:

    def predictPartyVictory(self, senate: str) -> str:

        dict = {}
        for idx in range(len(senate)):
            if senate[idx] in dict:
                dict[senate[idx]].append(idx)
            else:
                dict[senate[idx]] = collections.deque([])
                dict[senate[idx]].append(idx)
        visited = set()
        opposite = {"R": "D", "D": "R"}
        answer = {"R": "Radiant", "D": "Dire"}
        if "R" not in dict or "D" not in dict:
            return answer["R"] if "R" in dict else answer["D"]
        while dict["R"] and dict["D"]:
            for idx in range(len(senate)):
                if idx in visited:
                    continue
                senator = senate[idx]
                dict[senator].append(dict[senator].popleft())
                other = opposite[senator]
                if not dict[other]:
                    return answer[senator]
                popped = dict[other].popleft()
                visited.add(popped)
        return answer["R"] if dict["R"] else answer["D"]
