def correction_cal(mxnum, randnum):#correction function for when n is too large in the code generator
    w = 26 - mxnum
    q = (randnum - w) - 1
    return q

def correction_cal2 (snum, key):
    t = key -(snum)
    s = 27 - t
    return s
