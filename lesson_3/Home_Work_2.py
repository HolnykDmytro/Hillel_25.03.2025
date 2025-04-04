def main_list(list1):
    if not list1:
        return [[], []]
    middle = (len(list1) + 1) // 2

    first_list = list1[:middle]
    second_list = list1[middle:]

    return [first_list, second_list]

print(main_list([]))
print(main_list([1, 2, 3, 4]))
print(main_list([1, 2, 3, 4, 5]))

