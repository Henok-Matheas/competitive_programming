class Solution:
    def minOperations(self, logs: List[str]) -> int:
        """
        ../move to parent folder
        ./ remain in the same folder
        x/ move to the child folder named x(always exists)
        
        
        given logs 
        filesystem starts in the main folder then logs are perfomed
        return min number of operations needed to go back to the main folder
        after the changefolder operations have been done.
        
        
        how to do it:
        
        for every log
        if the log is ../ step -= 1 if step
        if the log is ./ step += 0
        if the log is else step += 1
        """
        
        step = 0
        
        for log in logs:
            if log == "../":
                step -= min(1, step)
            elif log != "./":
                step += 1
        
        return step