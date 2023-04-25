 #Ordenamiento de burbuja (Bubble Sort), compara los elementos adyacentes del vector y los intercambia si están en el orden incorrecto. 
 #El proceso se repite varias veces hasta que el vector está completamente ordenado.
def burbuja(nums):
    for i in range(len(nums)):
        for j in range(len(nums)-1-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

    nums = []
    n = int(input("Ingrese la cantidad de números: "))
    for i in range(n):
        nums.append(int(input(f"Ingrese el número {i+1}: ")))

    burbuja(nums)
    print("El vector ordenado es:")
    print(nums)
 #esta funcion utiliza el algoritmo de ordenamiento de burbuja para ordenar el vector, el vector ordenado se imprime en la consola al final del programa.  

 #Ordenamiento por selección (Selection Sort), busca el elemento más pequeño del vector y lo coloca en la primera posición. Luego, 
 #busca el siguiente elemento más pequeño y lo coloca en la segunda posición, y así sucesivamente hasta que el vector está completamente ordenado.
def selecccion(nums):
    n = len(nums)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]

    nums = []
    n = int(input("Ingrese la cantidad de números: "))
    for i in range(n):
        nums.append(int(input(f"Ingrese el número {i+1}: ")))

    selecccion(nums)
    print("El vector ordenado es:")
    for num in nums:
        print(num, end=" ")

 #esta funncion utiliza el algoritmo de ordenamiento por selección para ordenar el vector. El vector se solicita al usuario por medio de un ciclo for 
 #y la función selecccion es invocada para ordenarlo.

 #Ordenamiento por inserción (Insertion Sort), es un algoritmo simple y eficiente para ordenar vectores pequeños. el algoritmo trabaja como si estuviera ordenando 
 #un mazo de cartas en una mano. El algoritmo recorre el vector, compara cada elemento con el anterior y los intercambia si están en el orden incorrecto.
def insercion(nums):
    n = len(nums)
    for i in range(1, n):
        j = i
        while j > 0 and nums[j-1] > nums[j]:
            nums[j-1], nums[j] = nums[j], nums[j-1]
            j -= 1

    nums = []
    n = int(input("Ingrese la cantidad de números: "))
    for i in range(n):
        nums.append(int(input(f"Ingrese el número {i+1}: ")))

    insercion(nums)
    print("El vector ordenado es:")
    for num in nums:
        print(num, end=" ")


 #Ordenamiento rápido (Quick Sort), es uno de los algoritmos de ordenamiento más rápidos y eficientes para ordenar vectores grandes. El algoritmo 
 #divide el vector en dos subvectores, ordena cada subvector recursivamente y luego combina los subvectores ordenados en un vector ordenado.
def quicksort(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr)//2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)
        arr = input("Ingrese los números que desea ordenar, separados por comas: ")
        arr = [int(x) for x in arr.split(",")]
        print("Lista desordenada: ", arr)
        sorted_arr = quicksort(arr)
        print("Lista ordenada: ", sorted_arr)        

while True:
    print('---- MENÚ PRINCIPAL ----')
    print('1. Ordenamiento de burbuja (Bubble Sort)')   
    print('2. Ordenamiento por selección (Selection Sort)') 
    print('3. Ordenamiento por inserción (Insertion Sort)')
    print('4. Ordenamiento rápido (Quick Sort)')
    print('0. SALIR')
    opcion = int(input('Seleccione número de opcion: '))

    match opcion:
        case '1':
            burbuja()
        case '2':
            selecccion()
        case '3':
            insercion()
        case '4':
            quicksort()
        case '0':
            print('--- Fin de la ejecucion ---')
            break    