velocidade = int(input('digite sua velocidade: '))  #velocidade que o carro está na estrada 
local_carro = int(input("digite o local em que o carro se encontra: ")) #local em que o carro está na estrada
RADAR_1 = 60  # velocidade máxima do radar 1
LOCALRADAR_1 = 100  # local onde o radar 1 está
RADAR_DISTANCIA = 1  # A distância onde o radar pega




vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCALRADAR_1 - RADAR_DISTANCIA) and \
    local_carro <= (LOCALRADAR_1 + RADAR_DISTANCIA)
carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_pass_radar_1

if vel_carro_pass_radar_1:
    print('Velocidade carro passou do radar 1')



if carro_multado_radar_1:
  print("carro multado no radar 1")