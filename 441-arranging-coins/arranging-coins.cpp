class Solution {
public:
    int iscal(int k){
        return (k*(k+1))/2;
    }
    int arrangeCoins(int n) {
        int temp=n,i=1;
        int c=0;
        while(n>0){
            i=i+1;
            c=c+1;
            n=n-i;
        }
        return c;
    }
};