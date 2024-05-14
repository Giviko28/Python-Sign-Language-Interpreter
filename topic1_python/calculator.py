class Calculator:
    def Add(num1, num2):
        return num1+num2
    def Subtract(num1, num2):
        return num1-num2
    def Multiply(num1, num2):
        return num1*num2
    def Divide(num1, num2):
        if (num2 == 0):
            print("hollup can't divide by zero")
            return
        return num1/num2
    
        