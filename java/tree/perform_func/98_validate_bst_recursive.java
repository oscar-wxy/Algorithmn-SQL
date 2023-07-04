/**
validare bst, recursive solution
use oop
maintain the val before, then inorder
**/

class Solution {
    Integer pre = null;
    public boolean isValidBST(TreeNode root) {
        if(root == null){
            return true;
        }
        
        if(!isValidBST(root.left)){
            return false;
        }
        
        if(pre != null  && root.val <= pre){
            return false;
        }
        
        pre = root.val;
        
        return isValidBST(root.right);
    }
    
    
}