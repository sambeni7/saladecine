import json

salas = {}

def mostrar_sala(nombre):
    if nombre in salas:
        print(f"Sala: {nombre}")
        print("Estado actual de la sala:")
        print("  A B C D")
        for i, fila in enumerate(salas[nombre]):
            print(f"{i} {' '.join(fila)}")
        print()
    else:
        print(f"La sala '{nombre}' no existe.\n")

def crear_sala():
    nombre = input("Ingrese el nombre o número de la sala: ")
    if nombre in salas:
        print(f"La sala '{nombre}' ya existe.\n")
    else:
        salas[nombre] = [['O'] * 4 for _ in range(4)]  # Sala 4x4 con 'O' para asientos libres
        print(f"Sala '{nombre}' creada exitosamente.\n")
        mostrar_sala(nombre)

def ver_sala():
    nombre = input("Ingrese el nombre o número de la sala a ver: ")
    mostrar_sala(nombre)

def asignar_puesto():
    nombre = input("Ingrese el nombre o número de la sala: ")
    if nombre in salas:
        fila = int(input("Número de la fila (0-3): "))
        columna = input("Letra de la columna (A-D): ").upper()
        col_index = ord(columna) - ord('A')  # Convierte letra a índice numérico

        if 0 <= fila < 4 and 0 <= col_index < 4:
            if salas[nombre][fila][col_index] == 'O':
                salas[nombre][fila][col_index] = 'X'
                print(f"Asiento {fila}{columna} en sala '{nombre}' asignado.\n")
                mostrar_sala(nombre)  # Muestra la sala actualizada
            else:
                print(f"El asiento {fila}{columna} ya está ocupado.\n")
        else:
            print("Número de fila o columna fuera de rango. Deben ser entre 0 y 3 para filas y A-D para columnas.\n")
    else:
        print(f"La sala '{nombre}' no existe.\n")

def guardar_salas():
    with open('salas.txt', 'w') as archivo:
        json.dump(salas, archivo)
    print("Datos de las salas guardados.\n")

def cargar_salas():
    global salas
    try:
        with open('salas.txt', 'r') as archivo:
            salas = json.load(archivo)
        print("Salas cargadas exitosamente.\n")
    except FileNotFoundError:
        print("No se encontró un archivo de salas. Comenzando con salas vacías.\n")

# Cargar las salas existentes al inicio del programa
cargar_salas()

# Ciclo de operación principal
while True:
    print("_")
    print("1. Crear sala")
    print("_")
    print("2. Ver sala")
    print("_")
    print("3. Asignar puesto")
    print("_")
    print("4. Guardar salas")
    print("_")
    print("5. Salir")
    print("_")

    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        crear_sala()
    elif opcion == '2':
        ver_sala()
    elif opcion == '3':
        asignar_puesto()
    elif opcion == '4':
        guardar_salas()
    elif opcion == '5':
        print("Saliendo del sistema. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intente de nuevo.\n")