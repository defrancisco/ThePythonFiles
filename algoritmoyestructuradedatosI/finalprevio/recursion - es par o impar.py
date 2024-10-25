def esparoimpar(n):
    if n == 0:
        return "par"
    elif n == 1:
        return "impar"
    else:
        return esparoimpar(n-2)