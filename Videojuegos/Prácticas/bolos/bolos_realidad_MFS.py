import pymunk
import pygame
import pymunk.pygame_util



pygame.init()
pantalla = pygame.display.set_mode((1200,600))
reloj = pygame.time.Clock()
opciones_dibujo = pymunk.pygame_util.DrawOptions(pantalla)

masa = 0.5  
radio = 30  
g = 98   
v0 = 200     
# Cambiamos el momento de inercia porque el peso está distribuido de una manera no uniforme.
inercia = 0.32 * masa * radio**2
dt = 1/60

pista_cuerpo = pymunk.Body(body_type=pymunk.Body.STATIC)
pista = pymunk.Segment(pista_cuerpo, (0, 500), (1200, 500), 5)
pista.friction = 0.05

bola_cuerpo = pymunk.Body(masa, inercia)
bola_cuerpo.velocity = (v0,0)
# Añadimos una velocidad angular inicial. La bola se lanza con giro
bola_cuerpo.angular_velocity = 2
bola_cuerpo.position = (0, 500 - radio)
bola = pymunk.Circle(bola_cuerpo, radio)
bola.friction = 1

espacio = pymunk.Space()
espacio.gravity = (0,g)
espacio.add(bola_cuerpo, pista_cuerpo, bola,pista)

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
    
    # Cambiamos la fricción de la pista al principio y al final.
    if(bola_cuerpo.position.x > 400 and bola_cuerpo.position.x < 800):
        pista.friction = 0.25
    else: 
        pista.friction = 0.05
    
    # Añadimos la flag de si no ha rodado nunca (tiempo_rodar == 0) para evitar parpadeo de estados.
    if(bola_cuerpo.velocity.x > abs(bola_cuerpo.angular_velocity) * radio and tiempo_rodar == 0):
        estado = "DESLIZANDO"
    else:
        estado = "RODADURA PURA"
        if(tiempo_rodar == 0):
            tiempo_rodar = tiempo
        texto_tiempo_rodar = fuente.render(f"Tiempo que tarda en rodar: {tiempo_rodar:.2f} s", True, (255,0,0))
        pantalla.blit(texto_tiempo_rodar, (20, 120))
        # Frenamos la bola asumiendo un rozamiento por rodadura.
        bola_cuerpo.velocity = bola_cuerpo.velocity * 0.995
        bola_cuerpo.angular_velocity = bola_cuerpo.angular_velocity * 0.995
        pantalla.blit(fuente.render("--------------------------------",True, (0,0,0)), (20,142.5))
        pantalla.blit(fuente.render("Resultados ideales:", True, (0,0,0)), (20, 160))
        pantalla.blit(fuente.render("Velocidad lineal: 142.964 px/s", True, (0,0,0)), (20,185))
        pantalla.blit(fuente.render("Velocidad angular: 4.753 rad/s", True, (0,0,0)), (20,210))
        pantalla.blit(fuente.render("Tiempo: 2.91 s", True, (0,0,0)), (20,235))
        
    texto_tiempo = fuente_titulo.render(f"Tiempo: {tiempo:.2f} s", True, (0, 0, 0))
    texto_estado = fuente.render(f"Estado de la bola: {estado}", True, (0,0,0))
    texto_velocidad = fuente.render(f"Velocidad lineal: {bola_cuerpo.velocity.x:.2f} px/s", True, (0,0,0))
    texto_velocidad_angular = fuente.render(f"Velocidad angular: {bola_cuerpo.angular_velocity:.2f} rad/s", True, (0,0,0))
    
    pantalla.blit(texto_tiempo, (20, 10))
    pantalla.blit(texto_estado, (20, 45))
    pantalla.blit(texto_velocidad, (20, 70))
    pantalla.blit(texto_velocidad_angular, (20, 95))
    
    # Indicador de cuando cambia el rozamiento en la superficie 
    pygame.draw.line(pantalla, (255, 0, 0), (400, 520), (400, 495), 5)
    pygame.draw.line(pantalla, (255, 0, 0), (800, 520), (800, 495), 5)
    
    espacio.step(dt)
    tiempo += dt
    
    pygame.display.flip()
    reloj.tick(60)
    
