#!/usr/bin/python3

def infix_to_postfix(infix):
    priority = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '^': 3,
        '**': 3
    }
    stack = []  
    print(infix)

if __name__ == "__main__":
     
    postfix = []
    infix =  "(a+(b*c))"
    infix_to_postfix(infix)