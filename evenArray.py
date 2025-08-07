t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    wrong_even = 0
    wrong_odd = 0

    for i in range(n):
        if i % 2 != a[i] % 2:
            if i % 2 == 0:
                wrong_even += 1
            else:
                wrong_odd += 1

    if wrong_even != wrong_odd:
        print(-1)
    else:
        print(wrong_even)
