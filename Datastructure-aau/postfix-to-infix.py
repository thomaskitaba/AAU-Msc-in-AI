#!/usr/bin/python3
print("Thomas Kitaba")

def postfix_to_infix(data):
    stack = []
    operator = ['+', '-', '*', '/', '^', '**']

    for val in data:
        if (val in operator):
            if len(stack) >= 2:
                operand2 = stack.pop()
                operand1 = stack.pop()                
                stack.append(f'{operand1}{val}{operand2}')
            else:
                return ["Invalid Postfix"] 
        else: 
            stack.append(val)
    # print(stack[0])
    if len(stack) > 1: 
        return ["invalid Postfix"]
    else:
        # print(stack[0])
        return stack[0]

if __name__ == "__main__":
    postfixs = [
        "abc*",          # (a + (b * c))
        "ab+c*",         # ((a + b) * c)
        "ab+c*d+",       # (((a + b) * c) + d)
        "abc*+de*+f+",   # (((a + (b * c)) + (d * e)) + f)
        "ab+c*d+e*",     # ((((a + b) * c) + d) * e)
        "abcd*+e*f+g*",  # (((((a + (b * c)) + d) * e) + f) * g)
        "ab+c*de*+f*",   # ((((a + b) * c) + (d * e)) * f)
        "abc*+de*f+g*+h*", # ((((((a + (b * c)) + (d * e)) * g) + h)))
        "ab+cde*f+*g+",  # (((a + b) * ((d + (e * f)) * g)))
        "ab+c*de*f+*",   # (((a + b) * c) + (d + (e * f)))
    ]

    for postfix in postfixs:
        result = postfix_to_infix(postfix)
        print(f"Postfix: {postfix} -> Infix: {result}")
        
    