class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        f = list(map(int,a.split()))
        l = list(map(int,b.split()))

        i = len(f) - 1
        j = len(l) - 1
        carry = 0
        ans = ""
        while(i >= 0 and j >= 0):
            if(int(f[i])+ int(l[j]) + carry == 3):
                ans= "1" + ans
                carry = 1
            elif(f[i] + l[j]+ carry == 2):
                ans = "0" + ans
                carry = 1
            elif(f[i] + l[j] + carry == 1):
                ans= "1" + ans
                carry = 0
            elif(f[i] + l[j] + carry == 0):
                ans = "0" + ans
                carry = 0
            i = i- 1
            j = j -1
        ans = str(carry) + ans
        while(i >= 0):
            ans = f[i] + ans
            i = i -1
        return ans
