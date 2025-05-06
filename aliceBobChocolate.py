def alice_bob_chocolates(n, t):
    left = 0
    right = n - 1
    time_a = 0
    time_b = 0
    
    while left <= right:
        if time_a <= time_b:
            time_a += t[left]
            left += 1
        else:
            time_b += t[right]
            right -= 1
    
    alice_bars = left
    bob_bars = n - left
    return alice_bars, bob_bars

n = int(input())
t = list(map(int, input().split()))

a, b = alice_bob_chocolates(n, t)
print(a, b)
