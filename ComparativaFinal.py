import csv
import time
import random
import os

# Implementación de Shell Sort original
def shell_sort_original(arr):
    n = len(arr)
    intervalo = n // 2
    while intervalo > 0:
        for i in range(intervalo, n):
            temp = arr[i]
            j = i
            while j >= intervalo and arr[j - intervalo] > temp:
                arr[j] = arr[j - intervalo]
                j -= intervalo
            arr[j] = temp
        intervalo //= 2

# Implementación de Shell Sort mejorada
def shell_sort_mejorado(arr):
    n = len(arr)
    intervalo = 1
    while intervalo < n // 3:
        intervalo = intervalo * 3 + 1  
    while intervalo > 0:
        for i in range(intervalo, n):
            temp = arr[i]
            j = i
            while j >= intervalo and arr[j - intervalo] > temp:
                arr[j] = arr[j - intervalo]
                j -= intervalo
            arr[j] = temp
        intervalo //= 3

# Implementación del algoritmo de ordenamiento de Inserción
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Implementación del algoritmo de Quicksort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Generar arreglos de datos para ordenar
arreglo_10 = random.sample(range(1, 100), 10)
arreglo_50 = random.sample(range(1, 100), 10)
arreglo_100 = random.sample(range(1, 1000), 100)
arreglo_500 = random.sample(range(1, 1000), 100)
arreglo_1000 = random.sample(range(1, 10000), 1000)
arreglo_5000 = random.sample(range(1, 10000), 1000)
arreglo_10000 = random.sample(range(1, 100000), 10000)
arreglo_50000 = random.sample(range(1, 100000), 10000)
arreglo_100000 = random.sample(range(1, 1000000), 100000)



# Función para medir el tiempo de ejecución
def medir_tiempo(algoritmo, arreglo):
    inicio = time.time()
    algoritmo(arreglo.copy())
    fin = time.time()
    return fin - inicio

# Medir tiempos de ejecución para cada algoritmo y arreglo...
resultados = []
algoritmos = ['Shell Sort Original', 'Shell Sort Mejorado', 'Inserción', 'Quicksort']
arreglos = [arreglo_10, arreglo_50, arreglo_100, arreglo_500, arreglo_1000, arreglo_5000, arreglo_10000, arreglo_50000, arreglo_100000]

for i, tamano in enumerate([10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000]):
    for j, algoritmo in enumerate([shell_sort_original, shell_sort_mejorado, insertion_sort, quick_sort]):
        print(f"Ejecutando {algoritmos[j]} con arreglo de tamaño {tamano}...")
        tiempo = medir_tiempo(algoritmo, arreglos[i])
        resultados.append([tamano, algoritmos[j], tiempo])

# Guardar los resultados en un archivo CSV
try:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(script_dir, 'resultados_ordenamiento.csv')
    with open(csv_path, mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=',')

        # Escribir encabezados
        writer.writerow(['Tamaño', 'Shell Sort Original', 'Shell Sort Mejorado', 'Inserción', 'Quicksort'])

        # Escribir resultados
        for i, tamano in enumerate([10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000]):
            resultados_fila = [tamano]
            for j, algoritmo in enumerate([shell_sort_original, shell_sort_mejorado, insertion_sort, quick_sort]):
                tiempo = resultados[i * len(algoritmos) + j][2]  # Obtener el tiempo ya medido
                resultados_fila.append(tiempo)
            writer.writerow(resultados_fila)

    print("Los resultados han sido guardados en el archivo 'resultados_ordenamiento.csv' en la misma carpeta del script.")
except Exception as e:
    print("Ocurrió un error al guardar el archivo CSV:", e)