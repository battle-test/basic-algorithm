def f(n):
    assert n >=0, "Факториал не определён"
    if n == 0:
        return 1
    return f(n-1)*n

print(f(int(input())))
