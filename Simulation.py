N = 105095 #Numero de usuarios
L = 4 #Llamadas por persona
H = 120 # Duracion de cada llamada

hp=3600 #Tiempo en segundos en una hora

#Condiciones de Erlang B
ErlangB = (N*L*H)/3600
ErlangB = round(ErlangB,2)
#print(ErlangB)
porcetajeB = 84.06 #Porcentaje de perdida para 1% con un solo circuito
nB = (ErlangB*100)/porcetajeB
nB = round(nB,2)
#print(nB)

#Llamadas del evento
N_ev = N*L
#print(N_ev)
#Porcentaje de bloqueo
Porcentajeerror = 0.01
E1plusiA= (ErlangB*Porcentajeerror)/(N_ev+1+(ErlangB*Porcentajeerror))
E1plusiA = round(E1plusiA,10)
#print(E1plusiA)

#Intensidad de trafico
lambda_ = N_ev/hp
lambda_ = round(lambda_,2)
#print(lambda_)

#Ritmo de arribo
Ritmoarribo = 1/lambda_
Ritmoarribo = round(Ritmoarribo,6)
#print(Ritmoarribo)

#Tasa de asignacion de circuito digital
mu = 1/H
mu  = round(mu,6)
#print(mu)

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
#print(CR)

#Gestiones efectivas
Gefectivas=CA-CR
Gefectivas=round(Gefectivas,3)
#print(Gefectivas)

#Estimacion de tiempo de espera
TiempoMedio = 1/(N_ev-ErlangB)
TiempoMedio = round(TiempoMedio,8)
TiempoW  = H*TiempoMedio
TiempoPromedio = TiempoW*lambda_
#print(TiempoPromedio)