class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        """
        problem: no leading zeros
        solution: if the prev number starts with 0 and length is greater than one then return
        
        you can't have an operation before the digits
        
        question is a backtrack question.
        
        -> if there were no leading zeros
        
        for every digit,
        you can add it to a previous number
        mult to prev
        sub with prev
        concat with prev
        
        
        state: idx, expression
        
        
        
        """
        operations = "+-*"
        
        
        def backtrack(idx: int, expression: List[int]):
            if len(expression[-1]) > 1 and expression[-1][0] == "0":
                return []
            
            if idx == len(num):
                string_expression = "".join(expression)
                output = eval(string_expression)
                if output == target:
                    answer.append(string_expression)
                return
            
            if idx:
                for operation in operations:
                    expression.append(operation)
                    expression.append(num[idx])
                    backtrack(idx + 1, expression)
                    expression.pop()
                    expression.pop()
                    
            expression[-1] += num[idx]
            backtrack(idx + 1, expression)
            expression[-1] = expression[-1][:len(expression) - 1]
        
        answer, expression = [], [""]
        idx = 0
        backtrack(idx, expression)
        
        return answer