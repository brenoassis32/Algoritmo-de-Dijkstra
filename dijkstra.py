from class_grafo import *

orig=5
dest=2

g6=Grafo(6)

g6.addAresta(5, 4, 5, 0)
g6.addAresta(5, 3, 10, 0)
g6.addAresta(5, 6, 4, 0)
g6.addAresta(6, 4, 1, 0)
g6.addAresta(6, 1, 5, 0)
g6.addAresta(4, 1, 2, 0)
g6.addAresta(4, 3, 2, 0)
g6.addAresta(3, 1, 1, 0)
g6.addAresta(3, 2, 3, 0)
g6.addAresta(1, 2, 2, 0)

g6.dijkstra(orig,dest)
print(g6.retornaValorCusto())
g6.retornaValorRota()
