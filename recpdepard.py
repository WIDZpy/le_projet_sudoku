class recup:
    #créé une chaine de caractére avec le résultat
    def recuperation(self,V2):
        cases = []
        # 81 = le nombre de cases dans un sudoku
        if V2 == 2 :
            for nbdecase in range(81):
                grille = input("done moi les chifre de ton sudoku\n")
                if grille == "":
                    cases += " "
                else:
                    cases += grille
        elif V2 == 1:
            presudo = "7     1   81 93 454   5  329  5 4 78 583   29   82    5  27 9846 41382 78 29  6  "
            for loop in presudo:
                cases += [loop]
        else:
            for nbdecase in range(81):
                if nbdecase % 5 == 0:
                    cases = cases + [""]
                else:
                    cases = cases + ["0"]
        #print(cases)
        return (cases)