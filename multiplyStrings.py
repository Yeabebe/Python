class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        result = [0] * (m + n)  

        # multiply digits from right to left
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                pos1, pos2 = i + j, i + j + 1

                # add to existing number at pos2
                total = mul + result[pos2]
                result[pos2] = total % 10
                result[pos1] += total // 10

        # skip leading zeros
        res_str = ''.join(map(str, result)).lstrip('0')
        return res_str if res_str else "0"
