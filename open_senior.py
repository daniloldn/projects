def open_or_senior(data):
    x = []
    for i,j in enumerate(data):
        if j[0] >= 55 and j[1] > 7:
            x.append('Senior')
        else:
            x.append('Open')
    print(x)
    return x


open_or_senior([(16, 23),(73,1),(56, 20),(1, -1)])
