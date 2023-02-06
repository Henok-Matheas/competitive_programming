class DetectSquares:
    """
    X-Y
    
    [3, 10]
    [11, 2]
    [3, 2]
    [11, 2]
    
    
    [11, 2], [11, 2]
    
    [11, 10]
    
    look for nodes in the same row
    then that node could be of lower col or higher col
    
    find node down = same col, row is same dist
              downleft = same col as me, and row is same dist
              
    or
    find nodeup = same colas new, row is same dist
         nodeupleft = same col as me, row is same dist
         
         
    what if you have four points in the same place
    you should be decreasing the count then.
    
    
    
    have a rowdict for every row which will hold cols
    
    have a points dict with count
    
    
    when we add pointsdict[point] += 1
    we will also add that col into the rows thing
    .   .
    .   .
    """
    def __init__(self):
        self.rows = defaultdict(list)
        self.points = defaultdict(int)
        

    def add(self, point: List[int]) -> None:
        row, col = point
        self.rows[row].append(col)
        self.points[(row, col)] += 1
        

    def count(self, point: List[int]) -> int:
        row, col = point
        squares = 0
        
        for col2 in self.rows[row]:
            if col2 == col:
                continue
                
            col3, col4 = col2, col
            dist = abs(col - col2)
            
            row3, row4 = row + dist, row + dist
            squares += self.points[(row3, col3)] * self.points[(row4, col4)]
            
            row3, row4 = row - dist, row - dist
            
            squares += self.points[(row3, col3)] * self.points[(row4, col4)]
            
            
        return squares
            
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)