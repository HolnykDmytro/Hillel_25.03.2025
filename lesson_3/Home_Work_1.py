lst = [1, 2, 3, 4, 5, 6]
lst = lst[-1:] + lst[:-1] if len(lst) > 1 else lst
print(lst)