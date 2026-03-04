import pybullet as p
import pybullet_data

# 1. Configuración inicial
p.connect(p.GUI )
p.setAdditionalSearchPath( pybullet_data.getDataPath() )

# 2. Cargar suelo y configurar rebote
suelo_id = p.loadURDF(" plane . urdf ")
# restitution = elasticidad
p.changeDynamics( suelo_id , -1 , restitution =0.7)

# 3. Cargar cubo y configurar su rebote
# Posicion Z =1.0 (1 metro de altura )
cubo_id = p.loadURDF (" cube_small . urdf ", [0 , 0 , 1.0])
p.changeDynamics ( cubo_id , -1, restitution=0.7)

# 4. Ajustar camara
p.resetDebugVisualizerCamera (cameraDistance=1.5 , cameraYaw=45 , cameraPitch=-30 , cameraTargetPosition=[0 , 0 , 0])

import time
# 5. Bucle de simulacion
print (" Simulacion iniciada ... ")
try :
    while True :
        # Avanza el motor fisico
        p.stepSimulation ()
        # Sincroniza con tiempo real (240 Hz)
        time.sleep (1./240.)
except KeyboardInterrupt:
    # Cierra la conexion al salir
    p.disconnect ()
    print("\ nConexion cerrada .")

