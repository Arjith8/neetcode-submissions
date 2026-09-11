class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for opn in operations:
            if opn == "+":
                stack.append(stack[-1] + stack[-2])
            elif opn == "D":
                stack.append(2 * stack[-1])
            elif opn == "C":
                stack.pop()
            else:
                stack.append(int(opn))
        return sum(stack)