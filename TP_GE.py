moy_int=0
while moy_int==0:
    moy_str=input("Saisir votre note: ")
    try:
        moy_int=int(moy_str)
    except:
        print("Veuillez saisir une valeur numérique!!")
    else:
        if(20>=moy_int>=18):
            print("Excellent!")
        elif(18>moy_int>=14):
            print("Très bien!!")
        elif(14>moy_int>=10):
            print("Assez bien!!")
        elif(10>moy_int<=5):
            print("Insuffisant!!")
        elif(moy_int<5):
            print("catastrophique!!")

