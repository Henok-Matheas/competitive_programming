class RandomizedCollection:

    def __init__(self):
        ## similar to the non duplicate one but instead of a dict which holds an index it will hold a set of indexes
        ## when inserting we add the size of the array to the dict set
        ## when removing
            ## we will go to the dict set and choose one index and pop
            ## we will go to the array and then
                ## get value at last index and get last_val
                ## go to dict[last_val].pop(last_index)
                ## dict[last_val].add(val_index)
                ## array.pop
        self.dict = {}
        self.array = []
        

    def insert(self, val: int) -> bool:
        is_new = False
        
        if val not in self.dict:
            is_new = True
            self.dict[val] = set()
            
        self.dict[val].add(len(self.array))
        self.array.append(val)
        
        return is_new
        

    def remove(self, val: int) -> bool:
        ## we will go to the dict set and choose one index and pop
            ## we will go to the array and then
                ## get value at last index and get last_val
                ## go to dict[last_val].pop(last_index)
                ## dict[last_val].add(val_index)
                ## array.pop
        if val not in self.dict:
            return False
        
        val_idx = self.dict[val].pop()
        last_idx = len(self.array) - 1
        last_val = self.array[-1]
        
        self.array[val_idx] = last_val
        self.array.pop()
        
        
        self.dict[last_val].add(val_idx)
        self.dict[last_val].remove(last_idx)
            
        if len(self.dict[val]) == 0:
            self.dict.pop(val)
            
        return True
        

    def getRandom(self) -> int:
        idx = random.randint(0, len(self.array) - 1)
        
        return self.array[idx]
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()