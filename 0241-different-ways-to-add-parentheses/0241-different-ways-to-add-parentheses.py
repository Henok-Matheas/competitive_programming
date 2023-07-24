class Solution:
    @lru_cache(None)
    def diffWaysToCompute(self, expression: str) -> List[int]:
        """
        backtrack solution
        
        but it can also be a divide and conquer question
        
        
        when you find an operation
        
        break down the left and right and operate on the returns
        
        set[left] operation set[right]
        
        
        for left
            for right
                answer.add(left operation right)
                
                
        return answer
        what should the state be?
        """
        if expression.isdigit():
            return [int(expression)]
        
        answer = []
        
        def operate(num1, num2, operation):
            return eval(f"{num1} {operation} {num2}")
        
        operations = set(["+", "-", "*"])
        for idx in range(len(expression)):
            if expression[idx] in operations:
                left_list = self.diffWaysToCompute(expression[:idx])
                right_list = self.diffWaysToCompute(expression[idx + 1:])
                
                for left in left_list:
                    for right in right_list:
                        answer.append(operate(left, right, expression[idx]))
                        
                        
        return answer