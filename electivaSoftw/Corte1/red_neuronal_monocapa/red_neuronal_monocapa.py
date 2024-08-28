import numpy as np

# Definir las entradas (matrices 5x3) y las salidas esperadas (códigos binarios de 4 bits)
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
EPOCAS = 10000

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
    """Agrega ruido a la entrada y devuelve los índices alterados."""
    entrada_con_ruido = entrada.copy()
    num_bits = len(entrada)
    num_ruido = int(num_bits * porcentaje_ruido)
    indices_ruido = np.random.choice(num_bits, num_ruido, replace=False)
    entrada_con_ruido[indices_ruido] = 1 - entrada_con_ruido[indices_ruido]  # Invertir los bits
    return entrada_con_ruido, indices_ruido

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

# Probar la red con un número específico
NUMERO_A_PROBAR = 9
salida_predicha = predecir_numero(NUMERO_A_PROBAR, pesos_entrenados)

print(f"\n[--- NUMERO A PROBAR --- > {NUMERO_A_PROBAR}]\n")

print("ENTRADA:")
print(ENTRADAS[NUMERO_A_PROBAR])

print("\nSALIDA PREDICHA:")
print(salida_predicha)

print("\nSALIDA ESPERADA:")
print(SALIDAS[NUMERO_A_PROBAR])

print("\nMATRIZ VISUAL DEL NÚMERO:")
imprimir_matriz_como_numero(ENTRADAS[NUMERO_A_PROBAR])

# Añadir ruido a la entrada del número específico
entrada_ruidosa, indices_ruido = agregar_ruido(ENTRADAS[NUMERO_A_PROBAR], porcentaje_ruido=0.2)
print(f"\n< == ENTRADA RUIDOSA == >")
print(entrada_ruidosa)

print("\nMATRIZ VISUAL DEL NÚMERO CON RUIDO:")
imprimir_matriz_como_numero(entrada_ruidosa, indices_ruido)

print("\nEn este ejemplo, añadí ruido a los bits en las posiciones:")
for idx in indices_ruido:
    estado_original = ENTRADAS[NUMERO_A_PROBAR][idx]
    estado_actual = entrada_ruidosa[idx]
    print(f"Posición: {idx} (originalmente {'1' if estado_original == 1 else '0'}, ahora {'1' if estado_actual == 1 else '0'})")
