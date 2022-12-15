class Node:
    def __init__(self, idx):
        self.idx = idx
        self.left = None
        self.right = None
    

class Solution:
    def find_next(self,type_, idx, node, arr):
        ## returns next index
        if not node:
            return 0
        if arr[idx] == arr[node.idx]:
            return node.idx
        better = 0
        if (type_ == "INC" and arr[idx] > arr[node.idx]):
            better = self.find_next(type_, idx, node.right, arr)
            
        elif (type_ == "INC" and arr[idx] < arr[node.idx]):
            better = node.idx
            found = self.find_next(type_, idx, node.left, arr)
            if found and arr[found] < arr[better]:
                better = found
        
        elif (type_ == "DEC" and arr[idx] < arr[node.idx]):
            better = self.find_next(type_, idx, node.left, arr)
            
        else:
            better = node.idx
            found = self.find_next(type_, idx, node.right, arr)
            if found and arr[found] > arr[better]:
                better = found
                
        return better
        
    def insert(self,idx, node, arr):
        if not node:
            return Node(idx)
        
        if arr[idx] == arr[node.idx]:
            node.idx = idx
            
        elif arr[idx] < arr[node.idx]:
            node.left = self.insert(idx, node.left, arr)
            
        else:
            node.right = self.insert(idx, node.right, arr)
        return node
    
#     def iterator(self, node):
#         if not node:
#             return
        
#         self.iterator(node.left)
#         print(node.idx)
#         self.iterator(node.right)
    
    def oddEvenJumps(self, arr: List[int]) -> int:
        even = [False] * len(arr)
        odd = [False] * len(arr)
        even[-1], odd[-1] = True, True
        
        node = Node(len(arr) - 1)
        
        for idx in reversed(range(len(arr) - 1)):
            ## do operations when curr idx is odd
            ## find next increasing idx
            next_increasing = self.find_next("INC", idx, node, arr)
            ## find next
            if next_increasing and even[next_increasing]:
                odd[idx] = True
            
            ## do operations when curr idx is even
            next_decreasing = self.find_next("DEC", idx, node, arr)
                
            if next_decreasing and odd[next_decreasing]:
                even[idx] = True
                
            self.insert(idx, node, arr)
            
        return odd.count(True)
        