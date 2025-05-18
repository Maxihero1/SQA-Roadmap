#Bibliotecas
import os
import time

# Listas
IDEstudiante = []
Notas = []

# Funciones
def seleccionarEstudiante(): # Introducción de estudiante a lista
    while True:
        try:
            estudiante = int(input("Introduzca ID de estudiante: "))
            break
        except ValueError:
            print("Tipo de dato no valido.")
    os.system("cls")
    IDEstudiante.append(estudiante)
    return estudiante

def registrarCalificacion(): # Introducción de calificación a lista
    estudiante = seleccionarEstudiante()
    print("El estudiante de ID:", estudiante)
    while True:
        try:
            calificacion = int(input("Obtuvo una calificación de: "))
            return calificacion
        except:
            print("Tipo de dato no valido")

def notificarNota(calificacion):
    if calificacion > 100:
        print("Valor invalido")
    elif calificacion <= 100 and calificacion >= 90:
        if calificacion >= 97:
            print("Por lo tanto aprobo con una A+")
        elif calificacion >= 94:
            print("Por lo tanto aprobo con una A")
        else:
            print("Por lo tanto aprobo con una A-")
    elif calificacion < 90 and calificacion >= 80:
        if calificacion >= 87:
            print("Por lo tanto aprobo con una B+")
        elif calificacion >= 84:
            print("Por lo tanto aprobo con una B")
        else:
            print("Por lo tanto aprobo con una B-")
    elif calificacion < 80 and calificacion >= 70:
        if calificacion >= 77:
            print("Por lo tanto aprobo con una C+")
        elif calificacion >= 74:
            print("Por lo tanto aprobo con una C")
        else:
            print("Por lo tanto aprobo con una C-")
    else:
        print("Usted reprobo")
    Notas.append(calificacion)
    time.sleep(5)
    os.system("cls")

def citarNotasEstudiantes():
    for i in range(len(IDEstudiante)):
        print("La nota del estudiante de ID", IDEstudiante[i], "fue de:", Notas[i])

# Aplicación
for i in range(0,3):
    calificacion = registrarCalificacion()
    notificarNota(calificacion)
citarNotasEstudiantes()
