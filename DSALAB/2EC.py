

class DFS:
    def __init__(self):
        self.v = 6
        self.visited = []
        self.prev = []
        self.s = 0
        self.time=0
        self.start=[]
        self.finish=[]
        self.G= []
        self.sst = 0

    def take_input(self):
        file=open('input.txt','r')
        for line in file:
            line=line.strip()
            adjacentVertices = []
            first=True
            for node in line.split(' '):
                if first:
                    first=False
                    continue
                adjacentVertices.append(int(node))
            self.G.append(adjacentVertices)
        file.close()
        print(self.G)
        self.s = int(input("enter the source vertex \n"))
        self.lists = [[]*1 for _ in range(self.v)]
        self.prev = [[]*1 for _ in range(self.v)]
        self.visited = [[0]*1 for _ in range(self.v)]
        self.start = [[0]*1 for _ in range(self.v)]
        self.finish = [[0]*1 for _ in range(self.v)]
        self.distance = [[]*1 for _ in range(self.v)]
        return self.v,self.s

    def do_dfs(self, u):
        self.visited[u]=1
        self.start[u]=self.time
        self.time = self.time+1
        self.sst = self.start[u]
        
        for v in self.G[u]:
            if(self.visited[v]!=1):
                self.prev[v] = u
                self.sst = min(self.do_dfs(v),self.sst)
                
            elif(v!=self.prev[u]):
                self.sst = min(self.start[v],self.sst)
                print(self.sst)

        self.finish[u] = self.time
        self.time = self.time+1
        if(self.sst==self.start[u] and self.start[u]!=0):
            print("There is a bridge so it is not 2 way connected ")
            print(x.start)
            exit(0)
        else:
            print("It is two way connected")
        return self.sst




x = DFS()
n,s = x.take_input()
x.do_dfs(s)
