# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea:
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point:
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        if topRight.x >= bottomLeft.x and topRight.y >= bottomLeft.y and sea.hasShips(topRight, bottomLeft):
            if topRight.x == bottomLeft.x and topRight.y == bottomLeft.y:
                return 1
            
            midX, midY = (topRight.x + bottomLeft.x) // 2, (topRight.y + bottomLeft.y) // 2
            
            first_quad = self.countShips(sea, topRight, Point(midX + 1, midY + 1))
            second_quad = self.countShips(sea, Point(midX, topRight.y), Point(bottomLeft.x, midY + 1))
            third_quad = self.countShips(sea, Point(midX, midY), bottomLeft)
            fourth_quad = self.countShips(sea, Point(topRight.x, midY), Point(midX + 1, bottomLeft.y))
            
            return first_quad + second_quad + third_quad + fourth_quad
            
        return 0