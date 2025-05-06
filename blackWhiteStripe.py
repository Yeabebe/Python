def min_recolor(n, k, s):
    current_white = s[:k].count('W')
    min_white = current_white
    
    for i in range(k, n):
        if s[i - k] == 'W':
            current_white -= 1
        if s[i] == 'W':
            current_white += 1
        min_white = min(min_white, current_white)
    
    return min_white

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    result = min_recolor(n, k, s)
    print(result)
