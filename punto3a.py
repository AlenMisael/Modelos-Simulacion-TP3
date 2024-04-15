import matplotlib.pyplot as plt
import numpy as np

beta=12


#Se aplica la funcion de transformacion siguiendo la formula proporcionada por la catedra
def transformada(muestra,beta):
    datos_exponencial = []
    for dato in muestra: 
        #El dato exponencial sera igual a -(1/lambda(que es 1/beta)) *logaritmo(dato)
        dato_exponencial= -(1/(1/beta))*np.log(dato)
        #Se coloca el dato exponencial en  una nueva lista
        datos_exponencial.append(dato_exponencial)
    return datos_exponencial



#Se crea una lista de 1000 datos uniformes entre 0 y 1 
datos_uniformes = np.random.uniform(low=0,high=1,size=1000)


plt.subplot(221) #Grafico en la posicion superior izquierda
plt.hist(datos_uniformes,bins=40, alpha=0.7,color="skyblue", edgecolor="black")
plt.xlabel("Valores")
plt.ylabel("Frecuencia")
plt.title("Distribucion uniforme")


datos_exponenciales = transformada(datos_uniformes,beta)


plt.subplot(222) #Grafico en la posicion superior derecha
plt.hist(datos_exponenciales,bins=40, alpha=0.7,color="red", edgecolor="black")
plt.xlabel("Valores")
plt.ylabel("Frecuencia")
plt.title("Distribucion exponencial")

#Se muestran ambos graficos uno al lado del otro
plt.show()


