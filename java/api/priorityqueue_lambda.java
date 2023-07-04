class Solution {
    public int findKthLargest(int[] nums, int k) {
        Queue<Integer> heap = new PriorityQueue<>((x,y)->x-y);

        for(int i=0; i<nums.length; i++){
            if(i<k){
                heap.offer(nums[i]);
            }
            else{
                if(nums[i] > heap.peek()){
                    heap.poll();
                    heap.offer(nums[i]);
                }
            }
        }
        return heap.peek();
    }
}