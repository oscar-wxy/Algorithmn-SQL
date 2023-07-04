/*
DFS:
        []
[2]     [3]     [6]     [7]
/|\
[2] [3]...

for each level, it has to be equals or greater than last level, 
and after finishing this level, need backtracking

include previous better version at the bottom
**/


class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        
        // sort it in ascding order
        ascdingSort(candidates);
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        return dfs(candidates, target, new ArrayList<>(), result);
    }
    
    public List<List<Integer>> dfs(int[] candidates, int target, List<Integer> current, List<List<Integer>> result){
        int leastValueIndex = getLeastValueIndex(current, candidates);
        
        for(int i = leastValueIndex; i < candidates.length; i++){
            // when to add a value and avoid continuing
            if(sum(current) + candidates[i] == target){
                current.add(candidates[i]);
                result.add(copyList(current));
                // remove
                removeLastElement(current);
            }
            // skip if it's already bigger
            else if(sum(current) + candidates[i] > target){
                continue;
            }
            // keep dfs searching if it's smaller than that
            else{
                current.add(candidates[i]);
                dfs(candidates, target, current, result);
                // after this we need to remove it from current, backtracking
                removeLastElement(current);
            }
        }
        
        return result;
    }
    
    private int sum(List<Integer> li){
        int sum = 0;
        for(Integer ele : li){
            sum+=ele;
        }
        return sum;
    }
    public void ascdingSort(int[] candidates){
        //Todo
        Arrays.sort(candidates);
    }
    
    public int getLeastValueIndex(List<Integer> current, int[] candidates){
        if(current.size() == 0){
            return 0;
        }
        int val = current.get(current.size() - 1);
        int position = Arrays.binarySearch(candidates, val); 
        return position;
    }
    
    public List<Integer> copyList(List<Integer> li){
        return new ArrayList<>(li);
    }
    
    public void removeLastElement(List<Integer> li){
        li.remove(li.size() - 1);
    }
    
    // public int getValueByIndex(List<Integer> current), we need to know this..
     
}

/*
binary search array and return index:
int positon = Arrays.binarySearch(arrays, "fff"); 

List:
List.get(obj or index)
List.add(element)
list.remove(index)
list.size()
*/

/**
previous better version:

public class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        Arrays.sort(candidates);
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        getResult(result, new ArrayList<Integer>(), candidates, target, 0);
        
        return result;
    }
    
    private void getResult(List<List<Integer>> result, List<Integer> cur, int candidates[], int target, int start){
        if(target > 0){
            for(int i = start; i < candidates.length && target >= candidates[i]; i++){
                cur.add(candidates[i]);
                getResult(result, cur, candidates, target - candidates[i], i);
                cur.remove(cur.size() - 1);
            }//for
        }//if
        else if(target == 0 ){
            result.add(new ArrayList<Integer>(cur));
        }//else if
    }
}

Reason:
modify the target, to avoid the sum up in each loop, I waste so much time here
the if condition in the for(...) make it more simple

*/