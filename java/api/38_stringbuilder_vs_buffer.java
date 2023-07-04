/**
Difference between string builder and stringbuffer

StringBuilder - good for single thread, higher performance
StringBuffer - good for multi thread

use builder.append()
*/

class Solution {
    public String countAndSay(int n) {
        if(n == 1){
            return "1";
        }
        
        else{
            int slow = 0;
            int fast = 0;
            
            String s = countAndSay(n - 1);
            
            // look into string buffer, string building ....
            StringBuilder result = new StringBuilder();
        
            // make sure, for any time, strng[slow, fast + 1] is the same group
            for(int i = 0; i < s.length(); i++){
                if(fast + 1 <= s.length() - 1 && s.charAt(fast + 1) == s.charAt(slow) ){
                    fast++;
                }
                else{
                    // get the sub string
                    int subLength = fast - slow + 1;
                    char subDigit = s.charAt(slow);
                    char subLengthChar = (char)('0' + subLength);
                     // s concat char
                
                    result.append(subLengthChar);
                    result.append(subDigit);
                    slow = fast + 1;
                    fast = fast + 1;
                }
            }
            
            return String.valueOf(result);
        }
    }
}