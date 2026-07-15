class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            res = i
            print(stack)
            if i == "+":
                a = stack.pop()
                b = stack.pop()
                res = b + a

            elif i == "-":
                a = stack.pop()
                b = stack.pop()
                res = b - a

            elif i == "*":
                a = stack.pop()
                b = stack.pop()
                res = b * a
            elif i == "/":
                a = stack.pop()
                b = stack.pop()
                res = int(b / a)

            stack.append(int(res))
        return stack.pop()
        