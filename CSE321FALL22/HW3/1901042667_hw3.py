from collections import defaultdict
 
class Graph:
    def __init__(self, vertices):

        self.graph = defaultdict(list)
        self.V = vertices
    

    def addEdge(self, u, v):

        self.graph[u-1].append(v-1)


    def topologicalSortDFS(self):

        visited = [False]*self.V
        stack = []

        for i in reversed(range(self.V)):
            if visited[i] == False:
                self.setVisited(i, visited, stack)   
        
        return stack

    def topologicalSortBFS(self):

        inDegrees = [0]*(self.V)

        for i in self.graph:
            for j in self.graph[i]:
                inDegrees[j] += 1
        
        queue = []
        from heapq import heappush, heappop
        
        for i in range(self.V):
            if inDegrees[i] == 0:
                heappush(queue, i)

        order = []
        visited = [0]*(self.V)

        while queue:
            u = heappop(queue)
            if not visited[u]:
                order.append(u+1)
                for i in self.graph[u]:
                    inDegrees[i] -= 1
                    if inDegrees[i] == 0:
                        heappush(queue, i)
                visited[u] = 1
        
        return order
    
    def setVisited(self, u, visited, stack):
        visited[u] = True
        for i in self.graph[u]:
            if visited[i] == False:
                self.setVisited(i, visited, stack)
        stack.insert(0, u+1)



def findExponantial(a, n):
    if n==1:
        return a
    if n%2==1:
        return a*findExponantial(a, n-1)
    half = findExponantial(a, n/2)
    return half*half



def sudokuWithExhaustiveSearch(sudokuPuzzle):

    sudokuString = ''.join(map(str,[''.join(map(str, i)) for i in sudokuPuzzle]))
    
    index = sudokuString.find('0')

    unusuble = {sudokuString[j] for j in range(len(sudokuString)) if (index//9 == j//9) | (index%9 == j%9) 
    | ((index//9)//3 == (j//9)//3) & ((index%9)//3 == (j%9)//3)}

    possibilities = {str(i) for i in range(10)} - unusuble

    for val in possibilities:
        sudokuString = sudokuString[0:index] + val + sudokuString[index+1: ]
        sudokuWithExhaustiveSearch(sudokuString)
        if sudokuString.find('0') == -1:
            solvedPuzzle = []
            for i in range(len(sudokuString)):  
                if i % 9 == 0:
                    temp = []
                    for j in sudokuString[i:i+9]:
                        temp.append(int(j))
                    solvedPuzzle.append(temp)
            drawPuzzle(solvedPuzzle)


def drawPuzzle(puzzle):
    for i in range(9):
        if i == 0 or i == 3 or i == 6:
            print("*************************")
        for j in range(9):
            if j == 0 or j == 3 or j == 6:
                print("| ", end = "")
            if puzzle[i][j] != 0:
                print(puzzle[i][j], end = " ")
            else:
                print(end = "  ")
            if j == 8:
                print("|")
    print("*************************")
    
    
sudokuPuzzle =  [[0, 8, 0, 5, 3, 0, 2, 7, 6],
                  [0, 5, 0, 6, 0, 0, 0, 0, 0],
                  [6, 1, 3, 0, 0, 0, 0, 0, 0],
                  [0, 0, 6, 0, 5, 0, 0, 0, 0],
                  [0, 3, 2, 0, 0, 0, 7, 0, 1],
                  [7, 4, 5, 0, 0, 8, 6, 9, 3],
                  [0, 7, 0, 9, 6, 0, 5, 0, 0],
                  [4, 0, 0, 1, 8, 0, 0, 6, 7],
                  [5, 0, 0, 0, 0, 4, 8, 2, 9]]


print("Sudoku Problem")
drawPuzzle(sudokuPuzzle)
print("\nSudoku Solution")
sudokuWithExhaustiveSearch(sudokuPuzzle)
        
A = 7
B = [[6, 2], [6, 0], [4, 0], [4, 5], [2, 3], [3, 5]]
 
graph = Graph(A)
for u, v in B:
    graph.addEdge(u, v)

print("\n\nDirections: ")
for x, y in B:
    print(x, ",", y)
        
stack = graph.topologicalSortDFS()
print("Topological DFS: ", stack) 

stack = graph.topologicalSortBFS()
print("Topological BFS: ", stack) 

print("\n\n")
 
solution = findExponantial(4,2)
print("4^2 = ", solution)
solution = findExponantial(2,3)
print("2^3 = ", solution)