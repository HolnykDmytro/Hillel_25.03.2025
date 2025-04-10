lst = [1, 0, 4, 0, 42, 0, 7, 0]
new_lst = []
zero = 0
for x in lst:
    if x != 0:
        new_lst.append(x)
for zero in lst:
    if zero == 0:
        new_lst.append(zero)
print(new_lst)