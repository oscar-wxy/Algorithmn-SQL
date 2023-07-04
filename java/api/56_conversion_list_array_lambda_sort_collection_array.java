/**
How:
1. int[][] sort: Arrays.sort(intervals,(a,b)->(a[0]-b[0]));

2. List<List<Integer>> sort: Collections.sort(res, (a,b) -> (a.get(0) - b.get(0)));

3. convert int[] to List: ArrayList<String> list = new ArrayList<String>(Arrays.asList(strArray));
	通过Collections.addAll(arrayList, strArray)方式转换，根据数组的长度创建一个长度相同的List，
	然后通过Collections.addAll()方法，将数组中的元素转为二进制，然后添加到List中，这是最高效的方法
	
	ArrayList< String> arrayList = new ArrayList<String>(strArray.length);
	Collections.addAll(arrayList, strArray);

4. convert List to array: 
	List.toArray(new T[]) T has to be Object, so int don't work, Integer works, String work
	Integer[] -> int[] : can only for loop

5. build int[][] by List<List<>>:
	- for loop
	- //装入int数组
	List<int []> res=new ArrayList<>();
	for(int i=0;i<10;i++){
	    int []arr={i,i+1};
	    res.add(arr);
	}
	 
	//注意toArray（）方法的参数，是一个二维数组，行数为res的大小
	int [][]matrix=res.toArray(new int[res.size()][]);
*/
	class Solution {
    public int[][] merge(int[][] intervals) {
        List<List<Integer>> sortedList = getSortedList(intervals);
        List<List<Integer>> result = new ArrayList<>();
        
        for(List<Integer> interval : sortedList){
            // if result is empty, insert it
            if(result.size() == 0){
                result.add(new ArrayList<>(interval));
            }
            
            // [[], [ ]], it should be in order?
            int lastIntervalEnd = result.get(result.size() - 1).get(1);
            int newStart = interval.get(0);
            int newEnd = interval.get(1);
            
            // [[]]
            if(newEnd <= lastIntervalEnd){
                continue;
            }
            else if(newStart <= lastIntervalEnd){
                // modify the value of list?
                result.get(result.size() - 1).set(1, newEnd);
            }
            else{
                // how to initialize ArrayList value
                result.add(new ArrayList<>(interval));
            }
        }
        
        return convertTwoDListToArray(result);
        
    }
    
    private List<List<Integer>> getSortedList(int[][] intervals){
        // sort the array and convert it to List
        List<List<Integer>> res = new ArrayList<>();
        
        for(int[] arr : intervals){
           int first = arr[0];
           int second = arr[1];
            List<Integer> list = new ArrayList<>();
            list.add(first);
            list.add(second);
            res.add(list);
        }
        
        Collections.sort(res, (a,b) -> (a.get(0) - b.get(0)));
        
        return res;
       
    }
    
    private int[][] convertTwoDListToArray(List<List<Integer>> list){
        int[][] array = new int[list.size()][2];
        
        for(int i = 0; i < list.size(); i++){
            array[i][0] = list.get(i).get(0);
            array[i][1] = list.get(i).get(1);
        }
        
        return array;
    }
}

