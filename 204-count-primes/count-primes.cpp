class Solution {
public:
    int countPrimes(int n) {
        vector<int>a;
        vector<bool>v(n+1,true);
        v[0]=0;
        v[1]=0;
        for(int i=2;i*i<n+1;i++){
            if(v[i]){
                for(int j=i*i;j<n+1;j=j+i){
                    v[j]=0;
                }
            }
        }
        int c=0;
        for(int i=2;i<n;i++){
            if(v[i]){
                c+=1;
            }
        }
        return c;
    }
};