class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ["+", "-", "*", "/"]
        for i in range(len(tokens)):
            if tokens[i] in ops:
                if tokens[i] == "+":
                    n1 = stack.pop()
                    n2 = stack.pop()
                    stack.append(n1+n2)
                if tokens[i] == "-":
                    n1 = stack.pop()
                    n2 = stack.pop()
                    stack.append(n2-n1)
                if tokens[i] == "*":
                    n1 = stack.pop()
                    n2 = stack.pop()
                    stack.append(n1*n2)
                if tokens[i] == "/":
                    n1 = stack.pop()
                    n2 = stack.pop()
                    stack.append(int(n2/n1))
            else:
                stack.append(int(tokens[i]))
        return stack[-1]
                