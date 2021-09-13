from random import*
compteur=0
quitter = 0
saisie = "blabla"
while quitter == 0:
    a=randint(1,3)
    b=randint(1,3)
    compteur+=1
        
    if(a==b):
        print("Félicitations les deux nombres sont égaux.")
        print("vous avez gagné au bout de ",compteur,"essais")
    
        print("Fin du programme!!")
        break
        
        
    else:
        saisie=input("les deux nombres sont != Vous avez le choix de rejouer en tapant r ou de quitter en tapant la lettre q:")
        if saisie =="q":
            print("vous êtes sortis après",compteur,"essais")
            break
        elif saisie =="r":
            quitter = 0
    

        
