/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }

 nice morris traversal guide, use it as inorder for this question
 https://www.cnblogs.com/AnnieKim/archive/2013/06/15/morristraversal.html
 */
class Solution {
    public void recoverTree(TreeNode root) {
        TreeNode pre = null;
        TreeNode first = null;
        TreeNode second = null;
        TreeNode tmp = null;
        
        while(root != null){
            if(root.left != null){
                // get the back tracking node to the current root
                tmp = root.left;
                while(tmp.right != null && tmp.right != root){
                    tmp = tmp.right;
                }
                
                // case for backtracking
                if(tmp.right == null){
                    tmp.right = root;
                    root = root.left;
                }
                // case for deconstruct
                else{
                    // do the logic as output
                    if(pre != null && pre.val > root.val){
                        // compare it
                        if(first == null){
                            first = pre;
                            second = root;
                        }
                        else{
                            second = root;
                        }
                        
                        // move node
                        //pre = root;
                        //root = root.right;
                        //tmp.right = null;
                    }
                    pre = root;
                    root = root.right;
                    tmp.right = null;
                }
            }
            else{
                // output, copy the logic above
              if(pre != null && pre.val > root.val){
                        // compare it
                        if(first == null){
                            first = pre;
                            second = root;
                        }
                        else{
                            second = root;
                        }
                        
                        // move node
                        //pre = root;
                        //root = root.right;
                        //tmp.right = null;
                    }
                pre = root;
                root = root.right;
            
            }
        }
        
        if(first!= null && second != null){
		    int t = first.val;
		    first.val = second.val;
		    second.val = t;
		}
        
        
    }
}