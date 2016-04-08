#!/usr/bin/env python
# -*- coding: utf-8 -*-
import networkx as nx
import matplotlib.pyplot as plt


def draw(al):
    g = nx.Graph()
    nr = 0
    for i in range(al._nodes):
        g.add_node(i)
        for j in al._list[i]:
            if j > i:
                g.add_edge(i, j, nr=nr)
                nr += 1

    pos = nx.shell_layout(g)
    nx.draw_networkx_nodes(g, pos, node_size=300)
    nx.draw_networkx_edges(g, pos)
    nx.draw_networkx_labels(g, pos)
    nx.draw_networkx_edge_labels(g, pos)

    plt.axis('off')
    plt.show()

def chooseRep(obj):
    k2 = True
    while k2:
        print(
            "\n~~ WYBIERZ REPREZENTACJE ~~\n1) Macierz sąsiedztwa\n2) Lista sąsiedztwa\n3) Macierz incydencji\n4) Wróć\n")
        model = input("Reprezentacja nr: ")
        if model == 1:
            print("\n~~ Macierz sąsiedztwa ~~")
            obj.show()

            al = obj.toAL()
            draw(al)

            changeRep("am", obj)
        if model == 2:
            print("\n~~ Lista sąsiedztwa ~~")
            al = obj.toAL()
            al.show()

            draw(al)

            changeRep("al", al)
        if model == 3:
            print("\n~~ Macierz incydencji ~~")
            im = obj.toIM()
            im.show()

            al = obj.toAL()
            draw(al)

            changeRep("im", im)
        if model == 4:
            k2 = False


def changeRep(mode, obj):
    k3 = True
    while k3:
        if mode == "am":
            print("\n~~ ZAMIEŃ NA ~~\n1) Liste sąsiedztwa\n2) Macierz incydencji\n3) Wróć\n")
            change = input("Wybór: ")
            if change == 1:
                al2 = obj.toAL()
                print("\nMacierz sąsiedztwa --> Lista sąsiedztwa")
                al2.show()
            if change == 2:
                im2 = obj.toIM()
                print("\nMacierz sąsiedztwa --> Macierz incydencji")
                im2.show()
            if change == 3:
                k3 = False

        if mode == "al":
            print("\n~~ ZAMIEŃ NA ~~\n1) Macierz sąsiedztwa\n2) Macierz incydencji\n3) Wróć\n")
            change = input("Wybór: ")
            if change == 1:
                am2 = obj.toAM()
                print("\nLista sąsiedztwa --> Macierz sąsiedztwa")
                am2.show()
            if change == 2:
                im2 = obj.toIM()
                print("\nLista sąsiedztwa --> Macierz incydencji")
                im2.show()
            if change == 3:
                k3 = False

        if mode == "im":
            print("\n~~ ZAMIEŃ NA ~~\n1) Macierz sąsiedztwa\n2) Liste sąsiedztwa\n3) Wróć\n")
            change = input("Wybór: ")
            if change == 1:
                am = obj.toAM()
                print("\nMacierz incydencji --> Macierz sąsiedztwa")
                am.show()
            if change == 2:
                al = obj.toAL()
                print("\nMacierz incydencji --> Lista sasiedztwa")
                al.show()
            if change == 3:
                k3 = False