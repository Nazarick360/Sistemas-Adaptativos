import random
import time

#función para leer la temperatura 
def leer_temperatura():
    # Temperatura ambiente en °C
    return random.uniform(15, 35)

#ajustar la velocidad del ventilador
def ajustar_velocidad(velocidad):
    print(f"Velocidad del ventilador ajustada a: {velocidad}%")

#auto-ajuste basado en la temperatura
def autoajuste_ventilador():
    while True:
        #leer la temperatura ambiente actual
        temperatura_actual = leer_temperatura()
        print(f"Temperatura actual: {temperatura_actual:.2f}°C")
        
        #determinar la velocidad del ventilador en base a la temperatura
        if temperatura_actual < 20:
            velocidad = 0  #ventilador apagado
        elif 20 <= temperatura_actual < 25:
            velocidad = 30  #velocidad 1
        elif 25 <= temperatura_actual < 30:
            velocidad = 60  #velocidad 2
        else:
            velocidad = 100  #velocidad 3
        
        #ajustar la velocidad del ventilador
        ajustar_velocidad(velocidad)
        
        #para voler a tomar la lectura
        time.sleep(5)

#auto-ajuste del ventilador
autoajuste_ventilador()
