#!/usr/bin/python3
print("Thomas Kitaba")

def postfix_to_infix(data):
    stack = []
    operator = ['+', '-', '*', '/', '^', '**']
    
    for val in data:
        if (val in operator):
            if len(stack) >= 2:
                item = '(' + stack.pop() + val 
                # print(stack)
                item =  item + stack.pop() + ')'
                # print(stack)
                stack.append(item)
            else:
                return "Invalid Postfix"  
        else: 
            stack.append(val)
    print(stack[0])
    
    return ("----")

if __name__ == "__main__":
    
    postfix = [
    "abc*",          # Output: (a + (b * c))
    "ab+c*",          # Output: (a + b) * c
    "ab+c*d+",        # Output: ((a + b) * c) + d
    "abc*+de*+f+",    # Output: ((a + (b * c)) + (d * e)) + f
    "ab+c*d+e*",     # Output: ((a + b) * c + d) * e
    "abcd*+e*f+g*",  # Output: (((a + (b * c)) + d) * e + f) * g
    "ab+c*de*+f*",   # Output: ((a + b) * c + (d * e)) * f
    "abc*+de*f+g*+h*", # Output: (((a + (b * c)) + (d * e)) * g + h)
    "ab+cde*f+*g+",   # Output: (a + b) * ((d + (e * f)) * g)
    "ab+c*de*f+*",   # Output: ((a + b) * c + (d + (e * f)))
]

    for i in range(len(postfix)):
        result = postfix_to_infix(postfix[i])
        print(f'{result}-{i + 1}')

    