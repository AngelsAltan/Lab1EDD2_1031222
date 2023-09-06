import csv
import json
from AVL import AVLTree

with open('inputprueba.csv') as f:
    reader = csv.reader(f, delimiter=";")
    for row in reader:   
        
Arbol = AVLTree()
def mostrar_menu():
    print("Menú:")
    print("1. Insertar archivo csv")
    print("2. Eliminar por DPI")
    print("3. Eliminar por Nombre")
    print("4. Buscar por Nombre")
    print("5. Buscar por DPI")
    print("6. Modificar datos por nombre")
    print("7. Modificar datos por DPI")
    print("8. Salir")

def opcion_1():
    print("Has seleccionado la Opción 1")

def opcion_2():
    print("Has seleccionado la Opción 2")

def opcion_3():
    print("Has seleccionado la Opción 3")

def opcion_4():
    print("Has seleccionado la Opción 4")
    
def opcion_5():
    print("Has seleccionado la Opción 5")
    
def opcion_6():
    print("Has seleccionado la Opción 6")
    
def opcion_7():
    print("Has seleccionado la Opción 7")
    
def opcion_8():
    print("Has seleccionado la Opción 8")

while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        opcion_1()
    elif opcion == "2":
        opcion_2()
    elif opcion == "3":
        opcion_3()
    elif opcion == "4":
        opcion_4()
    elif opcion == "5":
        opcion_5()
    elif opcion == "6":
        opcion_6()
    elif opcion == "7":
        opcion_7()
    elif opcion == "8":
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")
    
