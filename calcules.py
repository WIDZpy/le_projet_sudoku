class calcules:
    def calcules(self,recup):
        V4 = 1
        lst =


        for loop in recup:


            if V4 % 9 == 1 :
                ligne = []
                ligne += recup[V4-1:V4-1+9]
                #ligne += recup[9 * int(V4 / 9) -9:9 * int(V4 / 9)]
            colone = []
            colone += recup[(V4-1) % 9 :  :9]


            for boucle in range(3):
            lst += 1 + 3 * boucle
            lst += 28 + 3 * boucle
            lst += 73 + 3 * boucle
            if (V4-1) % 3 == 0 :
                block = []
                var = V4 - 1

                if V4 % 9
                for rules in range(3) :
                    block += recup[var-1 + 9 * rules : var-1 + 9 * rules +3]


            print(block)
            #print(ligne)
            #print(colone)
            V4 += 1



#for loop in range(0,9):

#    lst += [loop]