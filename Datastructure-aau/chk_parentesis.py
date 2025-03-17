#!/usr/bin/python3
opening = ['(', '{', '[']
closing = [')', '}', ']']
stack = []

def check(test):
    for chr in test:
        if chr in opening:
            stack.append(chr)
        if chr in closing and opening.index(stack[-1]) == closing.index(chr):
            stack.pop()
        
    if len(stack) != 0:
        return False
    return True
# test = "( )(( )){([( )])}"	
test = "[ a + { b / ( c - d ) + e / (f + g ) } - h ]"
print(check(test))


