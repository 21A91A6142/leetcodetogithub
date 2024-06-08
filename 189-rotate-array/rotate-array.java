class Solution {
    public void reverse(int arr[],int l,int r){
        int temp;
        while(l<r){
            temp=arr[l];
            arr[l]=arr[r];
            arr[r]=temp;
            l++;
            r--;
        }
    }
    public void rotate(int[] nums, int k) {
        k=k%nums.length;
        if(nums.length>1){
            reverse(nums,0,nums.length-1);
            reverse(nums,0,k-1);
            reverse(nums,k,nums.length-1);
        }
        
    }
}