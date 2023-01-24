class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        """
        it's a bfs
        
        starting from the bottom left, we can have the range as directions/ destinations
        
        we can map number to their index in a hashmap
        
        
        if the cell is end cell we return moves
        
        and if the cell is snake/ladder we append that destination to queue
        and change the direction to -1
        
        21 22 23 24 25
        20 19 18 17 16
        11 12 13 14 15
        10 9  8  7  6
        1  2  3  4  5
        
        5 -> 15
        10 -> 25
        8 -> 20
        12 -> 17
        14 -> 19
        20 -> 2
        17 -> 6
        23 -> 19
        24 -> 10
        """
        
        """
        step1: make the hashmap of snakes and ladders
            from the top down we can decrease 
        """
        ### mapper
        hashmap = {}
        END = len(board) ** 2
        value = 1
        count = 0
        for row in reversed(range(len(board))):
            range_ = range(len(board))
            if count % 2:
                range_ = reversed(range_)
                
            for col in range_:
                cell = board[row][col]
                if cell == -1:
                    cell = value
                hashmap[value] = cell
                value += 1
            count += 1
                
        ## moves, value
        startmove, startvalue = 0, 1
        queue = deque([(startmove, startvalue)])
        
        while queue:
            move, value = queue.popleft()
            
            if value == END:
                return move
            
            for next_ in range(value + 1, min(value + 6, END) + 1):
                if next_ in hashmap:
                    queue.append((move + 1,  hashmap[next_]))
                    hashmap.pop(next_)
                    
        return -1