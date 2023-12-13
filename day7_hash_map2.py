'''454.四数相加II 

'''
class Solution(object): #my solution
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        ans = 0
        numsum = defaultdict(int)
        for i in nums1:
            for j in nums2:
                sumij = i+j
                numsum[sumij]+=1

        for k in nums3:
            for l in nums4:
                if -(k+l) in numsum:
                    ans+=numsum[-(k+l)]
        return ans

#简洁写法
from collections import defaultdict 
class Solution:
    def fourSumCount(self, nums1: list, nums2: list, nums3: list, nums4: list) -> int:
        rec, cnt = defaultdict(lambda : 0), 0
        for i in nums1:
            for j in nums2:
                rec[i+j] += 1
        for i in nums3:
            for j in nums4:
                cnt += rec.get(-(i+j), 0) 
        return cnt

#hashmap
class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        # 使用字典存储nums1和nums2中的元素及其和
        hashmap = dict()
        for n1 in nums1:
            for n2 in nums2:
                hashmap[n1+n2] = hashmap.get(n1+n2, 0) + 1
        
        # 如果 -(n1+n2) 存在于nums3和nums4, 存入结果
        count = 0
        for n3 in nums3:
            for n4 in nums4:
                key = - n3 - n4
                if key in hashmap:
                    count += hashmap[key]
        return count
 

'''383. 赎金信 

'''
class Solution(object): # my solution
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        mag_dict = Counter(magazine)
        for i in ransomNote:
            if i in mag_dict:
                mag_dict[i]-=1
            else:
                return False
        return True if all(mag_dict[i]>=0 for i in mag_dict) else False

class Solution(object): # my solution
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        diff_dict = defaultdict(int)
        for i in magazine:
            diff_dict[i]+=1
        for i in ransomNote:
            diff_dict[i]-=1
        return True if all(diff_dict[i]>=0 for i in diff_dict) else False


'''15. 三数之和 

'''
class Solution15(object): # fixed my solution
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        nums.sort()
        print(nums)
        for i in range(len(nums)):
            if nums[i]>0: #这个逻辑应该些在for loop里
                return results

            if i>0 and nums[i] == nums[i-1]: 
                continue #改写后的if，continue
            # if i == 0 or (i >0 and nums[i]!=nums[i-1]):# 这一步应该直接写成一个小if， continue
            l = i+1
            r = len(nums)-1
            while l<r:
                result = nums[i]+nums[l]+nums[r]
                print(result, nums[i],nums[l],nums[r])


                # if result == 0 and [nums[i],nums[l],nums[r]] not in results:
                #     results.append([nums[i],nums[l],nums[r]])
                # elif result <0:
                #     while nums[l]==nums[l+1] and l+1<len(nums)-1:
                #         l+=1
                #     l+=1
                # else:
                #     while nums[r]==nums[r-1] and r-1>=0:
                #         r-=1
                #     r-=1
                # 改写，太复杂了
                # while loop的最后才去重跳过相同元素
                if result <0:
                    l +=1
                elif result >0:
                    r -=1
                else:
                    print(result)
                    results.append([nums[i],nums[l],nums[r]])

                    while r>l and nums[r]==nums[r-1]:
                        r-=1
                    while r>l and nums[l]==nums[l+1]:
                        l+=1
                    r-=1
                    l+=1


        return results       

temp = Solution15()
# print(temp.threeSum([0,0,0]))
# print(temp.threeSum([-2,-3,0,0,-2]))
print(temp.threeSum([-1,0,1,2,-1,-4]))
print('done')





'''18. 四数之和 
步骤：剪支，去重
'''
class Solution: # my solution
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums.sort() # sort() sort it in place, while sorted() return a new sorted list with the original unchanged. 
        for a in range(len(nums)-1): #this could be range(len(nums))
            if nums[a]>0 and nums[a]>target:
                return ans # break
            if a>0 and nums[a]==nums[a-1]:
                continue
            for b in range(a+1,len(nums)):
                if nums[a]+nums[b]>0 and nums[a]+nums[b]>target:
                    continue # break
                if b>a+1 and nums[b]==nums[b-1]:
                    continue
                c = b+1
                d = len(nums)-1
                while c < d:
                    temp_sum = nums[a] + nums[b]+nums[c]+nums[d]
                    if temp_sum < target:
                        c+=1
                    elif temp_sum > target:
                        d-=1
                    else:
                        ans.append([nums[a], nums[b],nums[c],nums[d]])
                        while c<d and nums[c]==nums[c+1]:
                            c+=1
                        while c<d and nums[d]==nums[d-1]:
                            d-=1
                        c+=1
                        d-=1
        return ans


# 字典法
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 创建一个字典来存储输入列表中每个数字的频率
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        # 创建一个集合来存储最终答案，并遍历4个数字的所有唯一组合
        ans = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    val = target - (nums[i] + nums[j] + nums[k])
                    if val in freq:
                        # 确保没有重复
                        count = (nums[i] == val) + (nums[j] == val) + (nums[k] == val)
                        if freq[val] > count:
                            ans.add(tuple(sorted([nums[i], nums[j], nums[k], val]))) 
                            #the Python set add() method adds a given element to a set if the element is not present in the set
                            #that's why we need to sort to make sure there's no duplicate
        return [list(x) for x in ans]