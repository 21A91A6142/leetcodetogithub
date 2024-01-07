class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        int j=0,c=0;
        for(int i=31;i>=0;--i){
            if(((n>>j)&1)){
                c+=long(pow(2,i));
            }
            j+=1;
        }
        return c;
    }
};