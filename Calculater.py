class Calculator():
    def add(self,num1,num2):
        return num1+num2
    def sub(self,num1,num2):
        return num1-num2
    def mul(self,num1,num2):
        return num1*num2
    def div(self,num1,num2):
        if num2 == 0:
            return  "Error: Division by zero is not allowed"
        return num1/num2
print(Calculator().add(1,2))
print(Calculator().sub(3,4))
print(Calculator().mul(3,4))
print(Calculator().div(3,0))