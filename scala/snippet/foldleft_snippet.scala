package org.gef
case class Person(val name:String, val money:Int)
object Solution {
  def main(args: Array[String]): Unit = {
    val map1 = Map((1,3),(4,5))
    val map2 = Map((2,4))
    val map3 = map1.foldLeft(map2){
          // map here is map2
      case (map, a) => {
        val map2 = map+(a._1->a._2)
        map2
      }
    }
    println(map3)
    //Map(2 -> 4, 1 -> 3, 4 -> 5)
    val arr = Array(1,2,3,4,5,6)
    println(arr.foldLeft(0){_+_}) // 21
    println(arr.foldLeft(0)((a,b)=>{a+b})) // 21
  }
}