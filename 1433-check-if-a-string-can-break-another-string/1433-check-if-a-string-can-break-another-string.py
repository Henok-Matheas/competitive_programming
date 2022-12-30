class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        list1 = [char for char in s1]
        list2 = [char for char in s2]
        
        list1.sort()
        list2.sort()
        
        if list1 > list2:
            list1, list2 = list2, list1
            
        for idx, first in enumerate(list1):
            second = list2[idx]
            if first > second:
                return False
            
        return True
        
            