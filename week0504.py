# 561
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        ret = 0
        for i in range(len(nums)/2):
            ret += nums[i*2]
        
        return ret

# 2160
class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        list_num = []
        while num > 0:
            list_num.append(num % 10)
            num //= 10

        list_num.sort()
        return (list_num[0] + list_num[1]) * 10 + list_num[2] + list_num[3]

# 905
class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n < 1:
            return nums

        ret = [-1] * n
        l, r = 0, n - 1
        
        for i in range(n):
            if nums[i] % 2 == 0:
                ret[l] = nums[i]
                l += 1
            else:
                ret[r] = nums[i]
                r -= 1
        
        return ret


# 977
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]
        
        nums.sort()
        return nums

# 349
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        n1 = len(nums1)
        n2 = len(nums2)
        i, j = 0, 0
        ret = []

        while i < n1 and j < n2:
            if nums1[i] == nums2[j]:
                ret.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return list(set(ret))


# 1509
class Solution(object):
    def minDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 4:
            return 0

        nums.sort()
        poss_diff1 = nums[n-1] - nums[3]
        poss_diff2 = nums[n-2] - nums[2]
        poss_diff3 = nums[n-3] - nums[1]
        poss_diff4 = nums[n-4] - nums[0]
        return min(poss_diff1, poss_diff2, poss_diff3, poss_diff4)

# 1684
class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        count = 0
        allowed_set = set(allowed)
        for word in words:
            word_set = set(word)
            if word_set.issubset(allowed_set):
                count += 1
        
        return count
                

# 228
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        n = len(nums)
        ret = []
        l, r = 0, 0
        def str_gen(l,r):
            if l == r:
                return(str(nums[l]))
            else:
                return(str(nums[l]) + "->" + str(nums[r]))

        for i in range(n):
            if i + 1 < n:
                if nums[i+1] == nums[i] + 1:
                    r = i + 1
                else:
                    ret.append(str_gen(l,r))
                    l = i + 1
                    r = i + 1
            else:
                ret.append(str_gen(l,r))
        
        return ret



# 821
class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        n = len(s)
        ret = [n] * n
        dist = n

        for i in range(n):
            if s[i] == c:
                dist = 0
                ret[i] = dist
            else:
                dist += 1
                ret[i] = min(dist, ret[i])
        
        dist = n
        for i in range(n-1, -1, -1):
            if s[i] == c:
                dist = 0
            else:
                dist += 1
                ret[i] = min(dist, ret[i])
        
        return ret


# 56
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key = lambda x:x[0])
        ret = [intervals[0]]
        n = len(intervals)

        if n == 1:
            return ret

        for i in range(1, n):
            last_interval = ret[-1]
            if last_interval[1] < intervals[i][0]:
                ret.append(intervals[i])
            else:
                last_interval[1] = max(last_interval[1], intervals[i][1])
                ret[-1][1] = last_interval[1]

        return ret

