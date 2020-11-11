class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        if (i < j):
            f = list(b)
            l = list(a)
            i = len(f) - 1
            j = len(l) - 1
        else:
            f = list(a)
            l = list(b)

        carry = 0
        ans = ""
        while (i >= 0 and j >= 0):
            if (int(f[i]) + int(l[j]) + carry == 3):
                ans = "1" + ans
                carry = 1
            elif (int(f[i]) + int(l[j]) + carry == 2):
                ans = "0" + ans
                carry = 1
            elif (int(f[i]) + int(l[j]) + carry == 1):
                ans = "1" + ans
                carry = 0
            elif (int(f[i]) + int(l[j]) + carry == 0):
                ans = "0" + ans
                carry = 0
            i = i - 1
            j = j - 1
        while (i >= 0):
            if (carry == 1):
                if (int(f[i]) + carry == 2):
                    ans = "0" + ans
                    carry = 1
                elif (int(f[i]) + carry == 1):
                    ans = "1" + ans
                    carry = 0
            else:
                ans = f[i] + ans
            i = i - 1
        if (carry == 1):
            ans = str(carry) + ans
        return ans


x = Solution()
print(x.addBinary("100", "110010"))
