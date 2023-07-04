/*

Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

Constraints:

1 <= nums.length <= 3 * 104
0 <= nums[i] <= 105

Don't make it difficult
**/


class Solution {
    public boolean canJump(int[] nums) {
        int furthest = 0;
        
        for(int i = 0; i < nums.length; i++){
            if(i > furthest){
                return false;
            }
            furthest = Math.max(furthest, i + nums[i]);
        }
        
        return true;
    }
}

/**
class Solution {
    public boolean canJump(int[] nums) {
        return jump(nums, new char[nums.length], 0);
    }
    
    private boolean jump(int[] nums, char[] flag, int start){
        if(start + nums[start] >= nums.length - 1){
            flag[start] = 'y';
            return true;
        }
        
        if(flag[start] == 'y'){
            return true;
        }
        
        if(nums[start] == 0 && start < nums.length - 1){
            flag[start] = 'n';
            return false;
        }
        // need to try to jump from all the element within the range of nums[i]
        for(int i = start + 1; i <= start + nums[start]; i++){
            if(jump(nums, flag, i)){
                return true;
            }
        }
        
        return false;
    }
}
*/