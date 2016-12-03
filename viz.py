from graphviz import Digraph
import sys

if len(sys.argv) != 2:
    print("usage: python viz.py FILENUM")

FILE_NUMBER = [sys.argv[1]]

for fname in []:
    with open('cs170_final_inputs/' + fname + '.in') as f:
        dot = Digraph()
        n = int(next(f))
        A = []
        for line in f:
            A.append(list(map(int, line.rstrip().split(' '))))
        for i in range(n):
            dot.node(str(i), str(A[i][i]) + ", (" + str(i) + ")")

        for i in range(n):
            for j in range(n):
                if A[i][j] and i != j:
                    dot.edge(str(i), str(j))

        dot.render("graphpdf/" + fname, view=True)
