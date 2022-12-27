class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        ### explanation
        ## we need to know the places of the largest values.
        ## after that, since the lower values can easily be inserted where they are needed without disrupting
        ## the flow
        people.sort(key= lambda value: (-value[0], value[1]))
        queue = []
        for height, count in people:
            queue.insert(count, [height, count])
            
        return queue
            
        