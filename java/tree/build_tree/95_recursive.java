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
 
 we use recursive solution to do this
 
 what we do in the current level:
 generate all the unique trees of following
 [1,2,3,4,5,6] =>
 
 for(i in [1,2,3,4,5,6]):
    generate all the unique trees which take 1,2,3,4,5,6 as the root
    1 -> (roots of [2,3,4,5,6])
    4 -> (roots in [5,6])
    4.left = (roots in [1,2,3]) 
 
 
 */
class Solution {
    public List<TreeNode> generateTrees(int n) {
        return generate(1, n);
    }
    
    private List<TreeNode> generate(int start, int end){
        List<TreeNode> res = new ArrayList<>();
        if(start > end){
            res.add(null);
            return res;
        }
        
      //  List<TreeNode> res = new ArrayList<>();
        for(int i = start; i <= end; i++){
            // generate all the unique trees whose root is i
            List<TreeNode> leftTrees = generate(start, i - 1);
            List<TreeNode> rightTrees = generate(i + 1, end);
            
            for(TreeNode left : leftTrees){
                for(TreeNode right : rightTrees){
                    TreeNode root = new TreeNode(i);
                    root.right = right;
                    root.left = left;
                    res.add(root);
                }
            }
        }
        
        return res;
    }
}