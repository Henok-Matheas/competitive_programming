class Solution:
    def candy(self, ratings: List[int]) -> int:
        indices = [idx for idx in range(len(ratings))]
        candies = [1] * len(ratings)
        indices.sort(key = lambda idx : ratings[idx])
        for idx in indices:
            rating = ratings[idx]
            maxim = 1
            
            if idx and ratings[idx - 1] < rating:
                maxim = max(maxim, 1 + candies[idx - 1])
                
            if idx + 1 < len(ratings) and ratings[idx + 1] < rating:
                maxim = max(maxim, 1 + candies[idx + 1])
                
            candies[idx] = maxim
    
        return sum(candies)
        ## maximum assignment
        ## use a heap, or sorting, based on their values.
        ## if the current is greater than one of it's neighbours
        ## then we assign 1 + the lesser neighbours assignment