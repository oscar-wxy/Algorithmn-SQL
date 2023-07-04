

object LC7_reverse_integer {
  def main(args: Array[String]): Unit = {
    reverse(980)
  }

  def reverse(x: Int): Int = {
    // deal with negative int
    val strVal = if (x < 0) x.toString.tail else x.toString
    // reverse
    val reverseVal = strVal.reverse.toDouble * x.signum

    if (reverseVal.isValidInt) reverseVal.toInt else 0

  }
}
