from random import*
a=randint(1,10)
b=randint(1,10)
saisie="abc"
print("a=",a,"b=",b)
while(saisie == 'abc'):
    somme=int(input("Calculez la somme des deux nombres: "))
            
    if(somme==a+b):
        print("Félicitations vous avez trouvé la bonne reponse.") 
        saisie ="Q"
            
    else:
        saisie=input("les deux nombres sont != Vous avez le choix de quitter en tapant la lettre Q ou de reessayer en tapant n'importe quel touche du clavier :")
        saisie = saisie.upper()
        if saisie =="Q":
            break
            
        # elif saisie =="R":
        #         a=randint(1,100)
        #         b=randint(1,100)
                
        