class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        def soln(time,security):
            dec = [0] *len(security)
            inc = [0] * len(security)
            ans = []

            for i in range(1,len(security)):
                if security[i] <= security[i-1]:
                    dec[i] = dec[i-1] +1

            for j in range(len(security)-2,-1,-1):
                if security[j] <= security[j+1]:
                    inc[j] = inc[j+1] +1


            for k in range(time,len(security)):
                if inc[k] >= time and dec[k] >= time:
                    ans.append(k)

            return ans
        
        return soln(time,security)
        
        