class Solution {
    public boolean lemonadeChange(int[] bills) {
        int s=0,five=0,ten=0,twen=0,i=0;
        while(i<bills.length){
            if(bills[i]==5){
                five+=1;
            }
            else if(bills[i]==10 && five>=1){
                ten+=1;
                five-=1;
            }
            else if(bills[i]==20){
                if(ten>=1 && five>=1){
                    twen+=1;
                    ten-=1;
                    five-=1;
                }
                else if(ten<1 && five>=3){
                    five-=3;
                }
                else{
                    return false;
                }
            }
            else{
                return false;
            }
            i++;
        }
        //System.out.print(i);
        if(i==bills.length){
            return true;
        }
        else{
            return false;
        }
    }
}