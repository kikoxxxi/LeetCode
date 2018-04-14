class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        result = []
        odd = k + 1
        even = 1
        for i in range(k + 1):
            if i % 2 == 0:
                result.append(even)
                even += 1
            else:
                result.append(odd)
                odd -= 1
        result.extend(range(k + 2, n + 1))
        return result


def main():
    solution= Solution()
    n = 6
    k = 3
    print(solution.constructArray(n, k))


main()
