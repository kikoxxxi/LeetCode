class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        max_count = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 0
        max_count = max(max_count, count)
        return max_count


def main():
    solution = Solution()
    nums = [1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1]
    print(solution.findMaxConsecutiveOnes(nums))


main()
