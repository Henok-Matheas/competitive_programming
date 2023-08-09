class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        """
        n bulbs
        4 buttons
        
        A: flip all   [0, n]
        E: flip evens [0, 2, 4]
        O: flip odds  [1, 3, 5]
        T: flip 3     [0, 3, 6]
        
        AOET
        
        
        AA -> NONE
        EE -> NONE
        00 -> NONE
        TT -> NONE
        
        EO -> A
        
        [0, 0, 0, 0]
        [0, 0, 0, 1]
        [0, 0, 1, 0]
        [0, 0, 1, 1]
        [0, 1, 0, 0]
        [0, 1, 0, 1]
        [1, 0, 0, 0]
        [1, 0, 0, 1]
        [0, 0, 1, 0]
        [1, 0, 1, 1]
        [1, 1, 0, 0]
        [1, 1, 0, 1]
        
        
        0
        1 4 7 
        
        
        
        for _ in range(presses)
            for idx in tuples:
                if xor of idx 2 and 3:
                    make idx
                for every idx else:
                    new idx value = 1 - idx_value
                    
        
        12 * 4 * n
        for all presses:
            for 4 of them
                make them the opposite
                
                
        presses * 16 * 4
        
        0, 2, 4, 6
        1, 3, 5, 7
        0, 3, 6, 9
        
        """
        buttons = set([(0, 0, 0, 0)])
        statuses = set([])
        increments = [1, 2, 2, 3]
        starts = [0, 0, 1, 0]
        
        for _ in range(presses):
            child_buttons = set([])
            for button in buttons:
                new_button = list(button)
                
                for idx in range(len(button)):
                    new_button[idx] = 1 - button[idx]
                    child_buttons.add(tuple(new_button))
                    new_button[idx] = button[idx]
            
            buttons = child_buttons 
            
        
        def fill(status, start, increment):
            for idx in range(start, len(status), increment):
                status[idx] = 1 - status[idx]
            
        for button in buttons:
            status = [1] * n
            for idx in range(len(button)):
                if button[idx]:
                    fill(status, starts[idx], increments[idx])
            
            statuses.add("".join(map(str, status)))
                
        return len(statuses)