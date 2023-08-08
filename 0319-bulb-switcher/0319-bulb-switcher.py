class Solution:
    def bulbSwitch(self, n: int) -> int:
        """
        n off bulbs
        
        then reverse every first bulb
        
        turn reverse every second bulb
        
        reverse every third switch
        
        n bulb
        reverse every n switch
        
        
        on bulbs after n rounds
        
        thought:
        for every number until n if it has odd number of divisors then it gets added
        """
        
        return int(math.sqrt(n))