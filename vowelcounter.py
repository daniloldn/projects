def vcount (x):
    total = 0
    word = list(x)
    vowel = ["a", "e", "i", "o", "u"]
    for j in range(len(word)):
        for i in vowel:
            if word[j] == i:
                total = total + 1
                continue
            else:
                continue

    return total
print(vcount("picture"))
