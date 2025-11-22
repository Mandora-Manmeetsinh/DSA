# def infix_to_postfix(expression):
#     stack = []
#     postfix = []
#     precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
#     associativity = {'+': 'left', '-': 'left', '*': 'left', '/': 'left'}

#     for char in expression:
#         if char.isalnum():  
#             postfix.append(char)
#         elif char in precedence: 
#             while (stack and stack[-1] != '(' and
#                    (precedence[char] < precedence[stack[-1]] or
#                     (precedence[char] == precedence[stack[-1]] and associativity[char] == 'left'))):
#                 postfix.append(stack.pop())
#             stack.append(char)
#         elif char == '(':
#             stack.append(char)
#         elif char == ')':
#             while stack and stack[-1] != '(':
#                 postfix.append(stack.pop())
#             stack.pop()
#     while stack:
#         postfix.append(stack.pop())
#     return ''.join(postfix)

# result = infix_to_postfix(st)
# print("Postfix expression:", result)4

def splitprefixSuffix(categories , k) :
    dis_count = 0
    for i in range(1, len(categories)):
        pre = categories[:i]
        suf = categories[i:]
        common = set(pre) & set(suf)
        if len(common) > k:
            dis_count += 1
    print(dis_count)

if __name__ == '__main__' :
    categories = input()
    k = int(input())
    splitprefixSuffix(categories , k)

# Time complexity :- O(n^2) 
# Space complexity :- O(1)