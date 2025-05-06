def min_deletions(s, ch):
    l, r = 0, len(s) - 1
    deletions = 0
    while l < r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        elif s[l] == ch:
            l += 1
            deletions += 1
        elif s[r] == ch:
            r -= 1
            deletions += 1
        else:
            return float('inf')  
    return deletions

def solve(test_cases):
    for n, s in test_cases:
        if s == s[::-1]:
            print(0)
            continue
        min_ops = float('inf')
        for ch in set(s):
            ops = min_deletions(s, ch)
            min_ops = min(min_ops, ops)
        print(min_ops if min_ops != float('inf') else -1)

t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    s = input().strip()
    test_cases.append((n, s))

solve(test_cases)
