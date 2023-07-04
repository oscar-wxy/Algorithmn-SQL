/**
dfs medium 不会
思考为什么可以这样， 用集合图理解
【1，2，2】
dfs([], [], 0, [1,2,2])进行for循环时
i = 0:
    所有包含1的集合 dfs([[]], [1], 1, [1,2,2])
    
i = 1:
    所有不包含1的集合， 本层所有i的搜索都是不包含前面所有元素， 集合图理解 
*/


class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(nums);
        dfs(res, new ArrayList<>(), 0, nums);
        
        return res;
    }
    
    private void dfs(List<List<Integer>> res, List<Integer> current, int start, int[] nums){
        // add the current
        if(start <= nums.length){
            res.add(new ArrayList<>(current));
        }
        
        for(int i = start; i < nums.length; i++){
            // look into the element before nums[start], to see if this is the duplicate element
            // if it is, skip it
            if(i > start && nums[i] == nums[i - 1]){
                continue;
            }
            
            // if not then add it in current
            current.add(nums[i]);
            dfs(res, current, i + 1, nums);
            
            // before we move forward, back tracking
            current.remove(current.size() - 1);
        }
    }
}