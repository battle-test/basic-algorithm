import time

def pow(a, n):
    if n == 1:
        return a
    return pow(a, n - 1) * a

def pow_1(a, n):
    if n ==0:
        return 1
    elif n % 2 == 1:
        return pow(a,n-1)*a
    else:
        return pow(a**2,n//2)



a = int(str(input()))
n = int(str(input()))
print(time.time())
print(pow(a,n))
print(time.time())
print(pow(a,n))
print(time.time())