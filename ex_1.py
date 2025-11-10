rez = []
for number in range(10):
    rez.append(int(input()))
new_rez = []
for el in range(1, 9):
    new_rez.append(rez[el - 1] + rez[el + 1])
print(new_rez)

