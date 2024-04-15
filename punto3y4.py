import matplotlib.pyplot as plt
import numpy as np
import statistics 


#Se define el valor de beta
beta=3

#Se obtienen las 3 muestras exponenciales con 100, 1000 o 10000 elementos
datos_exponencial1 = np.random.exponential(beta,100)
datos_exponencial2 = np.random.exponential(beta,1000)
datos_exponencial3 = np.random.exponential(beta,10000)

#Media de los datos exponenciales
media1 = statistics.mean(datos_exponencial1)
media2 = statistics.mean(datos_exponencial2)
media3 = statistics.mean(datos_exponencial3)
print("La media de los 100 valores fue de: " + str(media1))
print("La media de los 1000 valores fue de: " + str(media2))
print("La media de los 10000 valores fue de: " + str(media3))

#Desvio estandar de los datos exponenciales
ds1 = statistics.stdev(datos_exponencial1)
ds2 = statistics.stdev(datos_exponencial2)
ds3 = statistics.stdev(datos_exponencial3)
print("La desviacion estandar de los 100 valores fue de: " + str(ds1))
print("La desviacion estandar de los 1000 valores fue de: " + str(ds2))
print("La desviacion estandar de los 10000 valores fue de: " + str(ds3))

#Varianza de los datos exponenciales
varianza1 = statistics.variance(datos_exponencial1)
varianza2 = statistics.variance(datos_exponencial2)
varianza3 = statistics.variance(datos_exponencial3)
print("La varianza de los 100 valores fue de: " + str(varianza1))
print("La varianza de los 1000 valores fue de: " + str(varianza2))
print("La varianza de los 10000 valores fue de: " + str(varianza3))

#Grafico de los datos con 100 valores
plt.subplot(221) #Grafico en la posicion inferior derecha
plt.hist(datos_exponencial1,bins=40, alpha=0.7,color="green", edgecolor="black")
plt.xlabel("Valores")
plt.ylabel("Frecuencia")
plt.title("Distribucion Exponencial de 100 valores")

#Grafico de los datos con 1000 valores
plt.subplot(222)
plt.hist(datos_exponencial2,bins=40, alpha=0.7,color="yellow", edgecolor="black")
plt.xlabel("Valores")
plt.ylabel("Frecuencia")
plt.title("Distribucion Exponencial de 1000 valores")

#Grafico de los datos con 10000 valores
plt.subplot(223)
plt.hist(datos_exponencial3,bins=40, alpha=0.7,color="blue", edgecolor="black")
plt.xlabel("Valores")
plt.ylabel("Frecuencia")
plt.title("Distribucion Exponencial de 10000 valores")

plt.tight_layout() #Ajusta espaciado entre graficos
plt.show()
