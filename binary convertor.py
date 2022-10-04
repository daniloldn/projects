
y = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]

def bicon(z):
    """this program converts decimal numbers into binary numbers"""
    bin = ""
    for i in y:
        max = z / i
        if max < 1:
            bin = bin + "0"
            continue
        elif max > 1:
            z = z - i
            bin = bin + "1"
            continue
        else:
            bin = bin + "1"
            return bin #breaks down the number in to all the numbers that divide into it
print(bicon(998))
