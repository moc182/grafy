from BGraph import *
import random
import AL
import IM



class AM(BGraph):
    def __init__(self, nodes, edges=0):
        BGraph.__init__(self, nodes, edges)
        self._matrix = np.zeros((nodes, nodes), dtype=np.int)


    def create(self):
        if self._edges > self._nodes*(self._nodes-1)/2: # jesli zostanie podana za zbyt duza ilosc krawedzi to tworzymy graf pelny
            z = self._nodes*(self._nodes-1)/2
        else:
            z = self._edges
        while z > 0:
            x = random.randrange(self._nodes)
            y = random.randrange(self._nodes)
            if not x == y and self._matrix[x][y]==0:
                self._matrix[x][y] = 1
                self._matrix[y][x] = 1
                z-=1

    def createP(self, pp):
        self._edges = 0
        i = 0
        while i < self._nodes*(self._nodes-1)/2:
            x = random.randrange(self._nodes)
            y = random.randrange(self._nodes)
            if not x == y and self._matrix[x][y] == 0:
                if pp > random.randrange(100):
                    self._matrix[x][y] = 1
                    self._matrix[y][x] = 1
                    self._edges += 1
            else:
                i -= 1
            i += 1




    def show(self):
        for i in self._matrix:
            print i

    def toAL(self):
        al = AL.AL(self._nodes, self._edges)
        for i in range(self._nodes):
            temp = []
            for j in range(self._nodes):
                if self._matrix[i][j] == 1:
                    temp.append(j)
            al._list.append(temp)
        return al

    def toIM(self):
        im = IM.IM(self._nodes, self._edges)
        e = 0
        for i in range(self._nodes):
            for j in range(i, self._nodes):
                if self._matrix[i][j] == 1 and e <= self._edges:
                    im._matrix[i][e] = 1
                    im._matrix[j][e] = 1
                    e+=1
        return im


