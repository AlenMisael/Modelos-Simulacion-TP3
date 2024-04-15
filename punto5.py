import numpy as np
import statistics
import math

#Coeficiente para un 99% de confianza
z=2.58
cantidad = 1000

def obtener_extremos(muestra,z, cantidad, cant_desvios=1): 
    media = statistics.mean(muestra)
    desvio_estandar = (statistics.stdev(muestra))*cant_desvios
    extremo_inferior = (media - z*(desvio_estandar/math.sqrt(cantidad)))  
    extremo_superior = (media + z*(desvio_estandar/math.sqrt(cantidad))) 

    print ("La muestra poblacional tiene el extremo inferior: " + str(extremo_inferior) + " y el extremo superior: " + 
           str(extremo_superior))
    


#Se crea una muestra uniforme
datos = np.random.uniform(0,1,cantidad)

#Se obtienen los extremos para una muestra con una desviacion estandar
obtener_extremos(datos,z, cantidad)

#Se obtienen los extremos para una muestra con 2 desviaciones estandar
obtener_extremos(datos,z, cantidad, 2)


