#!/usr/bin/env python
# -*- coding: utf-8 -*-
import networkx as nx
import matplotlib.pyplot as plt
from AM import AM
from Switch import *


k1 = True
while k1:
    print("\n~~ WYBIERZ SPOSÓB LOSOWANIA GRAFU ~~\n1) Wierzchołki-Krawędzie\n2) Wierzchołki-Prawdopodobieństwo\n3) Zakoncz\n")
    option = input("Wybór: ")
    if option == 1:
        nodes = input("\nLiczba wierzchołków: ")
        edges = input("Liczba krawędzi: ")
        am = AM(nodes=nodes, edges=edges)
        am.create()
        chooseRep(am)
    if option == 2:
        nodes = input("\nLiczba wierzchołków: ")
        probability = input("Prawdopodobieństwo: ")
        am = AM(nodes=nodes)
        am.createP(probability)
        chooseRep(am)
    if option == 3:
        k1 = False

###########################################################
'''print("~~~~ AM ~~~~")
am1 = AM.AM(nodes=5)
am1.createP(50)
am1.show()

print("~~~~ AM to AL ~~~~")
al1 = am1.toAL()
al1.show()

print("~~~~ AM to IM ~~~~")
im1 = am1.toIM()
im1.show()

print("~~~~ AL to AM ~~~~")
am2 = al1.toAM()
am2.show()

print("~~~~ AL to IM ~~~~")
im2 = al1.toIM()
im2.show()

print("~~~~ IM to AM ~~~~")
am3 = im2.toAM()
am3.show()

print("~~~~ IM to AL ~~~~")
al2 = im2.toAL()
al2.show()


###########################################################
g = nx.Graph()
nr = 0
for i in range(al1._nodes):
    g.add_node(i)
    for j in al1._list[i]:
        if j > i:
            g.add_edge(i, j, nr=nr)
            nr += 1

pos = nx.shell_layout(g)
nx.draw_networkx_nodes(g, pos, node_size=300)
nx.draw_networkx_edges(g, pos)
nx.draw_networkx_labels(g, pos)
nx.draw_networkx_edge_labels(g, pos)

plt.axis('off')
plt.show()'''
