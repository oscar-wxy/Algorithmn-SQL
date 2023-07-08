package org.gef
case class Person(val name:String, val money:Int)
object Solution {
  def main(args: Array[String]): Unit = {

    val pairs = Array(
      ("a", 5, 1),
      ("c", 3, 1),
      ("b", 1, 3)
    )
    val b = pairs.sortWith {
       (a, b) => {
        if (a._3 == b._3) { //如果第三个字段相等，就按第一个字段降序
          a._1 > b._1
        } else {
          a._3 < b._3 //否则第三个字段降序
        }
      }
    }

    b.foreach(println)
    /*
    (c,3,1)
    (a,5,1)
    (b,1,3)
     */
    val people = Array(Person("a",1), Person("b", 20), Person("c", 10))
    val sortedPeople = people.sortWith((a,b)=>{
      a.money > b.money
    })
    sortedPeople.foreach(println(_))
  }
}