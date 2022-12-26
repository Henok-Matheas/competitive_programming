class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count = [0, 0, 0]
        ## for 20 take a 10, 5 if possible, or 3: 5 else false
        ## for 10 take a 5
        ## for 5 count
        
        for bill in bills:
            if bill == 20:
                if count[1] and count[0]:
                    count[0] -= 1
                    count[1] -= 1
                    
                elif count[0] > 2:
                    count[0] -= 3
                else:
                    return False
            elif bill == 10:
                if not count[0]:
                    return False
                count[0] -= 1
            count[bill // 10] += 1
        
        return True
        