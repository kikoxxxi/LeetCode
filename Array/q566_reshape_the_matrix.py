class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        original_row = len(nums)
        original_column = len(nums[0])
        list_nums = [n for i in nums for n in i]
        if r * c == original_row * original_column:
            return [list_nums[i * c:(i + 1) * c] for i in range(r)]
        else:
            return nums


def main():
    solution = Solution()
    nums = [[1, 2], [3, 4], [5, 6]]
    r, c = 2, 3
    print(solution.matrixReshape(nums, r, c))


main()
