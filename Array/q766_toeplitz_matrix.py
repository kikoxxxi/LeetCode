class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for r in range(len(matrix) - 1):
            for c in range(len(matrix[0]) - 1):
                if matrix[r][c] != matrix[r + 1][c + 1]:
                    return False
        return True


def main():
    solution = Solution()
    matrix = [[0, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
    print(solution.isToeplitzMatrix(matrix))


main()
