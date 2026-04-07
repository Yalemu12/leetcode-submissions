class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                else:
                    stack.append(int(a / b)) # truncates towards zero
        return stack[0]                            
        """
        Understand: we see that the operators come after the operands 
        so the best data structure that we can use for this is a "Stack"

        Why?
        Because RPN works like this 
        1. Read tokens left -> right
        2. If its a number -> we push it into the stack
        3. if its an operator->
        - we pop two numbers
        - apply the operator
        - push the result back into the stack
        - the last value in the stack = answer
        """



        