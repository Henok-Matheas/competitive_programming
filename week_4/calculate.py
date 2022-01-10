class Solution:
    def calculate(self, s: str) -> int:
        num_stack = []
        op_stack = []

        op_dict = {"-": "1", "+": 1, "/": "2", "*": 2}

        op2oper = {
            "1": lambda x, y: x - y,
            1: lambda x, y: x + y,
            "2": lambda x, y: x // y,
            2: lambda x, y: x * y,
        }
        for index in range(len(s)):

            try:
                t = int(s[index])
                stri = str(t)

                i = index
                while len(num_stack) > 0 and num_stack[-1][1] + 1 == i:
                    stri = str(num_stack.pop()[0]) + stri
                    # print(stri)
                num_stack.append([int(stri), i])

            except:
                try:
                    op = op_dict[s[index]]

                    while len(op_stack) > 0 and int(op_stack[-1]) >= int(op):

                        y = num_stack.pop()
                        x = num_stack.pop()

                        operator = op_stack.pop()
                        num_stack.append([op2oper[operator](x[0], y[0]), x[1]])
                    op_stack.append(op)
                except:
                    continue

        while len(op_stack) > 0:
            y = num_stack.pop()
            x = num_stack.pop()

            operator = op_stack.pop()
            num_stack.append([op2oper[operator](x[0], y[0]), x[1]])

        return num_stack[0][0]
