N = 105095 #Numero de usuarios
L = 4 #Llamadas por persona
H = 120 # Duracion de cada llamada
hp=3600 #Tiempo en segundos en una hora

#Condiciones de Erlang B
ErlangB = (N*L*H)/3600
ErlangB = round(ErlangB,2)
porcetajeB = 84.06 #Porcentaje de perdida para 1% con un solo circuito
nB = (ErlangB*100)/porcetajeB
nB = round(nB,2)

#Llamadas del evento
N_ev = N*L
#Porcentaje de bloqueo
Porcentajeerror = 0.01
E1plusiA= (ErlangB*Porcentajeerror)/(N_ev+1+(ErlangB*Porcentajeerror))
E1plusiA = round(E1plusiA,10)

#Intensidad de trafico
lambda_ = N_ev/hp
lambda_ = round(lambda_,2)

#Ritmo de arribo
Ritmoarribo = 1/lambda_
Ritmoarribo = round(Ritmoarribo,5)

#Tasa de asignacion de circuito digital
mu = 1/H
mu  = round(mu,6)

#Respuesta del sistema
nA=666*8 #Numero de canales * 8 slots para cada uno

#Gestiones atendidas
CA = nA*lambda_

#Trafico cursado mediante erlang B
CY=CA*(1-Porcentajeerror)

#Trafico rechazado
B=E1plusiA
CR = CA*B
CR=round(CR,3)

#Gestiones efectivas
Gefectivas=CA-CR
Gefectivas=round(Gefectivas,3)

#Estimacion de tiempo de espera
TiempoMedio = 1/(N_ev-ErlangB)
TiempoMedio = round(TiempoMedio,8)
TiempoW  = H*TiempoMedio
TiempoPromedio = TiempoW*lambda_

import time
import numpy as np

#Combinacion, el primer valor es el numero de circuito, el segundo es el numero de llamada entrante y el tercero es el cronometro de los 120 segundos que le quedan dentro de la circuiteria
Filas = 26
Columnas = 8
#Creacion de la lista tridimensional
Circuitos =[]
for x in range(Filas):
    Circuitos.append([])
    for y in range(Columnas):
        Circuitos[x].append([])
        for z in range(3):
           Circuitos[x][y].append(0)

#Llenar el numero correspondiente de slot
Llenador=1
for i in range(Filas):
    for j in range(Columnas):
        Circuitos[i][j][0]=Llenador
        Llenador +=1
#Pasar la lista a una matriz tridimensional       
Circuitos = np.array(Circuitos).reshape(Filas,Columnas,3)


Nllamada=1
Segundero = (Nllamada*Ritmoarribo)+(mu*26)
Llenador=1
while (Segundero<=hp and Nllamada<=N_ev and Llenador <=N_ev):
    #time.sleep(Ritmoarribo)
   
    for i in range(Filas):
        for j in range(Columnas):
            if(Circuitos[i][j][2]==0):
                Circuitos[i][j][1]=Llenador
                Circuitos[i][j][2]=H
                Llenador +=1
            else:
                Circuitos[i][j][2]-=1
    print(Circuitos)
    #time.sleep(mu)
    
    Nllamada +=1
    Segundero = (Nllamada*Ritmoarribo)+(mu*26)