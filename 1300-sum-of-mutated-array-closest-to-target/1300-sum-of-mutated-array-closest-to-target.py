class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        """
        arr targ
        sort arr
        for every node in range(1, max(nums) + 1):
            choose index that is greater then
            len(index) people will need to be changed
            you have been doing prefix sum
            
            so max(max, prefix_sum + node * (len - idx) - target, -node)
        """
        arr.sort()
        idx = 0
        close = (float("inf"), float("inf"))
        sum_ = 0
        
        
        for mutate in range(arr[-1] + 1):
            while idx < len(arr) and arr[idx] < mutate:
                sum_ += arr[idx]
                idx += 1
            
            changed = abs(sum_ - target + mutate * (len(arr) - idx))
            close = min(close, (changed, mutate))
            
        return close[1]