a = [1, 2, 3, 8, 9, 10, 15, 16, 17]

index_list = list()
for i in range(len(a)):
    if i == 0:
        index_list.append(i)
    else:
        if a[i] != a[i - 1] + 1:
            index_list.append(i)
print(index_list)
