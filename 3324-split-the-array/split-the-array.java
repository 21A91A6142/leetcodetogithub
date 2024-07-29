class Solution {
    public boolean isPossibleToSplit(int[] nums) {
        ArrayList<Integer> arr1=new ArrayList<>();
        ArrayList<Integer> arr2=new ArrayList<>();
        for(int i=0;i<nums.length;i++){
            if(!arr1.contains(nums[i])){
                arr1.add(nums[i]);
            }
            else if(!arr2.contains(nums[i])){
                arr2.add(nums[i]);
            }
            else{
                return false;
            }
        }
        return true;

    }
}