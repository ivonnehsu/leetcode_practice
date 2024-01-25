'''860.柠檬水找零

'''
class Solution(object): # my sol
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        wallet = [0,0,0] #5,10,20
        for i in bills:
            print(wallet)
            if i==5:
                wallet[0]+=1
            elif i==10:
                if wallet[0]==0:
                    return False
                wallet[0]-=1
                wallet[1]+=1
            else:
                if wallet[0]==0 or (wallet[0]<3 and wallet[1]==0):
                    return False
                if wallet[1]>0: # -5, -10
                    wallet[0]-=1
                    wallet[1]-=1
                    wallet[2]+=1 #可以省略
                else: # -5*3
                    wallet[0]-=3
                    wallet[2]+=1 #可以省略
        return True


'''406.根据身高重建队列

'''
class Solution(object): # my sol
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        new_people = list()
        people.sort(key=lambda x: (-x[0],x[1])) #按[0]递减，[1]递增
        for i in people:
            new_people.insert(i[1],i)
        return new_people


'''452. 用最少数量的箭引爆气球

'''
class Solution(object): # my sol
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key=lambda x: x[0])
        print(points)
        total = 0
        if len(points)==1: return 1
        for i in range(1,len(points)):
            if points[i][0]<=points[i-1][1]:
                points[i] = [points[i][0],min(points[i-1][1],points[i][1])]
            else:
                total+=1
        return total+1 #z最后一个


class Solution: #答案
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 0: return 0
        points.sort(key=lambda x: x[0])
        result = 1
        for i in range(1, len(points)):
            if points[i][0] > points[i - 1][1]: # 气球i和气球i-1不挨着，注意这里不是>=
                result += 1     
            else:
                points[i][1] = min(points[i - 1][1], points[i][1]) # 更新重叠气球最小右边界
        return result

class Solution: # 不改变原数组 答案
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[0])
        sl,sr = points[0][0],points[0][1]
        count = 1
        for i in points:
            if i[0]>sr:
                count+=1
                sl,sr = i[0],i[1]
            else:
                sl = max(sl,i[0])
                sr = min(sr,i[1])
        return count