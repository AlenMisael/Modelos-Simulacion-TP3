import matplotlib.pyplot as plt
import numpy as np

#Inciso 2a) Distribucion uniforme
datos_uniformes = np.random.uniform(low=0,high=1,size=1000)
plt.subplot(221) #Grafico en la posicion superior izquierda
plt.hist(datos_uniformes,bins=40, alpha=0.7,color="skyblue", edgecolor="black")
plt.xlabel("Valores")
plt.ylabel("Frecuencia")
plt.title("Distribucion uniforme")

#Inciso 2b) Distribucion normal
media= 0
desvio = 1
datos_normal = np.random.normal(media,desvio, 1000)
plt.subplot(222) #Grafico en la posicion superior derecha
plt.hist(datos_normal,bins=40, alpha=0.7,color="red", edgecolor="black")
plt.xlabel("Valores")
plt.ylabel("Frecuencia")
plt.title("Distribucion normal")

#Inciso 2c) Distribucion de Poisson
lamb=6
datos_poisson = np.random.poisson(lamb, size=1000)
plt.subplot(223) #Grafico en la posicion inferior izquierda
plt.hist(datos_poisson,bins=40, alpha=0.7,color="yellow", edgecolor="black")
plt.xlabel("Valores")
plt.ylabel("Frecuencia")
plt.title("Distribucion de Poisson")

#Inciso 2d) Distribucion Exponencial
beta=3/4

datos_exponencial = np.random.exponential(beta,size=1000)
plt.subplot(224) #Grafico en la posicion inferior derecha
plt.hist(datos_exponencial,bins=40, alpha=0.7,color="green", edgecolor="black")
plt.xlabel("Valores")
plt.ylabel("Frecuencia")
plt.title("Distribucion Exponencial")

plt.tight_layout() #Ajusta espaciado entre graficos
plt.show()

