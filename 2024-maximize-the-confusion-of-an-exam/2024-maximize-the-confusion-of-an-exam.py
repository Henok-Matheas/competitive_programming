class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        """
        increase the number of same answers in a row
        
        answerKey - actual answer
        k - max operations
        
        
        operation = change answer
        
        
        return max no of T or F possible
        
        
        
        SOLUTION
        counter(answer)
            
            while not k and left != answer:
                if left == answer:
                    continue
                else:
                    k += 1
                count -= 1
            
            if current != answer:
                k -= 1
                count += 1
                
            max_count = max(count, max_count)
        
        """
        
        
        def counter(DESIRED, k):
            max_count = 0
            left = 0
            count = 0
            for current in answerKey:
                while not k and current != DESIRED:
                    if answerKey[left] != DESIRED:
                        k += 1
                    
                    left += 1
                    count -= 1
                    
                if current != DESIRED:
                    k -= 1
                count += 1
                max_count = max(max_count, count)
                
            return max_count
        
        return max(counter("T", k), counter("F", k))