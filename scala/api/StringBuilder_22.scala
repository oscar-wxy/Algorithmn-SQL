import scala.collection.mutable.ListBuffer

/*
StringBuilder.newBuilder is the constructor
delete the end param is exclusive
StringBuilder is not thread safe
StringBuffer is thread safe
*/
object Solution {
    def generateParenthesis(n: Int): List[String] = {
        var current = StringBuilder.newBuilder
        var result = ListBuffer[String]()
        generate(n,0,0,current,result)
        result.toList
    }

    def generate(n:Int, countOpen:Int, countClose:Int, current:StringBuilder, result:ListBuffer[String]): Unit = {
        if(countOpen==n && countClose==n){
            result+=current.toString
            return 
        }
        else if(countOpen==n){
            generate(n,countOpen,countClose+1,current.append(")"), result)
            current.delete(current.length-1,current.length)
            // println(current.toString)
        }
        else{
            if(countOpen>countClose){
                // println(current.toString)
                generate(n,countOpen,countClose+1,current.append(")"), result)
                current.delete(current.length-1,current.length)
            }
                
            
            generate(n,countOpen+1,countClose,current.append("("), result)
            current.delete(current.length-1,current.length)
        }
    }
}