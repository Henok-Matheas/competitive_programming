class RandomizedCollection:

    def __init__(self):
        self.dictionary = defaultdict(set)
        self.array = []

    def insert(self, val: int) -> bool:
        validity = False if self.dictionary[val] else True
            
        self.dictionary[val].add(len(self.array))
        self.array.append(val)
        
        return validity

    def remove(self, val: int) -> bool:
        
        if not self.dictionary[val]:
            return False
        
        index = self.dictionary[val].pop()
        self.array[index], self.array[-1] = self.array[-1], self.array[index]
        self.array.pop()
        
        if index < len(self.array):
            self.dictionary[self.array[index]].remove(len(self.array))
            self.dictionary[self.array[index]].add(index)
        
        return True

    def getRandom(self) -> int:
        index = random.randint(0, len(self.array) - 1)
        
        return self.array[index]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()