list_first = list(map(int, input().split()))

if list_first.count(3) == 1:
    list_first.remove(3)
    print(list_first)
else:
    print("in the list more than one 3")
