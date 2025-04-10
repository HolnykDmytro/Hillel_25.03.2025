import random
lst = []
for x in range(random.randint(3, 10)):
    lst.append(random.randint(1, 10))
print(lst)
x = (lst[0])
y = (lst[2])
q= (lst[-2])

new_lst = []
new_lst.extend([x])
new_lst.extend([y])
new_lst.extend([q])
print(new_lst)