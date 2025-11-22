def precedence(op):
    precedence_map = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    return precedence_map.get(op, 0)

def infix_to_prefix(expression):
    reversed_expression = expression[::-1].translate(str.maketrans('()', ')('))
 
    stack = []
    postfix_output = []
    for char in reversed_expression:
        if char.isalnum():
            postfix_output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix_output.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and precedence(char) < precedence(stack[-1]):
                postfix_output.append(stack.pop())
            stack.append(char)

    while stack:
        postfix_output.append(stack.pop())

    return "".join(postfix_output)[::-1]

def infix_to_postfix(expression):
    stack = []
    postfix_output = []
    for char in expression:
        if char.isalnum():
            postfix_output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix_output.append(stack.pop())
            stack.pop()  # Pop the '('
        else:  # An operator is encountered
            # Handle right-associativity for '^'
            if char == '^':
                while stack and stack[-1] != '(' and precedence(char) < precedence(stack[-1]):
                    postfix_output.append(stack.pop())
            else: # Handle left-associativity for other operators
                while stack and stack[-1] != '(' and precedence(char) <= precedence(stack[-1]):
                    postfix_output.append(stack.pop())
            stack.append(char)

    while stack:
        postfix_output.append(stack.pop())

    return "".join(postfix_output)

if __name__ == "__main__":
    infix_expression = "a+b*c-d"
    prefix_expression = infix_to_prefix(infix_expression)
    postfix_expression = infix_to_postfix(infix_expression)
    print(f"Infix expression: {infix_expression}")
    print(f"Prefix expression: {prefix_expression}")
    print(f"Postfix expression: {postfix_expression}")
