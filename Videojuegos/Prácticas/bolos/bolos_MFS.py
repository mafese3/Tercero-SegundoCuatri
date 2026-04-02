import pymunk
import pygame
import pymunk.pygame_util

#Iniciamos la interfaz
pygame.init()
pantalla = pygame.display.set_mode((1000,600))
reloj = pygame.time.Clock()
opciones_dibujo = pymunk.pygame_util.DrawOptions(pantalla)

# Asignamos unos valores iniciales a los parámetros
masa = 0.5  
radio = 30  
g = 98   
v0 = 200    
inercia = 2/5 * masa * radio**2     # El momento de inercia de una esfera sólida
dt = 1/60

# Creamos los cuerpos que conformarán el espacio (la pista y la bola)
pista_cuerpo = pymunk.Body(body_type=pymunk.Body.STATIC)
pista = pymunk.Segment(pista_cuerpo, (0, 500), (1000, 500), 5)
pista.friction = 0.2

bola_cuerpo = pymunk.Body(masa, inercia)
bola_cuerpo.velocity = (v0,0)
bola_cuerpo.position = (0, 500 - radio)
bola = pymunk.Circle(bola_cuerpo, radio)    #La dibujamos como un círculo porque estamos en 2D
bola.friction = 1

# Creamos el espacio con gravedad y le añadimos los cuerpos con sus formas
espacio = pymunk.Space()
espacio.gravity = (0,g)
espacio.add(bola_cuerpo, pista_cuerpo, bola,pista)

# Hacemos el bucle de ejecución.
ejecutando = True
tiempo = 0
fuente_titulo = pygame.font.SysFont(None, 30)
fuente = pygame.font.SysFont(None, 20)
tiempo_rodar = 0
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
            
    pantalla.fill((255,255,255))
    espacio.debug_draw(opciones_dibujo)
    
    # Cuando se cumple la condición de rodadura pura se muestran los datos que queremos.
    if(bola_cuerpo.velocity.x > abs(bola_cuerpo.angular_velocity) * radio):
        estado = "DESLIZANDO"
    else:
        estado = "RODADURA PURA"
        if(tiempo_rodar == 0):
            tiempo_rodar = tiempo
        texto_tiempo_rodar = fuente.render(f"Tiempo que tarda en rodar: {tiempo_rodar:.2f} s", True, (255,0,0))
        pantalla.blit(texto_tiempo_rodar, (20, 120))
        pantalla.blit(fuente.render("--------------------------------",True, (0,0,0)), (20,142.5))
        pantalla.blit(fuente.render("Resultados teóricos mediante fórmulas:", True, (0,0,0)), (20, 160))
        pantalla.blit(fuente.render("Velocidad lineal: 142.964 px/s", True, (0,0,0)), (20,185))
        pantalla.blit(fuente.render("Velocidad angular: 4.753 rad/s", True, (0,0,0)), (20,210))
        pantalla.blit(fuente.render("Tiempo: 2.91 s", True, (0,0,0)), (20,235))
    
    # Imprimimos en pantalla todos los datos que queremos visualizar
    texto_tiempo = fuente_titulo.render(f"Tiempo: {tiempo:.2f} s", True, (0, 0, 0))
    texto_estado = fuente.render(f"Estado de la bola: {estado}", True, (0,0,0))
    texto_velocidad = fuente.render(f"Velocidad lineal: {bola_cuerpo.velocity.x:.2f} px/s", True, (0,0,0))
    texto_velocidad_angular = fuente.render(f"Velocidad angular: {bola_cuerpo.angular_velocity:.2f} rad/s", True, (0,0,0))
    
    pantalla.blit(texto_tiempo, (20, 10))
    pantalla.blit(texto_estado, (20, 45))
    pantalla.blit(texto_velocidad, (20, 70))
    pantalla.blit(texto_velocidad_angular, (20, 95))
    
    # Aumentamos el tiempo
    espacio.step(dt)
    tiempo += dt
    
    pygame.display.flip()
    reloj.tick(60)
    
