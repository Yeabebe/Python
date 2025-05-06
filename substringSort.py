def substring_sort(strings):
    strings.sort(key=lambda x: (len(x), x))

    for i in range(len(strings) - 1):
        if strings[i] not in strings[i + 1]:
            print("NO")
            return
    
    print("YES")
    for s in strings:
        print(s)

n = int(input())
strings = [input().strip() for _ in range(n)]

substring_sort(strings)
