def decode_string(b):
    r = sorted(set(b))
    
    mapping = {}
    length = len(r)
    for i in range(length):
        mapping[r[i]] = r[length - 1 - i]
    decoded = ''.join(mapping[ch] for ch in b)
    return decoded

t = int(input())
for _ in range(t):
    n = int(input())
    b = input()
    result = decode_string(b)
    print(result)
