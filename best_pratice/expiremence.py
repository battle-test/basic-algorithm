n = int(input())
array = []
current_count = 0
max_count = 0
for i in range(n):
    array.append(int(input()))
for i in array:
    if i > 0:
        current_count += 1
        if current_count > max_count:
            max_count = current_count
    else:
        current_count = 0
print(max_count)

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