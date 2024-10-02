import numpy as np
import random
import pygame
import sys
import time

# Inicializamos Pygame
pygame.init()

# Definimos los parámetros
num_ciudades = 4  # Número de ciudades
num_hormigas = 5   # Número de hormigas
alpha = 1.0        # Importancia de la feromona
beta = 2.0         # Importancia de la visibilidad (1 / distancia)
evaporation_rate = 0.5  # Tasa de evaporación de feromonas
intensidad_feromona = 1.0  # Cantidad de feromona depositada por hormiga
iteraciones = 5  # Número de iteraciones

# Configuramos la ventana de Pygame
screen_size = 600  # Tamaño de la ventana
screen = pygame.display.set_mode((screen_size, screen_size))
pygame.display.set_caption("Colonia de Hormigas - TSP")

# Definimos el tamaño de cada celda del fondo cuadriculado
cell_size = 50  # Tamaño de cada celda

# Generamos un conjunto aleatorio de distancias entre las ciudades
distancias = np.random.randint(10, 100, size=(num_ciudades, num_ciudades))
np.fill_diagonal(distancias, 0)

# Inicializamos las feromonas
feromonas = np.ones((num_ciudades, num_ciudades))

# Generamos posiciones aleatorias para las ciudades
posiciones = np.random.rand(num_ciudades, 2) * (screen_size - 100) + 50

def dibujar_fondo_cuadriculado():
    """Dibuja un fondo cuadriculado en la pantalla."""
    color_cuadricula = (200, 200, 200)
    for x in range(0, screen_size, cell_size):
        pygame.draw.line(screen, color_cuadricula, (x, 0), (x, screen_size))
    for y in range(0, screen_size, cell_size):
        pygame.draw.line(screen, color_cuadricula, (0, y), (screen_size, y))

def seleccionar_siguiente_ciudad(ciudad_actual, ciudades_no_visitadas, feromonas, distancias, alpha, beta):
    """Selecciona la siguiente ciudad basada en la probabilidad con feromonas y visibilidad."""
    probabilidades = []
    for ciudad in ciudades_no_visitadas:
        tau = feromonas[ciudad_actual][ciudad] ** alpha
        eta = (1 / distancias[ciudad_actual][ciudad]) ** beta
        probabilidades.append(tau * eta)
    
    probabilidades = probabilidades / np.sum(probabilidades)
    
    return np.random.choice(ciudades_no_visitadas, p=probabilidades)

def recorrer_ciudades(num_ciudades, num_hormigas, feromonas, distancias, alpha, beta):
    """Recorre las ciudades y genera los recorridos de las hormigas, mostrando cada paso."""
    recorridos = []
    distancias_recorridos = []
    
    for _ in range(num_hormigas):
        ciudad_inicial = random.randint(0, num_ciudades - 1)
        recorrido = [ciudad_inicial]
        distancia_total = 0
        ciudades_no_visitadas = list(range(num_ciudades))
        ciudades_no_visitadas.remove(ciudad_inicial)
        
        ciudad_actual = ciudad_inicial
        while ciudades_no_visitadas:
            # Selecciona la siguiente ciudad
            ciudad_siguiente = seleccionar_siguiente_ciudad(ciudad_actual, ciudades_no_visitadas, feromonas, distancias, alpha, beta)
            recorrido.append(ciudad_siguiente)
            distancia_total += distancias[ciudad_actual][ciudad_siguiente]
            
            # Visualizamos el recorrido hasta ahora
            visualizar_recorridos([recorrido])  # Visualiza el recorrido actual
            time.sleep(0.5)  # Pausa para ver el movimiento de la hormiga
            
            ciudad_actual = ciudad_siguiente
            ciudades_no_visitadas.remove(ciudad_siguiente)
        
        # Volvemos a la ciudad inicial
        recorrido.append(ciudad_inicial)
        distancia_total += distancias[ciudad_actual][ciudad_inicial]
        
        # Visualizamos el recorrido final de la hormiga
        visualizar_recorridos([recorrido])
        time.sleep(0.5)  # Pausa para ver el recorrido completo de la hormiga
        
        recorridos.append(recorrido)
        distancias_recorridos.append(distancia_total)
    
    return recorridos, distancias_recorridos


def actualizar_feromonas(feromonas, recorridos, distancias_recorridos, evaporation_rate, intensidad_feromona):
    """Actualiza la cantidad de feromonas en base a los recorridos realizados."""
    # Evaporamos feromonas
    feromonas *= (1 - evaporation_rate)
    
    # Añadimos nuevas feromonas
    for recorrido, distancia in zip(recorridos, distancias_recorridos):
        for i in range(len(recorrido) - 1):
            ciudad_origen = recorrido[i]
            ciudad_destino = recorrido[i + 1]
            feromonas[ciudad_origen][ciudad_destino] += intensidad_feromona / distancia
            feromonas[ciudad_destino][ciudad_origen] += intensidad_feromona / distancia

def colonia_de_hormigas(num_ciudades, num_hormigas, alpha, beta, evaporation_rate, intensidad_feromona, iteraciones):
    """Algoritmo de la colonia de hormigas para resolver el TSP."""
    mejor_recorrido = None
    mejor_distancia = float('inf')
    
    for i in range(iteraciones):
        # Las hormigas recorren las ciudades
        recorridos, distancias_recorridos = recorrer_ciudades(num_ciudades, num_hormigas, feromonas, distancias, alpha, beta)
        
        # Actualizamos la mejor solución
        for recorrido, distancia in zip(recorridos, distancias_recorridos):
            if distancia < mejor_distancia:
                mejor_recorrido = recorrido
                mejor_distancia = distancia

        # Visualizamos todos los recorridos
        visualizar_recorridos(recorridos)
        
        # Imprimimos el estado actual
        print(f"Iteración {i + 1}: Mejor recorrido hasta ahora: {mejor_recorrido}, Distancia: {mejor_distancia}")
        
        # Actualizamos las feromonas
        actualizar_feromonas(feromonas, recorridos, distancias_recorridos, evaporation_rate, intensidad_feromona)
        
        # Pausa para visualizar el progreso
        time.sleep(1)  # Pausa de 1 segundo

    return mejor_recorrido, mejor_distancia

def visualizar_recorridos(recorridos):
    """Visualiza todos los recorridos en la ventana de Pygame."""
    dibujar_fondo_cuadriculado()

    # Dibuja las ciudades
    for i, (x, y) in enumerate(posiciones):
        pygame.draw.circle(screen, (0, 0, 255), (int(x), int(y)), 8)  # Ciudades en azul
        font = pygame.font.Font(None, 36)
        text = font.render(str(i), True, (0, 0, 0))
        screen.blit(text, (x + 10, y - 10))

    # Dibuja los recorridos
    for recorrido in recorridos:
        for i in range(len(recorrido) - 1):
            ciudad_origen = recorrido[i]
            ciudad_destino = recorrido[i + 1]
            pygame.draw.line(screen, (255, 0, 0), posiciones[ciudad_origen], posiciones[ciudad_destino], 2)  # Líneas en rojo

    pygame.display.flip()  # Actualiza la pantalla

# Ejecutamos el algoritmo
mejor_recorrido, mejor_distancia = colonia_de_hormigas(num_ciudades, num_hormigas, alpha, beta, evaporation_rate, intensidad_feromona, iteraciones)

# Mensaje final
print(f"Mejor recorrido final: {mejor_recorrido}")
print(f"Distancia total final: {mejor_distancia}")

# Loop para mantener la ventana abierta
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
