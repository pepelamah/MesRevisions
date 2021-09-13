def calcul_IMC(taille, poids):
    taille=input("Entrez votre taille en cm: ")
    poids=input("Entrez votre poids en kg: ")
    return (poids/(taille**2)*0.01)
IMC=calcul_IMC(195, 90)
print(IMC)
