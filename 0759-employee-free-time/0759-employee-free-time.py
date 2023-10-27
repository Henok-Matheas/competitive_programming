"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        new_schedule = []
        
        for sched in schedule:
            new_schedule.extend(sched)
        
        new_schedule.sort(key = lambda x : (x.start,x.end))
        
        
        
        merged_schedule = []
        free_times = []
        for inter in new_schedule:
            
            if merged_schedule and inter.start <= merged_schedule[-1].end:
                
                merged_schedule[-1].end = max(merged_schedule[-1].end, inter.end)
            else:
                merged_schedule.append(inter)
        
        
        
        for i in range(1,len(merged_schedule)):
            free_times.append(Interval(merged_schedule[i-1].end,merged_schedule[i].start))
            
        
        return free_times