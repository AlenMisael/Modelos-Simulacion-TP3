import statistics 
import matplotlib.pyplot as plt
import numpy as np

#Se obtiene una muestra aleatoria de 100 eleemntos entre 0 y 1
muestra = np.random.uniform(0,1,100)
print(muestra)
#Se calcula la media, el desvio estandar y la varianza
media = statistics.mean(muestra)
desvio_estandar = statistics.stdev(muestra)
varianza = statistics.variance(muestra)
#Se muestra la media, el desvio estandar y la varianza"
print("La media es: " + str(media))
print("El desvio estandar es: " + str(desvio_estandar))
print("La varianza es: " + str(varianza))

#Crea un histograma con lineas para la media y el desvio estandar
plt.figure(figsize=(8,6))
plt.hist(muestra, bins=10, color="skyblue", edgecolor="black", alpha=0.7)
plt.axvline(media, color="red", linestyle="--", label="Media")
plt.axvline(media + desvio_estandar, color="green", linestyle="-", label="Media + Desvio Estandar")
plt.axvline(media - desvio_estandar, color="green", linestyle="-", label="Media - Desvio Estandar")
plt.legend()
plt.xlabel("Valores")
plt.ylabel("Frecuencia")
plt.title("Histograma con muestra y desvio estandar")
plt.show()

#Se crea un grafico de caja y bigotes
plt.figure(figsize=(8,6))
plt.boxplot(muestra, vert=False)
plt.title("Grafico de caja")
plt.xlabel("Muestra")
plt.ylabel("Valores")
plt.show()


#Se crea un grafico de dispersion
plt.figure(figsize=(10,6))
plt.scatter(range(1,101), muestra, label="Valores")
plt.axhline(y=media, color="r", linestyle="--", label="Media")
plt.legend()
plt.xlabel("Indice de la muestra")
plt.ylabel("Valores")
plt.title("Grafico de la muestra donde se observa la media")
plt.show()



