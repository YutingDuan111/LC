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
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        
        return False


#3
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        strlen = len(s)
        if strlen <= 1:
            return strlen

        l,r = 0, 0
        charSet = set()
        maxLen = 1

        while r < strlen:
            c = s[r]
            if c not in charSet:
                maxLen = max(maxLen,(r-l+1))
            else:
                while c in charSet:
                    charSet.remove(s[l])
                    l += 1
            charSet.add(c)
            r += 1

        return maxLen
                

#5
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s
        
        maxLen=1
        maxStr = s[0]
        for i in range(len(s)-1):
            for j in range(i+1,len(s)):
                if j-i+1 > maxLen and s[i:j+1] == s[i:j+1][::-1]:
                    maxLen = j-i+1
                    maxStr = s[i:j+1]

        return maxStr


#12

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        s = []
        thousand = num // 1000 * 1000
        hundred = num - thousand
        hundred = hundred // 100 * 100
        dec = num - thousand - hundred
        dec = dec // 10 * 10
        sin = num - thousand - hundred - dec

        c = thousand / 1000
        s.append("M"*c)

        if hundred == 900:
            s.append('CM')
        elif hundred == 400:
            s.append('CD')
        elif hundred >= 500:
            hundred -= 500
            s.append('D')
            c = hundred / 100
            s.append('C'*c)
        else:
            c = hundred / 100
            s.append('C'*c)

        if dec == 90:
            s.append('XC')
        elif dec == 40:
            s.append('XL')
        elif dec >= 50:
            dec -= 50
            s.append('L')
            c = dec / 10
            s.append('X'*c)
        else:
            c = dec / 10
            s.append('X'*c)

        if sin == 9:
            s.append('IX')
        elif sin == 4:
            s.append('IV')
        elif sin >= 5:
            sin -= 5
            s.append('V')
            s.append('I'*sin)
        else:
            s.append('I'*sin)
            
        return ''.join(s)
        

#13
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        result = 0

        for i in range(len(s)):
            curr = roman[s[i]]
            if i+1 < len(s):
                next_val = roman[s[i+1]] 
            else:
                next_val = 0
            
            if curr < next_val:
                result -= curr
            else:
                result += curr
        
        return result

#17
# didn't understand the solution (backtracking)