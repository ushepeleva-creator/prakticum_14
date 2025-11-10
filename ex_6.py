del_number = []
number = int(input())
for n in range(1, int(((number) ** 0.5) + 1)):
    if number % n == 0:
        del_number.append(n)
        del_number.append(number // n)
print(*sorted(set(del_number)))