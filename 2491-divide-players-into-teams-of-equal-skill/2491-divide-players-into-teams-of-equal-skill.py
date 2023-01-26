class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        chemistry = 0
        tot = skill[0] + skill[len(skill) - 1]
        for idx in range(len(skill) // 2):
            curr, mate = skill[idx], skill[~idx]
            
            if curr + mate != tot:
                return -1
            
            chemistry += (curr * mate)
            
        return chemistry
            