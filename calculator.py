def cal(x, y, z,):
    num1 = int(x)
    num2 = int(z)
    if str(y) == "+":
        return num1 + num2
    elif str(y) == "-":
        return  num1 - num2
    elif str(y) == "/":
        return num1 / num2
    else:
        return num1 * num2

print(cal(7,"+", 9))
