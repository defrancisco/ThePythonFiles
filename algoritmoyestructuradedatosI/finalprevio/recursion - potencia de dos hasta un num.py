def potenciadedoshastaunnum(n):
    if n == 0:
        return 1
    else:
        return 2 * potenciadedoshastaunnum(n-1)