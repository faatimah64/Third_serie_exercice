coordinates= [(4,5),(9,3),(12,8),(13,7),(18,6),(20,9)]
i=0
coordinates2=[]
while i < len(coordinates):
    point=coordinates[i]
    y=point[1]
    x=point[0]
    if y>7:
        nouveau_point=(x,7)
    else:
        nouveau_point=(x,y)
    coordinates2.append(nouveau_point)
    i=i+1
print(coordinates2)    
        


"""
ordinates=[]
for i in coordinates :
    print (i[0])
    ordinates.append(i[1])
print(ordinates)


dic_coord={}

for i in coordinates :
    v=(i[1])
    c= str(i[0])
    dic_coord[v]=c
print(dic_coord)"""

dic_coord={}
i=0
while i < len(coordinates2) :
    c=coordinates2[i][0]
    v=coordinates2[i][1]
    dic_coord[c]=v
    i=i+1
print(dic_coord)



