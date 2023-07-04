class Solution {
    public boolean isPalindrome(int x) {
        if(x < 0){
            return false;
        }
        
        if (x == 0){
            return true;
        }
        
        String theInt = String.valueOf(x);
        
        for(int start = 0, end = theInt.length() - 1; start <= end; start++, end--){
            if(theInt.charAt(start) != theInt.charAt(end)){
                return false;
            }
        }
        
        return true;
    }
}

/***
String.valueOf, and String.length()
*/