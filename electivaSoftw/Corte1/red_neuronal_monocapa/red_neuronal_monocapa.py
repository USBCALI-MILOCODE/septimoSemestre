import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

# Definir las entradas y salidas
ENTRADAS = np.array([
    [1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1],  # 0
    [0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0],  # 1
    [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1],  # 2
    [1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1],  # 3
    [1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1],  # 4
    [1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1],  # 5
    [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1],  # 6
    [1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1],  # 7
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],  # 8
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1]   # 9
])

SALIDAS = np.array([
    [0, 0, 0, 0],  # 0
    [0, 0, 0, 1],  # 1
    [0, 0, 1, 0],  # 2
    [0, 0, 1, 1],  # 3
    [0, 1, 0, 0],  # 4
    [0, 1, 0, 1],  # 5
    [0, 1, 1, 0],  # 6
    [0, 1, 1, 1],  # 7
    [1, 0, 0, 0],  # 8
    [1, 0, 0, 1]   # 9
])

# Inicializar pesos aleatorios
np.random.seed(42)
PESOS_INICIALES = np.random.rand(15, 4)

# Parámetros de entrenamiento
TASA_APRENDIZAJE = 0.1
EPOCAS = 100

def activacion(x):
    """Función de activación (paso binario)."""
    return np.where(x >= 0, 1, 0)

def entrenar(entradas, salidas, pesos, tasa_aprendizaje, epocas):
    """Entrena la red neuronal."""
    errores = []
    for _ in range(epocas):
        salida_predicha = activacion(np.dot(entradas, pesos))
        error = salidas - salida_predicha
        errores.append(np.mean(np.abs(error)))
        pesos += tasa_aprendizaje * np.dot(entradas.T, error)
    return pesos, errores

def predecir_numero(numero, pesos_entrenados):
    """Predice la salida para un número específico."""
    entrada = ENTRADAS[numero]
    salida_predicha = activacion(np.dot(entrada, pesos_entrenados))
    return salida_predicha

def agregar_ruido(entrada, porcentaje_ruido=0.1):
    """Agrega ruido a una entrada dada en un porcentaje especificado."""
    entrada_ruidosa = np.copy(entrada)
    num_bits_ruido = int(len(entrada) * porcentaje_ruido)
    indices_ruido = np.random.choice(len(entrada), num_bits_ruido, replace=False)
    entrada_ruidosa[indices_ruido] = 1 - entrada_ruidosa[indices_ruido]  # Invertir bits
    return entrada_ruidosa, indices_ruido

def imprimir_matriz_como_numero(entrada, indices_ruido=None):
    """Imprime la matriz como una representación visual del número."""
    matriz = entrada.reshape(5, 3)
    for i, fila in enumerate(matriz):
        fila_visual = ' | '.join(f'{valor:1}' if valor == 1 else ' ' for valor in fila)
        if indices_ruido is not None:
            for idx in indices_ruido:
                if idx // 3 == i:
                    fila_visual = fila_visual[:(idx % 3) * 2] + 'R' + fila_visual[(idx % 3) * 2 + 1:]
        print(f"[{fila_visual}]")

# Entrenar la red
pesos_entrenados, errores = entrenar(ENTRADAS, SALIDAS, PESOS_INICIALES, TASA_APRENDIZAJE, EPOCAS)

# Graficar el error por época
plt.plot(errores)
plt.title('Error medio por época')
plt.xlabel('Época')
plt.ylabel('Error medio')
plt.grid(True)
plt.show()

# Mostrar la representación visual y los resultados
resumen = []
for numero_a_probar in range(10):
    print(f"\nNúmero: {numero_a_probar}")
    imprimir_matriz_como_numero(ENTRADAS[numero_a_probar])
    
    salida_predicha = predecir_numero(numero_a_probar, pesos_entrenados)
    error = np.any(salida_predicha != SALIDAS[numero_a_probar])
    estado = "ERROR" if error else "CORRECTO"
    
    print(f"Salida Predicha: {salida_predicha}")
    print(f"Salida Esperada: {SALIDAS[numero_a_probar]}")
    
    resumen.append([numero_a_probar, list(salida_predicha), list(SALIDAS[numero_a_probar]), estado])

    # Aplicar ruido a las entradas y probar
    np.random.seed(None)  # Reiniciar la semilla aleatoria para asegurar ruido aleatorio en cada iteración
    entrada_ruidosa, indices_ruido = agregar_ruido(ENTRADAS[numero_a_probar])
    print("\nEntrada con Ruido:")
    imprimir_matriz_como_numero(entrada_ruidosa, indices_ruido)
    print("\nEn este ejemplo, añadí ruido a los bits en las posiciones:", indices_ruido)
    
    salida_predicha_ruido = activacion(np.dot(entrada_ruidosa, pesos_entrenados))
    error_ruido = np.any(salida_predicha_ruido != SALIDAS[numero_a_probar])
    estado_ruido = "ERROR" if error_ruido else "CORRECTO"
    
    print(f"Salida Predicha con Ruido: {salida_predicha_ruido}")
    print(f"Salida Esperada: {SALIDAS[numero_a_probar]}")
    
    resumen.append([f"{numero_a_probar} (con ruido)", list(salida_predicha_ruido), list(SALIDAS[numero_a_probar]), estado_ruido])

# Mostrar el resumen al final en formato tabla
print("\n[=== RESUMEN ===]\n")
print(tabulate(resumen, headers=["Entrada", "Salida Predicha", "Salida Esperada", "Estado"], tablefmt="fancy_grid"))