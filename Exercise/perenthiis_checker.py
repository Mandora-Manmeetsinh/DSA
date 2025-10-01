def perenthisis_checker(exp) :
    n = len(exp)
    stack = []

    for i in range(n) :
        if exp[i] == '(' or exp[i] == '{' or exp[i] == '[':
            stack.append(exp[i])
        elif exp[i] == ')' or exp[i] == '}' or exp[i] == ']':
            if len(stack) == 0:
                return False
            stack.pop()

    if len(stack) == 0 :
        return "perenthisis are balanced"
    else :
        return "perenthisis are not balanced"
    
print(perenthisis_checker("({}{(()})"))