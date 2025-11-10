list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
a, b = map(int, input().split())
part = list1[a - 1:b]
list2.extend(reversed(part))
del list1[a - 1:b]
print(*list1)
print(*list2)
