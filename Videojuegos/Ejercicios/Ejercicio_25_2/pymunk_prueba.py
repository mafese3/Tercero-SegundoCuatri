import pymunk
import pygame
#1. Configuracion de la ventana
pygame.init()
pantalla = pygame.display.set_mode((600 , 600) )
pygame.display.set_caption(" Hello Munk ")
reloj = pygame.time.Clock()

# 2. Configuracion del mundo fisico
espacio = pymunk.Space()
# --- CREAR EL SUELO ---
suelo = pymunk.Segment( espacio.static_body ,
(0 , 550) ,(600 , 550) , 5)
suelo.elasticity = 0.5
espacio.add( suelo )
# --- CREAR LA CAJA ---
masa = 1
lado = 50
momento = pymunk.moment_for_box( masa ,( lado , lado ))
cuerpo_caja = pymunk.Body( masa , momento )
cuerpo_caja.position =(300 , 50)
forma_caja = pymunk.Poly.create_box( cuerpo_caja ,(lado , lado ) )
forma_caja.elasticity = 0.8
espacio.add( cuerpo_caja , forma_caja )

# 3. Bucle principal
running = True
while running :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False
    pantalla.fill((255 , 255 , 255) )
    # Avanzar fisica
    espacio.step(1/60.0)
    # Dibujar caja( posicion actual )
    pos = cuerpo_caja.position
    pygame.draw.rect( pantalla ,(255 , 0, 0) ,
    ( pos .x -25 , pos .y -25 , 50 , 50) )
    # Dibujar suelo
    pygame.draw.line( pantalla ,(0 , 0 , 0) ,
    (0 , 550) ,(600 , 550) , 5)
    pygame.display.flip()
    reloj.tick(60)
pygame.quit()

