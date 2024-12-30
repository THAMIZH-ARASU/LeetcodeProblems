class Solution:
    def findClosestNumber(self, nums):
        return min(nums, key=lambda x: (abs(x), -x))
    
if __name__ == '__main__':
    solution = Solution()
    nums1 = [-4,-2,1,4,8]
    nums2 = [2,-1,1]
    print(solution.findClosestNumber(nums1)) # Output: 1
    print(solution.findClosestNumber(nums2)) # Output: 1