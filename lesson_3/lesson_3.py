
x = 7 > 3
y = 10 > 5 > 1
if x:
    print("True")
    if y:
        print("Inner if")
elif y:
    print("Second if")
else:
    print("False")

print("______")

x = 7 > 3
y = 10 > 5 > 1
if x and y:
    print("True")
    print("True_1")
else:
    print("False")

print("________________")

#x = int(input("Number: "))

#if x == 1:
    #result = print("True")
#else:
    #result = print("False")

#result = "True" if x == 1 else "False"

print(("___________________"))

x = 1
x = x + 1

lst = [1, 2.1, "3", [1, 2, 3]]
#lst.append(5)
lst.append([6,7,8])
lst.insert(10, 10)
lst.extend([6, 7, 8])
print(lst)

print("__________________________")

lst.remove(2.1)
element = lst.pop(0)
print(lst)
print(element)

print("________________________________")

lst = [1, 2.1, "3", [1, 2, 3]]
print("3" in lst)
print(3 in lst)
if "3" not in lst:
    print("True")

print("___________________________")

print(len(lst))

lst_res = lst + [0,9,8]
print(lst_res)

print("____________________________")

lst = [0, 1, 2, 3, 4, 5]

print(lst[1:4])
print(lst[:5])
print(lst[::-1])

print("____________________________")
from copy import deepcopy
lst = [1,2,[3,4]]
lst_1 = lst[:]

lst_1[-1].append(5)
print(lst)
print(lst_1)