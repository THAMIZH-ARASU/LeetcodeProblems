class Solution:
    def findClosestNumber(self, nums):
        min_distance = 10 ** 5 + 1

        for i in range(len(nums)):
            if (abs(nums[i]) < abs(min_distance)):
                min_distance = nums[i]
        
        if (min_distance < 0 and (abs(min_distance) in nums)):
            return abs(min_distance)
        
        return min_distance


if __name__ == '__main__':
    solution = Solution()
    nums1 = [-4,-2,1,4,8]
    nums2 = [2,-1,1]
    print(solution.findClosestNumber(nums1)) # Output: 1
    print(solution.findClosestNumber(nums2)) # Output: 1