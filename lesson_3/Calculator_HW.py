print("Enter action:")
print("1. +")
print("2. -")
print("3. *")
print("4. /")

action = input("Enter number of action (1, 2, 3, 4) : ")

num_1 = int(input("Enter num_1: "))
num_2 = int(input("Enter num_2: "))
if action == '1':
    print("res:", num_1 + num_2)
elif action == '2':
    print("res:", num_1 - num_2)
elif action == '3':
    print("res:", num_1 * num_2)
elif action == '4':
    if num_2 != 0:
        print("res:", num_1 / num_2)
    elif num_2 == 0:
        print("Error")

