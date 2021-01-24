def gcd(a, b):
    if a == b:
        return a
    elif a > b:
        return gcd(a - b, b)
    else:
        return gcd(a, b - a)


def gcd_1(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def gcd_2(a, b):
    return a if b == 0 else gcd(b, a % b)

length = int(input())
massive = []
max_count = 0
current_count = 0
for value in range(length):
    massive.append(int(input()))
for value in massive:
    if value == 1:
        current_count +=1
        if current_count > max_count:
            max_count = current_count
    else:
        current_count = 0
print(max_count)