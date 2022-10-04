def tribonacci(signature, n):
    s_array = signature
    i = 0
    while i <n:
        s_array.append(sum(s_array[i:i+3]))
        i = i+1
    return s_array[0:n]


tribonacci([1,1,1], 10)
