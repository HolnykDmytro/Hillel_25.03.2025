print("Hello!")
digit = int(input("Enter 5 digit: "))

int1 = digit // 10000
zalishok = digit % 10000
int2 = zalishok // 1000
zalishok = zalishok % 1000
int3 = zalishok // 100
zalishok = zalishok % 100
int4 = zalishok // 10
int5 = zalishok % 10

revers_digit = int5 * 10000 + int4 * 1000 + int3 * 100 + int2 * 10 + int1
print(revers_digit)