# Activity 01

class Graph:

    def __init__(self, size):
        self.matrix = []
        for i in range(size):
            self.matrix.append([0] * size)
        self.size = size
        
# Activity 01

    def addEdge(self, u, v):
        self.matrix[u][v] = 1
        self.matrix[v][u] = 1

    def isEdge(self, u, v):
        return self.matrix[u][v] == 1

# Activity 02

    def bfs(self, start):
        visited = set()
        line = [start]
        while line:
            u = line.pop(0)
            visited.add(u)
            for v in range(self.size):
                if self.matrix[u][v] == 1 and v not in visited:
                    line.append(v)
        print(visited)

# Activity 03

    def dfs(self, start):
        visited = set()
        stack = [start]
        while stack:
            u = stack.pop()
            visited.add(u)
            for v in range(self.size):
                if self.matrix[u][v] == 1 and v not in visited:
                    stack.append(v)
        print(visited)

# Activity 04

g = Graph(5)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(2, 4)
g.addEdge(3, 4)

# Output of bfs()
g.bfs(0)

# Output of dfs()
g.dfs(0)


#Hash Tables

class Pair:
    def __init__(self, key, val):
        self.key = key
        self.val = val

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def probeHash(self, key, index):
        m = int(str(index)[-2:])
        return 1 + (key % m)

    def insert(self, key, val):
        hash_val = self.hash_function(key)
        if self.table[hash_val] is None:
            self.table[hash_val] = Pair(key, val)
        else:
            index = hash_val
            while self.table[index] is not None:
                index = (index + self.probeHash(key, index)) % self.size
            self.table[index] = Pair(key, val)

    def search(self, key):
        hash_val = self.hash_function(key)
        index = hash_val
        while self.table[index] is not None:
            if self.table[index].key == key:
                return self.table[index].val
            index = (index + self.probeHash(key, index)) % self.size
        return False

    def delete(self, key):
        hash_val = self.hash_function(key)
        index = hash_val
        while self.table[index] is not None:
            if self.table[index].key == key:
                self.table[index] = None
                return True
            index = (index + self.probeHash(key, index)) % self.size
        return False


Hash__Table = HashTable(20) 

Hash__Table.insert(21, "Sanduni")
Hash__Table.insert(45, "Nipuni")
Hash__Table.insert(83, "Niranjima")
Hash__Table.insert(26, "Hasithi")
Hash__Table.insert(7, "Oshini")

print(Hash__Table.search(21))


 
