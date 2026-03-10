import pymunk
import pygame
import pymunk.pygame_util

pygame.init()
pantalla = pygame.display.set_mode((600,600))
reloj = pygame.time.Clock()
opciones_dibujo = pymunk.pygame_util.DrawOptions(pantalla)

espacio = pymunk.Space()
espacio.gravity = (0,900)

class DampedPendulum:
    def __init__(self, body, anchor, length, friction, space):
        self.body = body
        self.anchor = anchor
        self.length = length
        self.friction = friction
        
        self.joint = pymunk.PinJoint(space.static_body, self.body, self.anchor, (0,0))       
        self.joint.distance = self.length
        
        space.add(self.joint)
        
        def apply_friction(body, gravity, damping, dt):
            pymunk.Body.update_velocity(body, gravity, damping, dt)
            fuerza_rozamiento = -self.friction * body.velocity
            body.apply_force_at_local_point(fuerza_rozamiento, (0,0))
        
        self.body.velocity_func = apply_friction
        


# Creamos elementos físicos
masa = 2
radio = 20
momento = pymunk.moment_for_circle(masa, 0, radio)
cuerpo_bola = pymunk.Body(masa,momento)
cuerpo_bola.position = (400, 300)
forma_bola = pymunk.Circle(cuerpo_bola, radio)

espacio.add(cuerpo_bola, forma_bola)

mi_pendulo = DampedPendulum(cuerpo_bola, (300,100), 250, 0.3, espacio)

ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
    
    pantalla.fill((255,255,255))
    
    espacio.debug_draw(opciones_dibujo)
    espacio.step(1/60)
    
    pygame.display.flip()
    reloj.tick(60)
    
pygame.quit()