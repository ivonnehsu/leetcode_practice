'''286. Walls and gates

'''
class Solution: #my sol, very slow run time but good memory？ 每个door都会重新跑一次空缺
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # trouble encoutering: to make sure that we only count a spot once for every door
        m = len(rooms)
        n = len(rooms[0])
        direction = [[0,-1],[0,1],[1,0],[-1,0]]

        def bfs(i,j):
            queue = deque()
            queue.append((i,j,0))
            visited = [[False]*n for _ in range(m)]
            while queue:
                x,y,step = queue.popleft()
                # print('x,y,step, ',x,y,step)
                for d in direction:
                    if not 0<=(x+d[0])<m:
                        continue
                    if not 0<=(y+d[1])<n:
                        continue
                    if rooms[x+d[0]][y+d[1]]==-1 or rooms[x+d[0]][y+d[1]]==0:
                        continue
                    if visited[x+d[0]][y+d[1]]:
                        continue
                    # print(x+d[0],y+d[1])
                    rooms[x+d[0]][y+d[1]]=min(rooms[x+d[0]][y+d[1]],step+1)
                    visited[x+d[0]][y+d[1]]=True
                    queue.append((x+d[0],y+d[1],step+1))

        for i in range(m):
            for j in range(n):
                if rooms[i][j]==0:
                    bfs(i,j)
        return rooms
        
import collections

class Solution: #online sol, better time complexity, add both first layer in. use size, to make sure that we do it by layers. m*n run time and 
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        emptyRoom = 2147483647
        wall = -1
        gate = 0
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        m = len(rooms)
        n = len(rooms[0])
        q = collections.deque()
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == gate:
                    q.append([i, j])

        distance = 0
        while q:
            size = len(q)
            distance += 1
            while size > 0:
                size -= 1
                room = q.popleft()
                x, y = room
                for dx, dy in dirs:
                    i, j = x + dx, y + dy
                    if 0 <= i < m and 0 <= j < n and rooms[i][j] == emptyRoom: #省了去重的过程 因为按照layer来 先到的肯定是小的距离
                        rooms[i][j] = distance
                        q.append([i, j])       


def wallsAndGates(self, rooms: List[List[int]]) -> None: #方法2  不用size
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return []
        r_size = len(rooms)
        c_size = len(rooms[0])
        q = collections.deque()
        for r in range(r_size):
            for c in range(c_size):
                if rooms[r][c] == 0:
                    q.append((r,c))
        dirs = [(-1,0),(0,-1),(1,0),(0,1)]
        while q:
            x, y = q.popleft()
            distance = rooms[x][y]+1
            for dx, dy in dirs:
                new_x, new_y = x+dx, y+dy
                if 0<=new_x<r_size and 0<=new_y<c_size and rooms[new_x][new_y] == 2147483647:
                    rooms[new_x][new_y] = distance
                    q.append((new_x, new_y))
        return rooms


class Solution: #my sol adjusted
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # trouble encoutering: to make sure that we only count a spot once for every door
        m = len(rooms)
        n = len(rooms[0])
        direction = [[0,-1],[0,1],[1,0],[-1,0]]
        INF = 2147483647

        queue = collections.deque()
        for i in range(m):
            for j in range(n):
                if rooms[i][j]==0:
                    queue.append((i,j))
        
        while queue:
            x,y = queue.popleft()
            # print(x,y)
            distance = rooms[x][y]+1
            for d in direction:
                x_next,y_next = x + d[0], y + d[1]
                # print('direction, ', x_next,y_next)
                if 0<=x_next<m and 0<=y_next<n and rooms[x_next][y_next]== INF:
                    rooms[x_next][y_next] = distance
                    queue.append((x_next,y_next))
        
        return rooms



'''1235. Maximum Profit in Job Scheduling

'''
class Solution(object): #my sol exceeded time limits
    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        combined = [[startTime[i],endTime[i],profit[i]] for i in range(len(profit))]
        combined.sort(key=lambda x: x[1])
        # print(combined)
        dp = [0]*(combined[-1][1]+1) # dp[0],dp[1]are both 1
        for i in range(len(endTime)):
            for j in range(2,combined[-1][1]+1):
                # print('combined[i][1],j',combined[i][1],j)
                if combined[i][1] <= j:
                    dp[j]=max(dp[j],dp[combined[i][0]]+combined[i][2])
                    # print(j,dp[j])
        return dp[-1]



# dp should be by job counts not by time 
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        combined = sorted(zip(startTime,endTime,profit),key=lambda x: x[1])
        print(combined[0])
        dp = [(0,0)] #end time, profit, we are adding to it in loops no need to do *len
        def binary(dp,start_time):
            left, right = 0, len(dp)-1
            while left <= right:
                mid = (left + right)//2
                if dp[mid][0]<= start_time:
                    left = mid+1 #end time 
                else:
                    right = mid-1
            return right
        print(range(len(endTime)))
        for i in range(len(endTime)):
            prev = binary(dp,combined[i][0]) #start time 2nd
            if dp[prev][1]+combined[i][2] > dp[-1][1]: #combined[2][i] is the profit for i
                dp.append((combined[i][1],dp[prev][1]+combined[i][2]))
        return dp[-1][1]


'''826. Most Profit Assigning Work

'''
class Solution: # my sol
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        project = sorted(zip(difficulty, profit), key = lambda x: x[0])
        worker = sorted(worker)
        cur = 0
        max_profit = 0
        total_profit = 0
        for i in worker:
            while cur < len(project) and project[cur][0] <= i:
                print(max_profit, project[cur][1])
                max_profit = max(max_profit,project[cur][1])
                cur+=1
            total_profit+=max_profit
        return total_profit


import bisect ## bisect solution / binary search

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        difficultyProfit = list(zip(difficulty, profit))
        difficultyProfit.sort()

        difficulty, profit = zip(*difficultyProfit)

        n = len(profit)
        dp = [0] * n
        for i in range(n):
            dp[i] = max(profit[i], dp[i - 1])

        result = 0
        for w in worker:
            index = bisect.bisect_right(difficulty, w) - 1
            if index < 0:
                continue
            
            result += dp[index]
        
        return result

'''1166. Design File System

'''
class TreeNode(object): # my sol TreeNodes so don't need to create one for each one
    def __init__(self,val=0):
        self.val = val
        self.child = defaultdict(TreeNode)

class FileSystem:

    def __init__(self):
        self.folder=TreeNode()

    def createPath(self, path: str, value: int) -> bool:
        if not path or path == '/':
            return False
        if not self.folder: return False
        paths = path.split('/')
        paths_main = deque(paths[1:-1])
        cur = self.folder
        while paths_main:
            p = paths_main.popleft()
            if p in cur.child:
                print('yes equal')
                cur = cur.child[p]
            else: return False
        if paths[-1] in cur.child: return False
        cur.child[paths[-1]]=TreeNode(val=value)
        return True

    def get(self, path: str) -> int:
        if not path or path == '/':
            return False
        if not self.folder: return False
        paths = path.split('/')
        paths_main = deque(paths[1:])
        cur = self.folder
        while paths_main:
            p = paths_main.popleft()
            if p in cur.child:
                cur = cur.child[p]
            else: return -1
        return cur.val



class FileSystem: #my sol without treenode. quick runtime but bad memory

    def __init__(self):
        self.folder=defaultdict(int)

    def createPath(self, path: str, value: int) -> bool:
        if not path or path == '/':
            return False
        path_lst = path.split('/')
        if path_lst[1:-1] and '/'+'/'.join(path_lst[1:-1]) not in self.folder: return False
        if path in self.folder: return False
        self.folder[path]=value
        return True

    def get(self, path: str) -> int:
        if not path or path == '/':
            return False
        if path in self.folder: return self.folder[path]
        else: return -1

'''1779. Find Nearest Point That Has the Same X or Y Coordinate

'''

class Solution: # my sol
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        points = [[a-x,b-y] for [a,b] in points]
        minimal = float('inf')
        idx = -1
        for x in range(len(points)):
            if points[x][0]==0 or points[x][1]==0:
                manhattan = abs(points[x][0]) + abs(points[x][1])
                if manhattan < minimal:
                    idx = x
                    minimal = manhattan
        return idx

'''1347. Minimum Number of Steps to Make Two Strings Anagram

'''
class Solution(object): # my sol
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        s_counter = Counter(s)
        t_counter = Counter(t)
        for i in s_counter:
            while s_counter[i]>0 and i in t_counter and t_counter[i]>0:
                s_counter[i]-=1
                t_counter[i]-=1
        return sum(s_counter.values())

# Python from online
class Solution(object): # or to use defaultdict(int)
    def minSteps(self, s, t):
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        # `ord(char)` is used to get the ASCII value of a character
        sum = 0
        for n in count:
            if n > 0:
                sum += n

        return sum


'''1094. Car Pooling

'''


'''317. Shortest Distance from All Buildings

'''


'''329. Longest Increasing Path in a Matrix

'''


'''224. Basic Calculator

'''

'''79. Word Search

'''



'''K means from scratch using numpy

'''
#import libraries
import pandas as pd
import numpy as np
import random as rd
import matplotlib.pyplot as plt

data = pd.read_csv('clustering.csv')
data.head()

# Step 1 and 2 - Choose the number of clusters (k) and select random centroid for each cluster

#number of clusters
K=3

# Select random observation as centroids
Centroids = (X.sample(n=K))
plt.scatter(X["ApplicantIncome"],X["LoanAmount"],c='black')
plt.scatter(Centroids["ApplicantIncome"],Centroids["LoanAmount"],c='red')
plt.xlabel('AnnualIncome')
plt.ylabel('Loan Amount (In Thousands)')
plt.show()

# Step 3 - Assign all the points to the closest cluster centroid
# Step 4 - Recompute centroids of newly formed clusters
# Step 5 - Repeat step 3 and 4

diff = 1
j=0

while(diff!=0):
    XD=X
    i=1
    for index1,row_c in Centroids.iterrows():
        ED=[]
        for index2,row_d in XD.iterrows():
            d1=(row_c["ApplicantIncome"]-row_d["ApplicantIncome"])**2
            d2=(row_c["LoanAmount"]-row_d["LoanAmount"])**2
            d=np.sqrt(d1+d2)
            ED.append(d)
        X[i]=ED
        i=i+1

    C=[]
    for index,row in X.iterrows():
        min_dist=row[1]
        pos=1
        for i in range(K):
            if row[i+1] < min_dist:
                min_dist = row[i+1]
                pos=i+1
        C.append(pos)
    X["Cluster"]=C
    Centroids_new = X.groupby(["Cluster"]).mean()[["LoanAmount","ApplicantIncome"]]
    if j == 0:
        diff=1
        j=j+1
    else:
        diff = (Centroids_new['LoanAmount'] - Centroids['LoanAmount']).sum() + (Centroids_new['ApplicantIncome'] - Centroids['ApplicantIncome']).sum()
        print(diff.sum())
    Centroids = X.groupby(["Cluster"]).mean()[["LoanAmount","ApplicantIncome"]]



# 2
import numpy as np

def k_means(X, k, max_iters=100, tol=1e-4):
    """
    Perform K-means clustering on the given data.

    Parameters:
    - X: numpy array, shape (n_samples, n_features)
        Input data.
    - k: int
        Number of clusters.
    - max_iters: int, optional (default=100)
        Maximum number of iterations.
    - tol: float, optional (default=1e-4)
        Tolerance to declare convergence.

    Returns:
    - centroids: numpy array, shape (k, n_features)
        Final cluster centers.
    - labels: numpy array, shape (n_samples,)
        Index of the cluster each sample belongs to.
    """

    # Randomly initialize centroids
    centroids = X[np.random.choice(len(X), k, replace=False)]

    for _ in range(max_iters):
        # Assign each data point to the nearest centroid
        labels = np.argmin(np.linalg.norm(X - centroids[:, np.newaxis], axis=2), axis=0)

        # Update centroids
        new_centroids = np.array([X[labels == i].mean(axis=0) for i in range(k)])

        # Check for convergence
        if np.linalg.norm(new_centroids - centroids) < tol:
            break

        centroids = new_centroids

    return centroids, labels

# Example usage
# Generate some random 2D data for testing
np.random.seed(42)
data = np.random.rand(100, 2)

# Set the number of clusters (k)
k = 3

# Run K-means clustering
centroids, labels = k_means(data, k)

# Print results
print("Final centroids:\n", centroids)
print("Cluster labels:\n", labels)