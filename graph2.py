class Graph:
    def __init__(self):
        self.adj_list = {}
    def add_vertex(self,vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
    def printGraph(self):
        for vertex in self.adj_list:
            print(vertex , ':  ', self.adj_list[vertex])
            
    def addEdge(self,v1,v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    
    def removeEdge(self,v1,v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False
    
    
    def removeVertex(self,v1):
        if v1 in self.adj_list.keys():
            for otherVertex in self.adj_list[v1]:
                self.adj_list[otherVertex].remove(v1)
            del self.adj_list[v1]
            return True
        return False            
                
            
my_graph = Graph()
my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('S')

my_graph.addEdge('A','B')
my_graph.addEdge('C','B')
my_graph.addEdge('A','C')

# my_graph.removeEdge('A','S')

my_graph.removeVertex('A')
my_graph.printGraph()