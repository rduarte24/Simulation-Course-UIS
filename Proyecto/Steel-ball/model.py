
#El usuario debe ingresar la masa de la esfera como parámetro de entrada 
def simulated(masa):
    import numpy as np
    g=9.8           #Gravedad
    Me=5972e24     #Masa de la Tierra
    ConsG=6674e-11 #Constante Gravitacional
    RadioT=6371     #Radio de la Tierra1
    t=0
    k=(masa*g)/(RadioT*1000)
    print("Inicio de Simulación T=0")
    x=-RadioT
    maxV=1
    for i in range(1,60):
        x=RadioT*np.cos(np.sqrt(k/masa)*t)
        v=RadioT*np.sin(np.sqrt(k/masa)*t)*np.sqrt(k/masa)*t*-1
        if (np.abs(v)>np.abs(maxV)):
            maxV=v
        print(f'i= {i} tnow = {t}  Posicion = {x} Velocidad= {v} ')
        t+=60
    print(f'Velocidad máxima alcanzada= {np.abs(maxV)} k/h')

simulated(1000)





