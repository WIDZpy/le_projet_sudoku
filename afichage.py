class afichage:
    def prinsipale(self,listt):
        #caca = liste
        #print(caca)
        resultat = ""
        V1 = 1
        V3 = 0
        for boucle in listt:

            #print(V1)
            if V1 % 9 == 0 and boucle != " ":
                resultat = f"{resultat} {boucle}\n"

            elif V1 % 9 != 0 and boucle != " ":
                resultat = f"{resultat} {boucle}"

            elif V1 % 9 == 0 and boucle == " ":
                resultat = f"{resultat} -\n"

            else:
                resultat = f"{resultat} -"
            if V1 == 3 * 9 or V1 == 6 * 9:
                for loop in range(11):
                    resultat = f"{resultat} —"
                resultat = f"{resultat} \n"

            #print(V3)
            #print("b",V1)
            if V1 == 3 + 9 * V3:
                resultat = f"{resultat} |"
            elif V1 == 6 + 9 * V3:
                resultat = f"{resultat} |"
            V1 += 1
            if V1 % 9 == 0:
                V3 += 1
        return resultat

        #print(resultat)

#{liste[range(boucle,boucle+9)]}