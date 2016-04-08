from BGraph import *
import AM
import IM

class AL(BGraph):
    def __init__(self, nodes, edges):
        BGraph.__init__(self, nodes, edges)
        self._list = []


    def show(self):
        for i,v in enumerate(self._list):
            print str(i),
            for w in v:
                print "->", w,
            print

    def toAM(self):
        am = AM.AM(self._nodes, self._edges)
        for i, v in enumerate(self._list):
            for j in v:
                am._matrix[i][j] = 1
        return am

    def toIM(self):
        im = IM.IM(self._nodes, self._edges)
        n = 0
        e = 0
        for i in self._list:
            for j in i:
                    if j>n:
                        im._matrix[n][e] = 1
                        im._matrix[j][e] = 1
                        e+=1
            n+=1
        return im


