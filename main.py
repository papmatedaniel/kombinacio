import random 

while True:
    
    lista = [random.randint(1,6) for i in range(5)] 
    lista.sort() 
    print("számaid: ", lista)
    statisztika = {i:lista.count(i) for i in lista} 
    
    for i in statisztika.items(): 
        print(f"szám {i[0]} ennyi van belőle: {i[1]}") 
    
    
    if len(statisztika) == 5: 
        if min(lista) == 1 and max(lista) == 5: 
            print("Kis sor") 
             
        if min(lista) == 2 and max(lista) == 6: 
            print("Nagy sor") 
    
    if len(statisztika) == 4: 
        print("Pár") 
    
    if len(statisztika) == 3: 
        if 3 in statisztika.values(): 
            print("Tripla") 
    
        else:
            print("Kettő Pár") 
    
    if len(statisztika) == 2: 
        if 3 in statisztika.values(): 
            print("Full House azaz egy tripla és egy pár") 
        else: 
            print("Póker azaz 4 egyforma") 
    
    if len(statisztika) == 1: 
         print("Yahtzee azaz 5 egyforma")
         break
