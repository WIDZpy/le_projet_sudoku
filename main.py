from recpdepard import recup
from afichage import afichage
from calcules import calcules
resulta = []
if __name__ == '__main__':
    resu = recup()
    resulta = afichage()
    cal = calcules()
    V2 = resulta.prinsipale(resu.recuperation(1))
    print(V2)





    print(cal.calcules(resu.recuperation(1)))
# le doit étre renplaser par un un 2 pour sortire de la configue teste
    #print(len(resu.recuperation(1)))


