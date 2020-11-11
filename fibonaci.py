class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        fibSum = 0
        fibList = [0, 1]
        for i in range(2, N + 1):
            fibSum = fibList[i - 1] + fibList[i - 2]
            fibList.append(fibSum)

        return fibList


x = Solution()
print(x.fib(5))
