'''总结

'''


'''332.重新安排行程

'''
class Solution(object): # my sol 超时
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        result=[]
        mapping = [False]*len(tickets)
        tickets.sort()
        self.backtracking(tickets,result,['JFK'],mapping,False)
        return result[0]
    def backtracking(self,tickets,result,path,mapping,state):
        if len(path)==len(tickets)+1:
            result.append(path[:])
            return True
        for i,ticket in enumerate(tickets):
            if ticket[0]==path[-1] and mapping[i]==False:
            # 因为是按顺序的，所以结果取第一个就好了
            # if i>0 and tickets[i][0]==tickets[i-1][0] and tickets[i][1]>tickets[i-1][1]:
                #     continue
                path.append(ticket[1])
                mapping[i]=True
                state = self.backtracking(tickets,result,path,mapping,state)
                mapping[i]=False
                path.pop()
                # if result:
                #     return result #这个result不会终止循环
                if state:
                    return True


from collections import defaultdict

class Solution: #标准 通过的答案
    def findItinerary(self, tickets):
        targets = defaultdict(list)  # 创建默认字典，用于存储机场映射关系
        for ticket in tickets:
            targets[ticket[0]].append(ticket[1])  # 将机票输入到字典中
        
        for key in targets:
            targets[key].sort(reverse=True)  # 对到达机场列表进行字母逆序排序
        
        result = []
        self.backtracking("JFK", targets, result)  # 调用回溯函数开始搜索路径
        return result[::-1]  # 返回逆序的行程路径
    
    def backtracking(self, airport, targets, result):
        while targets[airport]:  # 当机场还有可到达的机场时
            next_airport = targets[airport].pop()  # 弹出下一个机场
            self.backtracking(next_airport, targets, result)  # 递归调用回溯函数进行深度优先搜索
        result.append(airport)  # 将当前机场添加到行程路径中
'''51. N皇后

'''


'''37. 解数独

'''