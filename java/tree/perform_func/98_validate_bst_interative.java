/**
in a interative way
highlight: condition about when to stop
**/
class Solution {
    Integer pre = null;
    public boolean isValidBST(TreeNode root) {
        Deque<TreeNode> stack = new ArrayDeque<>();
        
        TreeNode pre = null;
        // the next to be interated
        TreeNode next = root;
        while(!stack.isEmpty() || next != null){
            // add it's self all the left subtree node in 
            while(next != null){
                stack.addFirst(next);
                next = next.left;
            }
            
            // pop the latest pushed, compare, and set the next one to be added in as right
            next = stack.pollFirst();
            if(pre != null && pre.val >= next.val){
                return false;
            }
            pre = next;
            next = next.right;
        }
        
        return true;
    }
    
    
}