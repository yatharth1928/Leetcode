class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        cnt={}
        if(len(s)!=len(t)):
            return False
        n=len(s)
        for i in range(n):
            cnt[s[i]]=cnt.get(s[i],0)+1
            cnt[t[i]]=cnt.get(t[i],0)-1
        
        for x in cnt:
            if cnt[x]!=0:
                return False
        return True
        