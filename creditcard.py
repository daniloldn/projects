def crd(x):
    i = 0
    num = ""
    y = list(str(x))
    if len(y) != 16:
        print("Credit card number is incorrect")
    for j in range(len(y)):
        if i < 12:
            num = num + "x"
            i = i + 1
            continue
        else:
            num = num + str(y[j])
            i = i + 1
            continue
    return num

print(crd(1234567890123456))
