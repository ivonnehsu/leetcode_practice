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


class Solution: #标准
    def __init__(self):
        self.dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]] 
        
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[False]*n for _ in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                if visited[i][j] == False and grid[i][j] == '1':
                    res += 1
                    self.bfs(grid, i, j, visited)  # Call bfs within this condition
        return res

    def bfs(self, grid, i, j, visited):
        q = deque()
        q.append((i,j))
        visited[i][j] = True
        while q:
            x, y = q.popleft()
            for k in range(4):
                next_i = x + self.dirs[k][0]
                next_j = y + self.dirs[k][1]

                if next_i < 0 or next_i >= len(grid):
                    continue 
                if next_j < 0 or next_j >= len(grid[0]):
                    continue
                if visited[next_i][next_j]:
                    continue
                if grid[next_i][next_j] == '0':
                    continue
                q.append((next_i, next_j))
                visited[next_i][next_j] = True