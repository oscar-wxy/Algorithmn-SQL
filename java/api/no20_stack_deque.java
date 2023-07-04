/**
Use Deque to implement stack
Syntax:
Deque<Character> = new ArrayDeque<>();

API:
  1.添加元素
        addFirst(E e)在数组前面添加元素
        addLast(E e)在数组后面添加元素
        offerFirst(E e) 在数组前面添加元素，并返回是否添加成功
        offerLast(E e) 在数组后天添加元素，并返回是否添加成功

  2.删除元素
        removeFirst()删除第一个元素，并返回删除元素的值,如果元素为null，将抛出异常
        pollFirst()删除第一个元素，并返回删除元素的值，如果元素为null，将返回null
           removeLast()删除最后一个元素，并返回删除元素的值，如果为null，将抛出异常
        pollLast()删除最后一个元素，并返回删除元素的值，如果为null，将返回null
           removeFirstOccurrence(Object o) 删除第一次出现的指定元素
        removeLastOccurrence(Object o) 删除最后一次出现的指定元素
 3.获取元素
        getFirst() 获取第一个元素,如果没有将抛出异常
        getLast() 获取最后一个元素，如果没有将抛出异常
*/


class Solution {
    public boolean isValid(String s) {
        /**
        Stack
        [()] => [] √
        [(]=>[()]=>[] ... [] √
        [(] ] x
        */
        Deque<Character> dq = new ArrayDeque<>();
        
        for(int i = 0; i < s.length(); i++){
            char p = s.charAt(i);
            
            if(dq.isEmpty()){
                if(p=='(' || p=='{' || p=='['){
                    dq.addLast(p);
                }
                else{
                    return false;
                }
            }
            
            // if it;s not empty
            else{
                if(p=='(' || p=='{' || p=='['){
                    dq.addLast(p);
                }
                else{
                    if(p==')'){
                        if(dq.getLast()=='('){
                            dq.removeLast();
                        }
                        else{
                            return false;
                        }
                        
                    }
                    else if(p==']'){
                        if(dq.getLast()=='['){
                            dq.removeLast();
                        }
                        else{
                            return false;
                        }
                    }
                    else{
                        if(dq.getLast()=='{'){
                            dq.removeLast();
                        }
                        else{
                            return false;
                        }
                    }
                }
            }
        }
        
        return dq.isEmpty() ? true : false;
        
    }
}