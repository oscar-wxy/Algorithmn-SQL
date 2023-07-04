/***
We need to track the index for each ele

Two solution:
1. save the space, time=O(n)
2. Faster, but will use O(n) extra space 
*/
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++){
            map.put(nums[i], i);
        }
        
        for (int i = 0; i < nums.length; i++){
            int another  = target - nums[i];
            if(map.containsKey(another) && i != map.get(target - nums[i])){
                return new int[]{i, map.get(target - nums[i])};
            }
        }
        
         throw new IllegalArgumentException("No two sum solution");
        // return new int[]{};
    }
}

// build map
// map put / get
// return in the middle of the loop, how to avoid exception
// how to build an array