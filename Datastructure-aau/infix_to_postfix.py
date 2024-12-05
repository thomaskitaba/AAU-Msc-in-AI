#!/usr/bin/python3
def infix_to_postfix(infix):
    priority = {
        ')': 0,
        '(': 0,
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '^': 3,
        '**': 3
    }
    
    stack = []
    postfix = []
    
    
    #todo: rule
    # 1. no two operands with z same priority can stay together
    # 2. operator with lowest prority can not be placed above high priority operator 
    # 3. when )  is incountered  pop everything until (,  and append the operatnds to postfix ( *  +   not allowed)
    # infix =  "(a+(b*c))"
   
    for e in infix:
       if e in priority: # means e is an operator
            if e == '(':
               stack.append(e)
            elif e == ')':
                while stack and priority[stack[-1]] >= priority[e] and stack[-1] != '(':
                    postfix.append(stack.pop())
                stack.pop()
            else:
                while stack and priority[stack[-1]] >= priority[e] and stack[-1] != '(':
                    postfix.append(stack.pop())
                stack.append(e)
       else:
           postfix.append(e)
    
    while stack:
        postfix.append(stack.pop())
    return postfix
       
if __name__ == "__main__":
    infixs = [
        "(a + (b * c))",          # Output: abc*
        "(a + b) * c",          # Output: ab+c*
        "((a + b) * c) + d",        # Output: ab+c*d+
        "((a + (b * c)) + (d * e)) + f",    # Output: abc*+de*+f+
        "((a + b) * c + d) * e",     # Output: ab+c*d+e*
        "(((a + (b * c)) + d) * e + f) * g",  # Output: abcd*+e*f+g*
        "((a + b) * c + (d * e)) * f",   # Output: ab+c*de*+f*
        "(((a + (b * c)) + (d * e)) * g + h)", # Output: abc*+de*f+g*+h*
    ]
    
    for infix in infixs:
        result = ''.join(infix_to_postfix(infix))
        print(result.replace(" ", ""))
        
        # print(''.join(infix_to_postfix(infix)))
        