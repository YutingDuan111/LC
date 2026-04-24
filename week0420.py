#344
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        f, l = 0, len(s)-1
        while f < l:
            a = s[f]
            s[f] = s[l]
            s[l] = a
            f+=1
            l-=1

#9
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_str = str(x)
        x_inverse = x_str[::-1]
        if x_str == x_inverse:
            return True
        
        return False
    

#14
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ret = []
        length = len(strs)
        strs.sort(key = len)

        for i in range(len(strs[0])):
            c = strs[0][i]
            for j in strs:
                if j[i] != c:
                    return "".join(ret)
            ret.append(c)


#70
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1

        l = [-1]*(n+1)
        l[0] = 1
        l[1] = 1

        for i in range(2, n+1):
            l[i] = l[i-1] + l[i-2]

        return l[n]
    

#217



#3



#5



#12


#13


#17

