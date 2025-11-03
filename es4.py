n=-1
sp=0
pd=1
while n!=0:
    n= int(input("inserisci un numero: "))
    if n%2 == 0:
        sp=sp+n
    else:
        pd=pd*n
    
    
print ("somma dei numeri pari: ",sp)
print ("prodotto dei numeri dispari: ",pd)
       
    