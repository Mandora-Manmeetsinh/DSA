# def infix_to_postfix(exp) :
#     stack = []
#     postfix = []
#     precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
#     associativity = {'+': 'left', '-': 'left', '*': 'left', '/': 'left', '^': 'right'}

#     for char in exp:
#         if char.isalnum():
#             postfix.append(char)
#         elif char in precedence:
#             while (stack and stack[-1]!= '(' and
#                    precedence[char] <= precedence[stack[-1]] and associativity[char] == 'left' or (precedence[char] < precedence[stack[-1]] and associativity[char] == 'right')):
#                 postfix.append(stack.pop())
#             stack.append(char)
#         elif char == '(':
#             stack.append(char)
#         elif char == ')':
#             while stack[-1]!= '(':
#                 postfix.append(stack.pop()) 
#             stack.pop()

#     while stack:
#         top_element = stack[-1]
#         if top_element != '(':
#             postfix.append(stack.pop())
#         else:
#             stack.pop()

#     return ' '.join(postfix)
  
# print(infix_to_postfix("a-b / c*d % e"))


def infix_to_postfix(infix):
    stack = []
    postfix = ""
    operators = set(['+', '-', '*', '/', '(', ')'])

    for char in infix:
        if char not in operators:
            postfix += char
        elif char == '(':
            stack.append('(')
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()  # pop '('
        else:
            while stack and precedence(char) <= precedence(stack[-1]):
                postfix += stack.pop()
            stack.append(char)

    while stack:
        postfix += stack.pop()

    return postfix


def precedence(op):
    if op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/':
        return 2
    return 0


if __name__ == "__main__":
    infix = input("Enter an infix expression: ")
    postfix = infix_to_postfix(infix)
    print("Postfix expression:", postfix)