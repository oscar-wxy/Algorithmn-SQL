/*
pattern match how to use if
also another thought to use 
you can even do:
case _ if remainOpen==remainClose && expr
*/
object Solution {
    def generate(remainOpen:Int, remainClose:Int):List[String] = {
        (remainOpen, remainClose) match {
            case (0,0) => List("")
            case(0, remainClose) => List(")" * remainClose) // note
            // can only add "("
            case _ if remainOpen==remainClose => generate(remainOpen-1, remainClose).map("("+_)
            case _ if remainOpen<remainClose => generate(remainOpen-1, remainClose).map("("+_)++generate(remainOpen,remainClose-1).map(")"+_)
        }
    }
    def generateParenthesis(n: Int): List[String] = {
        generate(n,n)
    }
}