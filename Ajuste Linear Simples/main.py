import numpy as np
import matplotlib.pyplot as plt

# Entrada dos pontos amostrados
n = int(input("Digite o número de pontos amostrados: "))
x = []
y = []
print("Digite os valores de x e y para cada ponto:")
for i in range(n):
    x_i = float(input(f"x[{i+1}]: "))
    y_i = float(input(f"y[{i+1}]: "))
    x.append(x_i)
    y.append(y_i)

x = np.array(x)
y = np.array(y)

# Entrada das retas aleatórias
print("\nDigite os coeficientes da primeira reta aleatória (y = a1 * x + b1):")
a1 = float(input("a1: "))
b1 = float(input("b1: "))

print("\nDigite os coeficientes da segunda reta aleatória (y = a2 * x + b2):")
a2 = float(input("a2: "))
b2 = float(input("b2: "))

# Cálculo dos desvios totais para as retas aleatórias
S1 = np.sum((y - (a1 * x + b1)) ** 2)
S2 = np.sum((y - (a2 * x + b2)) ** 2)

# Ajuste pela fórmula de mínimos quadrados
n = len(x)
a = (n * np.sum(x * y) - np.sum(x) * np.sum(y)) / (n * np.sum(x**2) - (np.sum(x))**2)
b = (np.sum(y) - a * np.sum(x)) / n

# Cálculo do desvio total para a melhor reta
S_best = np.sum((y - (a * x + b)) ** 2)

# Exibir os valores de a, b e os desvios
print(f"\nMelhor reta: y = {a:.2f}x + {b:.2f}")
print(f"Desvios totais: S1 = {S1:.2f}, S2 = {S2:.2f}, S_best = {S_best:.2f}")

# Cálculo dos valores ajustados para cada reta
y_best = a * x + b
y_aleat1 = a1 * x + b1
y_aleat2 = a2 * x + b2

# Tabela com os valores calculados
table_data = []
for i in range(n):
    table_data.append([i+1, x[i], y[i], y_best[i], y_aleat1[i], y_aleat2[i]])

# Plotagem dos pontos e retas
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue', label='Pontos amostrados')
plt.plot(x, y_aleat1, color='red', linestyle='--', label=f'Reta aleatória 1: y = {a1}x + {b1}')
plt.plot(x, y_aleat2, color='green', linestyle='--', label=f'Reta aleatória 2: y = {a2}x + {b2}')
plt.plot(x, y_best, color='black', linestyle='-', label=f'Melhor reta: y = {a:.2f}x + {b:.2f}')

# Ajustes do gráfico
plt.xlabel('x')
plt.ylabel('y')
plt.title('Ajuste Linear Simples')
plt.legend()
plt.grid(True)

# Exibindo a tabela
columns = ["i", "xi", "yi", "ŷ (melhor reta)", "ỹ (reta aleatória 1)", "ȳ (reta aleatória 2)"]
table = plt.table(cellText=table_data, colLabels=columns, cellLoc='center', loc='bottom', bbox=[0, -0.5, 1, 0.3])
table.auto_set_font_size(False)
table.set_fontsize(8)
table.scale(1, 1.5)

plt.subplots_adjust(left=0.2, bottom=0.4)
plt.show()
