class Solution {
public:
    int numberOfSteps(int n) {
        int c=0;
        while(n){
            if(n&1){
                n=n^1;
                c+=1;
            }
            else{
                n=n>>1;
                c+=1;
            }
        }
        return c;
    }
};