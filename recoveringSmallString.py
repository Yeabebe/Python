def recover_small_string(t, cases):
    for n in cases:      
        pos = [1, 1, 1]
        remaining = n - 3
        
        for i in [2, 1, 0]:
            add = min(25, remaining)
            pos[i] += add
            remaining -= add
  
        result = ''.join(chr(ord('a') + p - 1) for p in pos)
        print(result)

t = int(input())
cases = [int(input()) for _ in range(t)]

recover_small_string(t, cases)
