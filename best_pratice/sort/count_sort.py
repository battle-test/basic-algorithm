#Сортировка подсчётом
def counting_sort(array, max_val):
    m = max_val+1
    count = [0] * m
    for a in array:
        count[a] += 1
    i = 0
    c = []
    for a in range(m):
        for x in range(count[a]):
            c.append(a)
    # for a in range(m):
    #     for c in range(count[a]):
    #         array[i] = a
    #         i +=1
    return c

array = list(map(int, str(input())))
max_val = int(str(input()))
print(counting_sort(array=array, max_val=max_val))
