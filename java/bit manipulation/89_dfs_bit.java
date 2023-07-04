/**

位运算技巧：
某位变1: （1 << n） | number
某位变0: number & ~(1 << n)

better solution:
f(n) = G(f(n - 1))
**/
class Solution {
    public List<Integer> grayCode(int n) {
        Set<Integer> set = new HashSet<Integer>();
        List<Integer> res = new ArrayList<Integer>();
        set.add(0);
        res.add(0);
        dfs(res, set, n);

        return res;
    }
    
    public static boolean dfs(List<Integer> res, Set<Integer> set, int n){
        if(res.size() >> n == 1){
            return true;
        }
        // get the digits, and 0 ->1, 1->0
        int number = res.get(res.size() - 1);
        for(int i = 0; i < n; i++){
            int digit = ((1 << i) & number) >> i;
            int toChange = 1 - digit;
            System.out.println(toChange);
            // generate the newpublic List<Integer> grayCode(int n) {
            //
            //    }
            //}
            int next = toChange == 1 ? (toChange << i) | number : number & ~(1 << i);
            if(!set.contains(next)){
                res.add(next);
                set.add(next);
                if(dfs(res, set, n)){
                    return true;
                }
                res.remove(res.size() - 1);
                set.remove(next);
            }
        }

        return false;
    }
}