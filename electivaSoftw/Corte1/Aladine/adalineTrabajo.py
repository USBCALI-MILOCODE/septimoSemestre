#importar librerias
import numpy as np
import matplotlib.pyplot as plt

# Definir los parámetros
A1 = 1.0  # Amplitud de x1
A2 = 1.0  # Amplitud de x2
A3 = 1.0  # Amplitud de x3
w1 = 2 * np.pi * 1  # Frecuencia angular para x1 (puedes ajustar)
w2 = 2 * np.pi * 2  # Frecuencia angular para x2 (puedes ajustar)
w3 = 2 * np.pi * 3  # Frecuencia angular para x3 (puedes ajustar)

# Definir las funciones de activación y entrenamiento
def linear_function(x):
    return x

def adaline_predict(X, weights):
    return linear_function(np.dot(X, weights[1:]) + 0*weights[0])

def adaline_train(X, y, learning_rate, epochs):
    weights = np.random.rand(X.shape[1] + 1)
    errors = []
    for _ in range(epochs):
        total_error = 0
        for xi, target in zip(X, y):
            output = adaline_predict(xi, weights)
            error = (target - output)**2
            total_error += abs(error)
            update = 2 * learning_rate * (target - output)
            weights[1:] += update * xi
            weights[0] += update
        errors.append(total_error)
    return weights, errors

# Preparar los datos de entrada y salida
n_samples = 5000
t = np.linspace(0, 12, n_samples)

# Definir las señales sinusoidales
x1 = A1 * np.sin(w1 * t)
x2 = A2 * np.sin(w2 * t)
x3 = A3 * np.sin(w3 * t)

# Combinar las señales
X = x1 + x2 + x3

# Graficar las señales individuales y la señal combinada
plt.figure(figsize=(12, 6))
plt.plot(t, x1, label='x1 = A1 * sin(w1 * t)', color='b')
plt.plot(t, x2, label='x2 = A2 * sin(w2 * t)', color='g')
plt.plot(t, x3, label='x3 = A3 * sin(w3 * t)', color='r')
plt.plot(t, X, label='X = x1 + x2 + x3', linestyle='--', color='k')
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud de la señal")
plt.title("Componentes Sinusoidales y Señal Combinada")
plt.legend()
plt.grid(True)
plt.show()

# Graficar la señal combinada y las salidas esperadas en una sola gráfica
plt.figure(figsize=(12, 6))
plt.plot(t, X, label='Entrada con ruido', color='k')
plt.plot(t, x1, '--b', label='Salida esperada: x1')
plt.plot(t, x2, '--g', label='Salida esperada: x2')
plt.plot(t, x3, '--r', label='Salida esperada: x3')
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud de la señal")
plt.title("Señal Combinada y Salidas Esperadas")
plt.legend()
plt.grid(True)
plt.show()

# Crear las entradas y la salida para ADALINE
delay = 15
noisy_signal = np.array([X[i:i+delay] for i in range(n_samples-delay)])
d = x1[delay:]  # Selecciona una salida específica para entrenar

# Entrenar el perceptrón
weights, errors = adaline_train(noisy_signal, d, 0.01, 200)
print("Pesos entrenados:", weights)
print("Errores:", errors)

# Graficar el error global en cada época
plt.figure(figsize=(12, 6))
plt.plot(range(1, len(errors) + 1), errors, marker='o')
plt.xlabel('Época')
plt.ylabel('Error Global')
plt.title('Error Global del Perceptrón en cada Época')
plt.grid(True)
plt.show()

# Señal filtrada
prediction = np.zeros(noisy_signal.shape[0])
for i, xi in enumerate(noisy_signal):
    prediction[i] = adaline_predict(xi, weights)

# Mostrar la gráfica con la señal filtrada
plt.figure(figsize=(12, 6))
plt.plot(t, X, 'b', label='Entrada con ruido')
plt.plot(t, x1, '--r', label='Salida esperada: x1')
plt.plot(t[delay:], prediction, '-.k', label='Salida filtrada por la red')
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud de la señal")
plt.title("Señal Filtrada por la Red Neuronal")
plt.legend()
plt.grid(True)
plt.show()
