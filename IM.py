from BGraph import *
import AM
import AL


class IM(BGraph):
    def __init__(self, nodes, edges):
        BGraph.__init__(self, nodes, edges)
        self._matrix = np.zeros((nodes, edges), dtype=np.int)

    def show(self):
        for i in self._matrix:
            print i

    def toAL(self):
        al = AL.AL(self._nodes, self._edges)
        for v in range(self._nodes):
            temp = []
            for e in range(self._edges):
                if self._matrix[v][e] == 1:
                    for n in range(self._nodes):
                        if self._matrix[n][e] == 1 and n != v:
                            temp.append(n)
            al._list.append(temp)
        return al

    def toAM(self):
        am = AM.AM(self._nodes, self._edges)
        for i in range(self._nodes):
            for j in range(self._edges):
                if self._matrix[i][j] == 1:
                    for n in range(self._nodes):
                        if self._matrix[n][j] == 1 and n != i:
                            am._matrix[i][n] = 1
                            am._matrix[n][i] = 1
        return am