class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        """
        bags with weights
        
        divide into k bags
            no empty bag
            substring type inclusion
            cost of a single bag = first marble + last marble
            
        score = total cost of k bags
        
        return diff b/n max score and min score
        
        
        
        thought:
        what if we had a heap of the endings, with associated starts
        e.g for the first example it would look sth like
        [(1, 3), (3, 5), (5, 1)]
        
        what this means is that if we chose the first 1 as an end then 3 has to be a start by definition., same for 3, if we choose 3 as an end 5 has to be a start by definition
        
        
        so if we want to maximize the sum we need to remove k - 1 elements from the heap
        
        k - 1 because if we chose one for the example we can be sure that the the array gets divided into 2 which is k
        
        
        so what we do is we first precompute the max-heap, and the min-heap.
        then for both of the heaps we will remove k - 1 elements and sum them.
        then return the difference between the sums
        
        """
        
        
        max_heap = []
        min_heap = []
        max_sum, min_sum = 0, 0
        for idx in range(len(weights) - 1):
            sum_ = weights[idx] + weights[idx + 1]
            heapq.heappush(max_heap, sum_)
            heapq.heappush(min_heap, -sum_)
            
        for _ in range(k - 1):
            maxim = heapq.heappop(max_heap)
            minim = heapq.heappop(min_heap)
            max_sum += maxim
            min_sum += minim
            
        print(max_sum, min_sum)
        return -(max_sum + min_sum)