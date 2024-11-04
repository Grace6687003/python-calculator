class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b    #chage  b-a to a-b

    def multiply(self, a, b):
        result = a*b
        return result
    
    # แก้ divided
    def divide(self, a, b):
        if b == 0 or a==0:
            return "Cannot divide by zero"
        
        result = 0
        while a >= b:
            a = self.subtract(a, b)
            result += 1
        return result
    
    def modulo(self, a, b):
        if b == 0 or a == 0:
            raise ValueError("Cannot divide by zero")

        while a >= b:
            a = a-b
        return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: division: ", calc.divide(10, 0))  #Can't divide by zero
    print("Example: modulo: ", calc.modulo(10, 3))
    # print("Example: modulo: ", calc.modulo(10, 0), ValueError)  #Can't modulo by zero
