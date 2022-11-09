##hacer una funciòn q devuelva una lista con 5 patentes
## al azar q no se repitan "LL NNN LL" mayùs

import random
def patentes():
    abc="A,B,C,D,E,F,G,H,I,J,K,L,M,N,Ñ,O,P,Q,R,S,T,U,V,W,X,Y,Z" #o abrir un lemario
    num="0,1,2,3,4,5,6,7,8,9"
    listap=[]
    cont=0
    while(cont<5):
        l=random.choice(abc)
        n=random.choice(num)
        pat=
        if not pat in listap:
            listap.append(pat)
    return(listap)

##pp
print(patentes())

