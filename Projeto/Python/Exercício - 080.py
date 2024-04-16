print("====== DESAFIO 080 ======")  

lista = []


for c in range(0, 5):
    valor = int(input("Valor: "))

    if c == 0:
        print(c)
        lista.append(valor)
        print("Adicionado no final da lista...")
        print(lista)

    elif valor >= max(lista):
        print(c)
        lista.insert(len(lista), valor)
        print("Adicionado no final da lista...")
        print(lista)
        
    elif valor <= min(lista):
        print(c)
        lista.insert(0, valor)
        print("Adicionado no inicio da lista...")
        print(lista)
    
    else:
        if c == 2:
            print(c)
            lista.insert(1, valor)
            print("Adicionado na posição 1 da lista...")
            print(lista)

        elif c == 3:
            if valor >= lista[1]:
                print(c)
                lista.insert(2, valor)
                print("Adicionado na posição 2 da lista...")
                print(lista)
            else:
                print(c)
                lista.insert(1, valor)
                print("Adicionado na posição 1 da lista...")
                print(lista)
                
        elif c == 4:
            if valor <= lista[1]:
                print(c)
                lista.insert(1, valor)
                print("Adicionado na posição 1 da lista...")
                print(lista)
            
            elif valor >= lista[2]:
                print(c)
                lista.insert(3, valor)
                print("Adicionado na posição 3 da lista...")
                print(lista)
                
            else:
                print(c)
                lista.insert(2, valor)
                print("Adicionado na posição 2 da lista...")
                print(lista)
            
