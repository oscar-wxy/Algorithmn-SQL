/**
[1,1,2,2,3]
[1, (1,2,2,3)], [2, [1,1,2,3]],
switch with the first element

note: after dfs, need to switch back 

*/

class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        // we need to sort this time
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(nums);
        
        dfs(result, new ArrayList<>(), nums, 0);
        return result;
    }
    
    private void dfs(List<List<Integer>> result, List<Integer> current, int[] nums, int start){
    // when to stop
        if(current.size() == nums.length){
            result.add(new ArrayList<>(current));
            return;
        }
        
     // start represent the next num to use
        Set<Integer> set = new HashSet<>();
        
        for(int i = start; i < nums.length; i++){
            // when to skip
            /*
            [1,1,2]
            **/
            if(!set.contains(nums[i])){
                // switch with start
                int startNum = nums[start];
                nums[start] = nums[i];
                nums[i] = startNum;
                
                set.add(nums[start]);
                
                current.add(nums[start]);
                dfs(result, current, nums, start + 1);
                current.remove(current.size() - 1);
                
                // following can be put in a function called (swap)
                startNum = nums[start];
                nums[start] = nums[i];
                nums[i] = startNum;
            }
        }
    }
}