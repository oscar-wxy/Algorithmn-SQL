// ListBuffer can be used to create multi demension list
// sort a array
object Solution {
    def threeSum(unsorted: Array[Int]): List[List[Int]] = {
        var res = scala.collection.mutable.ListBuffer[List[Int]]();
        val nums = unsorted.sorted
        for(i<- 0 to nums.length-1){
            if(i==0 || nums(i)!=nums(i-1)){
                // use a while loop to find it
                var j = i+1
                var k = nums.length - 1
                val target = -nums(i)
                // assumption is: deduplicated when the while loop starts
                while(j<k){
                    // println(s"${nums(i)},${nums(j)},${nums(k)}")
                    if(nums(j)+nums(k)==target){
                        res+=(List(nums(i), nums(j), nums(k)))
                        while(j<nums.length-1 && nums(j+1)==nums(j)) j+=1
                        while(k>0 && nums(k-1)==nums(k)) k-=1
                        j+=1
                        k-=1
                    }
                    else if(nums(j)+nums(k)>target){
                        // while(j<nums.length-1 && nums(j+1)==nums(j)) j+=1
                        // j+=1
                        while(k>0 && nums(k-1)==nums(k)) k-=1
                        k-=1
                    }
                    else{
                        // while(k>0 && nums(k-1)==nums(k)) k-=1
                        // k-=1
                        while(j<nums.length-1 && nums(j+1)==nums(j)) j+=1
                        j+=1
                    }
                }
            }
        }
        res.toList
    }
}