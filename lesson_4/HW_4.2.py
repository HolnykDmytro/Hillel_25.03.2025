lst = [0, 3, 5, 9, 8, 4, 13]
lst_2 = lst[::2]
num = lst_2.pop()
#print(lst_2)
#print([num])

summa = 0
for element in lst_2:
    summa += element
    #print(summa)
result = summa * num
print(result)