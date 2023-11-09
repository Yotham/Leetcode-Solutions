class Solution(object):
    def backspaceCompare(self, s, t):
        
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        def noBackSpace(L):
            size = len(L)
            i = 0
            while i < size:
                if L[i] == '#' and i != 0:
                    L.pop(i-1)
                    i-=1
                    L.pop(i)
                    i-=1
                    size-=2
                elif L[i] == "#" and i == 0:
                    L.pop(i)
                    i-=1
                    size-=1
                i+=1
            return L

        s = list(s)
        t = list(t)
        s = noBackSpace(s)
        t = noBackSpace(t)
        print(s,t)
        if s == t:
            return True
        else:
            return False
            
            