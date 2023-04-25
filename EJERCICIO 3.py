N = int(input("Ingrese número de elementos para el vector (no mayor a 100): "))

if N > 100:
    print("--- Error, no pueden ser mas de 100 ---")
    exit()

vector = []
for i in range(N):
    num = int(input(f"Ingrese número #{i+1}: "))
    j = 0
    while j < len(vector) and vector[j] < num:
        j += 1
    vector.insert(j, num)
    
while True:
    buscar = int(input("Ingrese número para su busqueda (ingrese -1 para salir): "))
    if buscar == -1:
        break
    else:
        num_encontrado = False
        for i in range(len(vector)):
            if vector[i] == buscar:
                print(f"El número {buscar} se encuentra en la posición {i}")
                num_encontrado = True
                break
        if not num_encontrado:
            print(f"El número {buscar} no está en el vector.")
    print("Los números ingresados son:", vector)        