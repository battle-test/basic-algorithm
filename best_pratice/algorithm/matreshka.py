def matreshka(n):
    if n ==1:
        print("Матрёшечка")
    else:
        print("Верх матрёшки n=", n)
        matreshka(n-1)
        print("Низ матрёшки n=", n)

print(matreshka(5))