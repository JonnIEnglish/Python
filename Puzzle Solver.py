import numpy as np

#a = [1, 1, 1, 0, 1]
#b = [0, 0, 0, 0, 1]
#c = [0, 1, 1, 0, 1]
#d = [1, 0, 0, 1, 0]
#e = [1, 1, 0, 0, 0]
#f = [1, 1, 1, 0, 0]
#g = [0, 0, 0, 1, 0]
#h = [1, 0, 1, 0, 1]
#i = [1, 0, 0, 1, 1]
#j = [1, 0, 1, 0, 0]

a = b = [0, 0, 0, 0, 0]
c = d = e = f = g = h = i = j = [0, 0, 0, 0, 0]


pieceArray = np.matrix([a, b, c, d, e, f, g, h, i, j])


def top_mat(pOrder):
    top = pieceArray[pOrder[0:5]]
    return(top)


def bottom_mat(pOrder):
    bottom = pieceArray[pOrder[5:10]]
    return(bottom.transpose())



def run(pOrder):
    top = top_mat(pOrder)
    bottom = bottom_mat(pOrder)
    print("\n\nTop\n")
    print(top)
    print("\nBottom\n")
    print(bottom)
    works = np.array_equal(top, bottom)
    print(works)
    return(works)

def doPuzzle():
    global solutions
    global solutionsList
    solutions = ([])
    numIt = 0
    numSuccess = 0
    numComb = 0
    for i in range(0,10):
        for j in range(0,10):
            if i != j:
                for k in range(0,10):
                    if k not in [i,j]:
                        for l in range(0,10):
                            if l not in [i,j,k]:
                                for m in range(0,10):
                                    if m not in [i,j,k,l]:
                                        for n in range(0,10):
                                            if n not in [i,j,k,l,m]:
                                                for o in range(0,10):
                                                    if o not in [i,j,k,l,m,n]:
                                                        for p in range(0,10):
                                                            if p not in [i,j,k,l,m,n,o]:
                                                                for q in range(0,10):
                                                                    if q not in[i,j,k,l,m,n,o,p]:
                                                                        for r in range(0,10):
                                                                            if r not in [i,j,k,l,m,n,o,p,q]:
                                                                                pOrder = [i,j,k,l,m,n,o,p,q,r]
                                                                                if run(pOrder):
                                                                                    print("SUCCESS!!!!!")
                                                                                    numSuccess += 1
                                                                                    numComb += 1
                                                                                    numIt += 1
                                                                                    print(numIt/3628800*100,"%")
                                                                                    print("Number of successes: ", numSuccess)
                                                                                    print("Number checked: ", numComb, "\n")
                                                                                    solutionsList = solutions.append(pOrder)
                                                                                    if numSuccess == 4:
                                                                                        return


                                                                                numIt += 1
                                                                                numComb += 1
                                                                                print(numIt/3628800*100,"%")
                                                                                print("Number of successes:", numSuccess)
                                                                                print("Number checked: ", numComb, "\n")


doPuzzle()
print(solutionsList)
