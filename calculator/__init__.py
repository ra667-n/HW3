class MyCalculation:
    def __init__(self, x, y, operation):
        self.x = x
        self.y = y
        self.operation = operation

    def get_result(self):
        return self.operation(self.x, self.y)

    def add(a: int,b: int) -> int:
        return a + b

    def subtract(a,b):
        return a - b
 
    def multiply(a,b):
        return a * b

    #def divide(a,b) -> None:
        #if b == 0:
            #raise DivisionByZero("Cannot divide by zero")
        #return None

test = MyCalculation(1, 2, "add")
print(test.get_result())
