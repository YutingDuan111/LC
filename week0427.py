#1
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}

        for i in range(len(nums)):
            left = target - nums[i]
            if left in dic:
                return [dic[left],i]
            dic[nums[i]] = i

#15
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        nums.sort()
        
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break

            j = i + 1
            k = len(nums) - 1
            
            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total == 0 and [nums[i], nums[j], nums[k]] not in ret:
                    ret.append([nums[i], nums[j], nums[k]])
                    j += 1 
                    k -= 1

                elif total < 0:
                    j += 1

                else:
                    k -= 1

        return ret
    
#27
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            if nums[0] == val:
                return 0
            else:
                return 1

        l, r, k = 0, 0, 0
        while r < len(nums):
            if nums[r] == val:
                while r < n and nums[r] == val:
                    r += 1
                    k += 1
                if r < n:
                    nums[l] = nums[r]
                r += 1
                l += 1
            else:
                nums[l] = nums[r]
                r += 1
                l += 1

        return n - k
    
# 31
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        
        if i == 0:
            nums.reverse()
            return
        
        j = len(nums) - 1
        while j >= i and nums[j] <= nums[i-1]:
            j -= 1
        
        nums[i-1], nums[j] = nums[j], nums[i-1]

        nums[i:] = reversed(nums[i:])

# 36
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for row in board:
            record = set()
            for num in row:
                if num == '.':
                    continue
                elif num in record:
                    return False
                else:
                    record.add(num)
        
        for i in range(9):
            record = set()
            for j in range(9):
                if board[j][i] == '.':
                    continue
                elif board[j][i] in record:
                    return False
                else:
                    record.add(board[j][i])
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                record = set()
                for x in range(3):
                    for y in range(3):
                        if board[i+x][j+y] == '.':
                            continue
                        elif board[i+x][j+y] in record:
                            return False
                        else:
                            record.add(board[i+x][j+y])

        return True
    
# 1512
class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        ret_val = 0
        
        unique_nums = set(nums)
        counts = Counter(nums)

        for num in unique_nums:
            n = counts[num]
            if n > 1:
                ret_val += n * (n-1) / 2
            
        return ret_val
    
# 1672
class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        ret = 0
        for i in accounts:
            wealth = sum(i)
            ret = max(ret, wealth)
        
        return ret

# 1480
# Subscription required

# 2574
class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)

        leftSum = [0] * n
        rightSum = [0] * n
        ret = [0] * n

        for i in range(1, n):
            leftSum[i] = leftSum[i-1] + nums[i-1]

        for i in range(n-2, -1, -1):
            rightSum[i] = rightSum[i+1] + nums[i+1]

        for i in range(n):
            ret[i] = abs(leftSum[i] - rightSum[i])

        return ret        

# 804
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        unique_code = set()

        table = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        for word in words:
            code = ''
            for c in word:
                index = ord(c) - ord('a')
                code += table[index]
            unique_code.add(code)

        return len(unique_code)
                

        
        
# tap water: https://colab.research.google.com/drive/1-G-VHDIVjMBveHbWL8I2tsgdJVMNRZdx#scrollTo=mrEXc0iLJ4cI
def solution(nums, tap):
  ret = [0] * len(nums)
  cur_bar = 0
  n = len(nums)

  def find_cur_bar(nums, i):
    if i == 0 or i == len(nums) - 1:
      return nums[i]
    return max(nums[i-1], nums[i], nums[i+1])

  for i in range(n):
    if i in tap:
      ret[i] = 1
      cur_bar = max(cur_bar, find_cur_bar(nums, i))
      continue
    if nums[i] >= cur_bar:
      cur_bar = 0
    else:
      ret[i] = 1


  for i in range(n-1, -1, -1):
    if i in tap:
      ret[i] = 1
      cur_bar = max(cur_bar, find_cur_bar(nums, i))
      continue
    if nums[i] >= cur_bar:
      cur_bar = 0
    else:
      ret[i] = 1

  return ret
    