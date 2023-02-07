class Solution:
    def minOperations(self, logs: List[str]) -> int:
        step = 0
        for log in logs:
            if log == "../":
                step -= min(1, step)
            elif log != "./":
                step += 1
        
        return step