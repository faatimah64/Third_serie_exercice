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
        


