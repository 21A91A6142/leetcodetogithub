class Solution {
    public static int subtraction(int n){
        int s=0;
        if(n%3==0){
            return 0;
        }
        while(true){
            s+=1;
            n-=1;
            if(n%3==0){
                break;
            }
        }
        return s;

    }
    public static int addition(int n){
        int s=0;
        if(n%3==0){
            return 0;
        }
        while(true){
            s+=1;
            n+=1;
            if(n%3==0){
                break;
            }
        }
        return s;

    }
    public int minimumOperations(int[] nums) {
        int s=0;
        for(int i:nums){
            s+=Math.min(addition(i),subtraction(i));
        }
        return s;
    }
}