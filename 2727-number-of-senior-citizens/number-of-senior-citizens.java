class Solution {
    public int countSeniors(String[] details) {
        int c=0;
        for(int i=0;i<details.length;i++){
            if(details[i].charAt(11)=='6' && details[i].charAt(12)>='1'){
                c+=1;
            }
            else if(details[i].charAt(11)>'6'){
                c+=1;
            }
            //System.out.println((details[i].charAt(11)+""+details[i].charAt(12)));
        }
        return c;
    }
}