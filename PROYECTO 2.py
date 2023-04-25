import csv
from datetime import date

estudiantes =  []

def buscar_estudiantes(carnet):
    for estudiante in estudiantes:
        if estudiante['Carnet'] == carnet:
            return estudiante
        return None
    
def datos_estudiantes():
    cantidad = int(input('Ingrese la cantidad de estudiantes a ingresar en el sistema: '))
    for i in range(cantidad):
        carnet = input('Ingrese el carnte del estudiante: ')
        nombre = input('Ingrese el nombre del estudiante: ')
        carrera = input('Ingrese la carrera del estudiante: ')
        estudiante = {'Carnet': carnet, 'Nombre': nombre, 'Carrera': carrera, 'Nota': 0}
        estudiantes.append(estudiante)

def notas_estudiantes():
    carnet = int(input('Ingrese carnet del estudiante: '))
    estudiante = buscar_estudiantes(carnet)
    if estudiante is not None:
        print('--- Datos del estudiante ---')
        print("Carnet:", estudiante["carnet"])
        print("Nombre:", estudiante["nombre"])
        print("Carrera:", estudiante["carrera"])
        print("Nota:", estudiante["nota"])

        respuesta = input('¿Desea cambiar la nota? (s/n) ')
        if respuesta.lower() == 's'|'S':
            nueva_nota = float(input('Ingrese la nota nueva: '))
            estudiante["nota"] = nueva_nota
        else:
            print('--- Estudiante no registrado ---')

def mostrar_datos_estudiantes():
    for estudiante in estudiantes:
        if estudiante["nota"] != 0:
            print("Carnet:", estudiante["carnet"])
            print("Nombre:", estudiante["nombre"])
            print("Carrera:", estudiante["carrera"])
            print("Nota:", estudiante["nota"])

def exportar_acta_notas():
    hoy = date.today().strftime("%Y%m%d")
    with open(f"acta_notas_{hoy}.csv", mode="w", newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["Carnet", "Nombre", "Carrera", "Nota"])
        for estudiante in estudiantes:
            escritor.writerow([estudiante["carnet"], estudiante["nombre"], estudiante["carrera"], estudiante["nota"]])
    print("El acta de notas se ha exportado exitosamente.")


def menu():
    while True:
        print("------- Menú Principal -------")
        print("1. Ingreso de datos de estudiantes")
        print("2. Ingreso de notas")
        print("3. Exportar acta de notas")
        print("4. Salir")
        
        opcion = int(input("Seleccione una opcion: "))
        
        if opcion == 1:
            datos_estudiantes()
        elif opcion == 2:
            notas_estudiantes()
        elif opcion == 3:
            exportar_acta_notas()
            notas = [estudiante["nota"] for estudiante in estudiantes if estudiante["nota"] != 0]
            promedio = sum(notas) / len(notas)
            hoy = date.today().strftime("%d/%m/%Y")
            print("Promedio de notas:", promedio)
            print("Fecha de generacion de acta:", hoy)
        elif opcion == 4:
            break

menu()






