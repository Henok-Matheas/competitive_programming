class Solution:
    def knightDialer(self, n: int) -> int:
        """
        8 branches
        
        depth is n
        
        
        8 ** n
        
        
        
        we can instead do a dp
        
        
        of current key, and remaining
        
        
        if we can do this we can decrease the complexity to
        
        10 * n
        
        numpad * n
        
        
        for the dp
        
        
        we will also have the two dimensional representation of the keys
        
        0 => [0, 0]
        1 => [0, 1]
        
        
        or we can go to int division for the row and the remainder for the column
        
        so for neighbours
        
        we need to first change the current node into row and column
        
        then for the children we add the delta_row and delta_col
        
        and for the new_row and new_col change it into a number
        
        if that 0 <= new_row < 4 and 0 <= new_col < 4 and number != 9:
            current_sum += sum[number]
            
            
        return sum(last_row) % (10 ** 9 + 7)
        
        
        for loop over the numpad
        
        
        we can even do a bottom up
        
        for the bottom up we will have numpad * all n's
        
        
        for size in range(n):
            for numpad_key in range(11):
                if numpad_key == 
        
        
        """
        MOD = 10 ** 9 + 7
        keypad_size = 11
        keypad_row = 3
        forbidden_keypad = 9
        movements = [[0] * keypad_size for _ in range(n)]
        movements[0] = [1] * keypad_size
        movements[0][forbidden_keypad] = 0
        directions = [[-2, -1], [-2, 1], [2, -1], [2, 1], [-1, -2], [1, -2], [-1, 2], [1, 2]]
        
        for movement_idx in range(1, n):
            for keypad in range(keypad_size):
                if keypad == forbidden_keypad:
                    continue
                    
                row, col = keypad // keypad_row, keypad % keypad_row
                
                for delta_row, delta_col in directions:
                    new_row, new_col = row + delta_row, col + delta_col
                    new_keypad = new_row * keypad_row + new_col
                    
                    if 0 <= new_row < 4 and 0 <= new_col < keypad_row and new_keypad != forbidden_keypad and new_keypad < keypad_size:
                        movements[movement_idx][keypad] = (movements[movement_idx][keypad] + movements[movement_idx - 1][new_keypad]) % MOD
                        
                        
        return sum(movements[-1]) % MOD