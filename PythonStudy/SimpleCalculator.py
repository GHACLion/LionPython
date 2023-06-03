# Author：程序员良哥
# DateTime: 2023/3/6 16:32

# 简易计算器
"""
    这里 try / except 用法 类似于 java 中的 try / catch
"""

error = False

try:
    num1 = float(input("Please input the first number ："))
except:
    print("Type of The first number is Wrong !")
    error = True
try:
    num2 = float(input("Please input the second number : "))
except:
    print("Type of The second number is Wrong !")
    error = True

op = input("Please type in the operator (+ - * / **): ")
if error:
    print("Unknown Error")
else:
    if num2 == 0 and op == "/":
        print("The division can't be 0")
    elif op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "*":
        print(num1 * num2)
    elif op == "/":
        print(num1 / num2)
    elif op == "**":
        print(num1 ** num2)
    else:
        print("Unknown Operator")

print("End")
