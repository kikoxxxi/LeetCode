class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero_index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero_index] = nums[zero_index], nums[i]
                zero_index += 1
        return nums


def main():
    solution = Solution()
    nums = [0,1,3,1,2,0,0,0,1,2]
    print(solution.moveZeroes(nums))


main()
