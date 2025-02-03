class Solution {
    public int longestMonotonicSubarray(int[] nums) {
        int x=0,y=0;
        int c1=1,c2=1;
        for(int i=0;i<nums.length-1;i++){
            if (nums[i]<nums[i+1]){
                c1+=1;
            }
            else{
                c1=1;
            }
            if(c1>x){
                x=c1;
            }
        }
        for(int i=0;i<nums.length-1;i++){
            if (nums[i]>nums[i+1]){
                c2+=1;
            }
            else{
                c2=1;
            }
            if(c2>y){
                y=c2;
            }
        }
        if(x>y){
            return x;
        }
        else if(y>x){
            return y;
        }
        else if(x==0 && y==0){
            return c1;
        }
        else{
            return x;
        }
    }
}