class Solution(object):
    def validateCoupons(self, code, businessLine, isActive):
        """
        :type code: List[str]
        :type businessLine: List[str]
        :type isActive: List[bool]
        :rtype: List[str]
        """
        def check(s):
            string="!@#$%^&*()+=.,/|"
            for i in string:
                if i in s:
                    return False
            return True

        k=[]    
        b=["electronics", "grocery", "pharmacy", "restaurant"]
        codes=zip(businessLine,code)
        final_code=zip(codes,isActive)
        final_code=sorted(final_code)
        for key,values in final_code:
            if key[0] in b and check(key[1]) and len(key[1])!=0 and values==True:
                k.append(key[1])
        return k

        