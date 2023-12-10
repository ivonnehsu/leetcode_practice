import collections 
'''CONCEPTS 
通过下标访问数组中的元素
当需要判断这个元素是否出现过，我们就使用哈希表
hashcode
hashfunction = hashcode(name)%tablesize
common hash structures: 
    1. 数组：范围小  如果哈希值比较少、特别分散、跨度非常大，使用数组就造成空间的极大浪费
    2. set 集合：范围大, 空间，速度比数组大（单个）
    3. map 映射：有y值 dict？（有对应的数值）
'''


'''242.有效的字母异位词 

'''
class Solution(object):  # my solution
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_dict = collections.Counter(s)
        for i in t:
            if i in s_dict:
                s_dict[i]-=1
            else:
                return False
        print(s_dict)
        return True if all(s_dict[i]==0 for i in s_dict) else False #确认好用的逻辑词 all/any


# Counter 更简单的写法
class Solution(object):
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        a_count = Counter(s)
        b_count = Counter(t)
        return a_count == b_count
# 数组作为哈希表
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        record = [0] * 26
        for i in s:
            #并不需要记住字符a的ASCII，只要求出一个相对数值就可以了
            record[ord(i) - ord("a")] += 1 #unicode
        for i in t:
            record[ord(i) - ord("a")] -= 1
        for i in range(26):
            if record[i] != 0:
                #record数组如果有的元素不为零0，说明字符串s和t 一定是谁多了字符或者谁少了字符。
                return False
        return True
# defaultdict的写法
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict
        
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)
        for x in s:
            s_dict[x] += 1
        
        for x in t:
            t_dict[x] += 1
        return s_dict == t_dict
# temp = Solution()
# print(temp.isAnagram(s='ab',t='a'))



'''349. 两个数组的交集 


'''
class Solution(object): # my solution
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set1 = set(nums1)
        set2 = set(nums2)
        return [i for i in set1 if i in set2]

# 字典和集合 方法
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    # 使用哈希表存储一个数组中的所有元素
        table = {}
        for num in nums1:
            table[num] = table.get(num, 0) + 1
        
        # 使用集合存储结果
        res = set()
        for num in nums2:
            if num in table:
                res.add(num)
                del table[num]
        
        return list(res)

# 使用数组
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = [0]*1001
        count2 = [0]*1001
        result = []
        for i in range(len(nums1)):
            count1[nums1[i]]+=1
        for j in range(len(nums2)):
            count2[nums2[j]]+=1
        for k in range(1001):
            if count1[k]*count2[k]>0:
                result.append(k)
        return result

# 使用集合
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2)) #交集？
        
'''202. 快乐数

'''
class Solution(object): # my solution
    def __init__(self):
        self.sum_set = set() # 集合，set在这里用来排除是否有重复数（陷入循环）
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        new_number = 0
        for i in str(n):
            new_number+=int(i)**2
        if new_number in self.sum_set:
            return False 
        self.sum_set.add(new_number)
        return self.isHappy(new_number)


#使用集合 但是操作更简洁
class Solution:
    def isHappy(self, n: int) -> bool:        
        record = set()

        while True:
            n = self.get_sum(n)
            if n == 1:
                return True
            
            # 如果中间结果重复出现，说明陷入死循环了，该数不是快乐数
            if n in record:
                return False
            else:
                record.add(n)

    def get_sum(self,n: int) -> int: 
        new_num = 0
        while n: # 不断循环加个位数的平方值
            n, r = divmod(n, 10)
            new_num += r ** 2
        return new_num

# 集合方式2
class Solution:
   def isHappy(self, n: int) -> bool:
       record = set()
       while n not in record:
           record.add(n)
           new_num = 0
           n_str = str(n)
           for i in n_str:
               new_num+=int(i)**2
           if new_num==1: return True
           else: n = new_num
       return False

# 数组方式
class Solution:
   def isHappy(self, n: int) -> bool:
       record = []
       while n not in record:
           record.append(n)
           new_num = 0
           n_str = str(n)
           for i in n_str:
               new_num+=int(i)**2
           if new_num==1: return True
           else: n = new_num
       return False

# 精简数组
class Solution:
   def isHappy(self, n: int) -> bool:
       seen = []
       while n != 1:
           n = sum(int(i) ** 2 for i in str(n))
           if n in seen:
               return False
           seen.append(n)
       return True

'''1. 两数之和 

'''
class Solution(object): # my solution
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = defaultdict(int)
        for i in range(len(nums)): #可以用for index, value in enumerate(nums): 
            remain = target - nums[i]
            if remain in dic:
                return [dic[remain],i]
            else:
                dic[nums[i]] = i
        return None
#使用集合
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #创建一个集合来存储我们目前看到的数字
        seen = set()             
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [nums.index(complement), i]
            seen.add(num)