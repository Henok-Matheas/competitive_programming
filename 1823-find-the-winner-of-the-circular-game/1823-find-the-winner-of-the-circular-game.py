class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        """
        [1, 2, 3, 4, 5]
        [0, 1, 2, 3, 4]
        
        2 removed
        
        [0, 2, 3, 4]
        
        
        to explain my understanding it goes something like this
        
        
        [0, 1, 2, 3, 4]
        
        first we go to 2
        
        now the new array becomes
        
        [2, 3, 4, 0]
        
        or in other words
        
        
        do the same thing for (n - 1, k) but add k to it and % n
        
        [0, 1, 2, 3] + 2 % n
        
        [2, 3, 4, 0]
        
        now next we pick 2 again
        
        [2, 3, 0] + 2 % n
        
        [4, 0, 2]
        
        [0, 1 , 2] + 2
        
        
        
        0 + 2 % 5
        
        3 + 2 % 5
        
        2 + 2 % 5
        
        4 + 2 % 5
        
        1 + 2 % 5
        
        k = 2
        
        2 removed
        
        [1, 3, 4, 5]
        k = 2
        
        4 removed
        
        [1, 3, 5]
        
        1 removed
        
        [3, 5]
        
        5 removed
        
        [3]
        return 3
        
        the bruteforce answer would be to to append 
        
        what if we had a linked list and a dictionary of indexes
        
        
        
        """
        
        
        answer = 0
        
        
        for size in range(1, n + 1):
            answer = (answer + k) % size
            
        return answer + 1