class Calculator:
    def __init__(self) -> None:
        pass
    def Add(self, num1, num2):
        return num1+num2
    def Subtract(self, num1, num2):
        return num1-num2
    def Multiply(self, num1, num2):
        return num1*num2
    def Divide(self, num1, num2):
        if (num2 == 0):
            print("hollup can't divide by zero")
            return
        return num1/num2
    
        