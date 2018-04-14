class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        flag = True
        for num in nums:
            if nums[abs(num) - 1] < 0 and flag:
                res.append(abs(num))
                flag = False
            else:
                nums[abs(num) - 1] *= -1
                flag = True
        return res

    def deleteDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for num in nums:
            if nums[abs(num) - 1] > 0:
                nums[abs(num) - 1] *= -1
                res.append(abs(num))
        return res


def main():
    solution = Solution()
    nums = [1, 3, 3, 2, 1, 3, 3, 6, 2, 2, 2]
    print(solution.findDuplicates(nums))


main()
