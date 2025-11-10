text = list(map(int, input().split()))
command = input()
direction = command[0]
steps = int(command[1:]) % len(text)
if direction == 'R':
    result = text[-steps:] + text[:-steps]
elif direction == 'L':
    result = text[steps:] + text[:steps]
else:
    result = text
print(*result)
