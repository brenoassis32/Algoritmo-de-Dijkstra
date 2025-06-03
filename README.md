# Algoritmo-de-Dijkstra

## Importando a classe Grafo
~~~python
from class_grafo import *
~~~
Lembre-se que o arquivo class_grafo.py deve estar na mesma pasta do arquivo prim.py

## Passando a quantidade de vértices igual a 4
~~~python
g=Grafo(6)
~~~

## Definindo Origem e Destino do problema
~~~python
orig=5
dest=2
~~~

## Adicionando arcos/arestas seguindo o formato: .addAresta(vértice1, vértice2, peso da arco/aresta, orientação do problema)

Orientação do problema
* 0 = orientado (arcos)
* 1 = não-orientado (arestas)

~~~python
g.addAresta(5, 4, 5, 0)
g.addAresta(5, 3, 10, 0)
g.addAresta(5, 6, 4, 0)
g.addAresta(6, 4, 1, 0)
g.addAresta(6, 1, 5, 0)
g.addAresta(4, 1, 2, 0)
g.addAresta(4, 3, 2, 0)
g.addAresta(3, 1, 1, 0)
g.addAresta(3, 2, 3, 0)
g.addAresta(1, 2, 2, 0)
~~~

## Executando o algortimo de Dijkstra
~~~python
g.dijkstra(orig,dest)
~~~

## ## Obtendo o caminho mínimo entre o par origem-destino
~~~python
print(g.retornaValorCusto())
~~~
Resultado igual a 9 no exemplo demonstrado.

## ## Obtendo a rota ótima para o par origem-destino
~~~python
g.retornaValorRota()
~~~
Resultado de C = {(5,4), (4,1), (1,2)} no exemplo demonstrado.


## Referências
ARENALES, M. et al., Pesquisa Operacional para Cursos de Engenharia., Rio de Janeiro: Elsevier, 2007.

HILLIER, F.S., LIEBERMAN, G.J. Introduction to Operations Research., MacGraw-Hill, 2001.

TAHA, H.A., Pesquisa Operacional, 8. ed. Pearson Prentice Hall, 2008.

WINSTON, W. Operations Reseach, Applications and Algorithms. Duxbury Press, 2003.

