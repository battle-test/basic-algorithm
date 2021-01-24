def gen_bin(M, prefix=""):
    if M == 0:
        print(prefix)
        return
    else:
        gen_bin(M-1, prefix+"0")
        gen_bin(M-1, prefix+"1")

def generate_numbers(N:int, M:int, prefix=None):
    """Генерирует все числа (с лидидрующими незначащими нулями)
    в N-ричной системе счисления (N <= 10)
    длины М"""
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for digit in range(N):
        prefix.append(digit)
        generate_numbers(N, M-1, prefix)
        prefix.pop()

gen_bin(3)
#generate_numbers(4,3)