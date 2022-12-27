#add
def add(num1,num2):
    return num1+num2
print("add")
#subtract
def sub(num1,num2):
    return num1-num2
print("subtract")
#muliply
def mul(num1,num2):
    return num1*num2
print("multiply")
#divide
def sub(num1,num2):
    return num1/num2
print("divide")
print ("Enter value")
while True:
    choice = input ("calculate (add/sub/mul/div:")
    num1 = int(input("fist digit:"))
    num2 = int(input("second digit:"))
if choice in ('add', 'sub', 'mul', 'div'):
    if choice == '1':
        print(num1, "+", num2, "=", add(num1,num2))
elif choice == '2':
    print(num1, "-",num2,"-",subtract(num1,num2))
elif choice == '3':
    print(num1, "*",num2,"-",subtract(num1,num2))
elif choice == '4':
    print(num1, "/",num2,"-",subtract(num1,num2))
else:
    print("Invalid")
