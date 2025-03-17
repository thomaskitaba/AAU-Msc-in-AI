#!/usr/bin/python3
print("Thomas Kitaba")

class Calculator:
    count = 0
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.count += 1
        self.history = []
        
    def add(self, a, b):
        result = a + b
        self.history.append(result)
        return (a + b)

    def sub(self):
            return (self.x - self.y)
    
    def history(self):
        return self.history
    
val = Calculator(3, 3) #
print(f"val = {val.x}")

a, b = 1, 2
object_1 = Calculator()

sum = object_1.add(a, b)
print(sum)

diff = object_1.sub()
print(f"{diff}")
