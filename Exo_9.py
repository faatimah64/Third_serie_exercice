chaine="Ce beau pays Un pays que je veux remettre sur pied"
chaine= chaine.replace("je veux", "Assim veut")
print(chaine)
Liste_mot=chaine.split()

dict_mots={}
for i in Liste_mot:
    if i not in dict_mots.keys():
     dict_mots[i]=1
    else:
         dict_mots[i] +=1
print(dict_mots)




