'''797. All Paths From Source to Target

'''
class Solution(object): # my sol
    def __init__(self):
        self.result = []
        self.path = [0]
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        if not graph: return []
        self.dfs(graph,0)
        return self.result
    def dfs(self,graph,cur):
        if self.path[-1]==len(graph)-1:
            self.result.append(self.path[:]) # 0 doesn't work
            return
        for i in graph[cur]:
            self.path.append(i)
            self.dfs(graph,i)
            self.path.pop() # 回溯



'''200. Number of Islands

'''
class Solution(object): # my sol, dfs
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        result = 0
        visited = [[0]*n for _ in range(m)]
        direction = [[0,1],[0,-1],[1,0],[-1,0]]

                
        def dfs(x,y):
            for d in direction:
                if 0<=x+d[0]<m and 0<=y+d[1]<n and grid[x+d[0]][y+d[1]]=='1' and visited[x+d[0]][y+d[1]]==0:
                    visited[x+d[0]][y+d[1]]=1
                    dfs(x+d[0],y+d[1])

        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1' and visited[i][j]==0:
                    print(['here'])
                    result+=1
                    dfs(i,j)
        return result

 
class Solution(object): #my sol, bfs
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        result = 0
        visited = [[0]*n for _ in range(m)]
        direction = [[0,1],[0,-1],[1,0],[-1,0]]
        queue = deque()
                
        def bfs(queue):
            while queue:
                x,y = queue.popleft()
                for d in direction:
                    if 0<=x+d[0]<m and 0<=y+d[1]<n and grid[x+d[0]][y+d[1]]=='1' and visited[x+d[0]][y+d[1]]==0:
                        visited[x+d[0]][y+d[1]]=1
                        queue.append((x+d[0],y+d[1]))

        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1' and visited[i][j]==0:
                    print(['here'])
                    result+=1
                    queue = deque()
                    queue.append((i,j))
                    bfs(queue)
        return result