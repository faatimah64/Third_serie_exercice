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

#fonction permettant de Remplacer
def A(ch):
    modi=ch.replace("je veux", "Assim veut")
    return modi
print(A("je veux manger"))

#fonction permettant de decouper en list de mots
def B(mots):
    res=mots.split()
    return res
print(B("je veux manger"))

#fonction permettant de decouper en dictionaire de mots en mettant les mots comme clés et les occurences comme valeurs

def C(lst):
    dict_mots={}
    for i in lst:
        if i not in dict_mots.keys():
            dict_mots[i]=1
        else:
            dict_mots[i] +=1
    return dict_mots

#affichage 1
l1 = B("bonjour bonjour aurevoir")
d1 = C(l1)
print(d1)

#affichage 2     
print(C(B("bjr bjr bjr aur")))

#(1=2)




