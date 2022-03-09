class Solution:


    def preictPartyVictory(self, sena t
            e: str) -> st
r           :
        
            
           
        
        dic, opposite, visited, idx 
           = {
            "R": deque(),
            "D": deque()
        }, {
            "R": "D",
            "D": "R"
        }, set(), 0
for i in range(len(senate)):
    dic[senate[i]].append(i)
        while dic["R"] and dic["D"]:
            if idx not in visited:
                dic[senate[idx]].append(dic[senate[idx]].popleft())
                visited.add(dic[opposite[senate[idx]]].popleft())
            idx = (idx + 1) % len(senate)
        return "Radiant" if dic["R"] else "Dire"


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
