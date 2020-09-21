class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def sum(self):
        return self.num1 + self.num2
    
    def subtract(self):
        return self.num1 - self.num2
    
    def multiply(self):
        return self.num1 * self.num2
    
    def divide(self):
        return self.num1/self.num2


if __name__ == '__main__':
    calc = Calculator(6, 2) # num1 = 6, num2 = 2
    sumResult = calc.sum()
    subtractResult = calc.subtract()
    multiplyResult = calc.multiply()
    divideResult = calc.divide()
    print(f'덧셈결과 {sumResult}')
    print(f'뺄셈결과 {subtractResult}')
    print(f'곱셈결과 {multiplyResult}')
    print(f'나누셈결과 {divideResult}')