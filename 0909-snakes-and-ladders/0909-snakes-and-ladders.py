class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        hashmap = {}
        value = 1
        n = len(board)
        cols = list(range(0, n))
        for row in reversed(range(n)):
            for col in cols:
                cell = board[row][col]
                if cell == -1:
                    cell = value
                hashmap[value] = cell
                value += 1
            cols.reverse()
                
        startmove, startvalue = 0, 1
        queue = deque([(startmove, startvalue)])
        
        while queue:
            move, value = queue.popleft()
            
            if value == n ** 2:
                return move
            
            for next_ in range(value + 1, min(value + 6, n ** 2) + 1):
                if next_ in hashmap:
                    queue.append((move + 1,  hashmap[next_]))
                    hashmap.pop(next_)
                    
        return -1