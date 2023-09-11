import typing as ts
from collections import defaultdict

class Graph :
    v:int = 0;

    def __init__ (self,len:int) :
        self.v = len;
        self.vlist=[]
        for i in range(self.v):
            self.vlist.append(defaultdict(lambda:0))

    def addEdge (self,v1:int,v2:int,weight:int=1) :
        self.vlist[v1][v2]=weight;

    def addEdgeBi (self,v1:int,v2:int,weight:int=1) :
        self.addEdge(v1,v2,weight);
        self.addEdge(v2,v1,weight);


    def __repr__(self) :
        stl = []
        try:
            stl.append(f"Vertices |V| = {self.v}\n")
            for i in range(self.v) :
                stl.append(f'{i} : {dict(self.vlist[i])}')
            return "\n".join(stl)
        except ValueError :
            return ("Not initiated")


def depthFirst(g:Graph,src:int) :
    res:ts.List[int] = []
    visited:ts.List[bool]=[False]*g.v
    st = Stack(int)
    st.push(src)
    visited[src]=True
    while (not st.isEmpty()) :
        res.append(curr:= st.pop())
        visited[curr]=True
        for i in sorted(g.vlist[curr].keys(),reverse=True) :
            if visited[i] : continue
            st.push(i)
            visited[i]=True
    return res

def breadthFirst(g:Graph,src:int) :
    res:ts.List[int] = []
    visited:ts.List[bool]=[False]*g.v
    q = Queue(int)
    q.push(src)
    visited[src]=True
    while (not q.isEmpty()) :
        res.append(curr:= q.pop())
        for i in sorted(g.vlist[curr].keys()) :
            if visited[i] : continue
            q.push(i)
            visited[i]=True
    return res

def hasPath(g:Graph,src:int,des:int,visited=[]) :
    if not visited : visited = [False]*g.v
    visited[src]=True
    if (src==des) : return True
    for i in g.vlist[src] :
        if visited[i]: continue
        if hasPath(g,i,des,visited) :
            return True
    else:
        return False

def djikstra(g:Graph,src:int) :
    visited = [False]*g.v
    weights = [float("inf")]*g.v
    weights[src] = 0
    visited[src] = True
    q = []
    q.append(src)

    while (len(q)!=0) :
        q.sort(key=lambda x:weights[x])
        x = q.pop(0)
        visited[x] = True
        for i in g.vlist[x] :
            if visited[i]: continue
            distance = weights[x] + g.vlist[x][i]
            if distance<weights[i]:
                weights[i] = distance
            q.append(i)
    return weights


