input_data = list(map(int, input().split()))
chet_number = []
for num in input_data:
    if el % 2 == 0:
        chet_number.append(num)
print(sum(chet_number), sum(input_data) - sum(chet_number))