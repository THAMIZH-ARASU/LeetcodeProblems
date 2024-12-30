class Solution{
    public static int findClosestNumber(int[] nums){
        int minDistance = Integer.MAX_VALUE;

        for(int i = 0; i < nums.length; ++i){
            if(Math.abs(nums[i]) < Math.abs(minDistance)){
                minDistance = nums[i];
            }  
        }
        if(minDistance < 0 && presence(Math.abs(minDistance), nums)){
            return Math.abs(minDistance);
        }
        return minDistance;
    }

    public static boolean presence(int value, int[] nums){
        for(int num : nums){
            if (num == value){
                return true;
            }
        }
        return false;
    }
    
    public static void main(String args[]){
        int[] nums1 = {-4, -2, 1, 4, 8};
        int[] nums2 = {2, -1, 1};
        
        System.out.println(findClosestNumber(nums1));
        System.out.println(findClosestNumber(nums2));
    }
}