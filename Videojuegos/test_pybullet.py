import pybullet as p
import pybullet_data
import time

# Conectar al simulador de PyBullet (modo GUI)
physicsClient = p.connect(p.GUI)

# Configurar el path de datos de PyBullet
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Configurar la gravedad
p.setGravity(0, 0, -10)

# Cargar un plano
planeId = p.loadURDF("plane.urdf")

# Cargar un cubo sobre el plano
cubeStartPos = [0, 0, 1]
cubeStartOrientation = p.getQuaternionFromEuler([0, 0, 0])
cubeId = p.loadURDF("cube.urdf", cubeStartPos, cubeStartOrientation)


print("=" * 50)
print("PyBullet - Control de Cámara")
print("=" * 50)
print("Simulación física iniciada:")
print(f"- Plano ID: {planeId}")
print(f"- Cubo ID: {cubeId}")
print("\nControles del teclado:")
print("  - Flecha ARRIBA: Aumentar pitch (mirar arriba)")
print("  - Flecha ABAJO: Disminuir pitch (mirar abajo)")
print("  - Flecha IZQUIERDA: Rotar a la izquierda (yaw)")
print("  - Flecha DERECHA: Rotar a la derecha (yaw)")
print("  - W: Acercar cámara")
print("  - S: Alejar cámara")
print("\nCierra la ventana de simulación para terminar.")
print("=" * 50)

# Parámetros iniciales de la cámara
camera_distance = 3.0
camera_yaw = 45       # Ángulo horizontal (grados)
camera_pitch = -30    # Ángulo vertical (grados)
camera_target = [0, 0, 0.5]  # Mirar al cubo

# Velocidades de control
yaw_speed = 1.0
pitch_speed = 1.0
distance_speed = 0.1

# Configurar cámara inicial
p.resetDebugVisualizerCamera(camera_distance, camera_yaw, camera_pitch, camera_target)

# Códigos de teclas
ARROW_KEYS = {
    65297: "UP",
    65298: "DOWN", 
    65295: "LEFT",
    65296: "RIGHT"
}

print("\nValores de cámara iniciales:")
print(f"Distance: {camera_distance:.2f}, Yaw: {camera_yaw:.1f}°, Pitch: {camera_pitch:.1f}°")

# Ejecutar la simulación
step = 0
last_update = time.time()

try:
    while True:
        p.stepSimulation()
        time.sleep(1./240.)  # 240 Hz
        
        # Leer eventos del teclado
        keys = p.getKeyboardEvents()
        
        camera_updated = False
        
        # Procesar teclas presionadas
        for key, state in keys.items():
            if state == p.KEY_IS_DOWN or state == p.KEY_WAS_TRIGGERED:
                # Flechas del teclado
                if key == 65297:  # UP
                    camera_pitch += pitch_speed
                    camera_updated = True
                elif key == 65298:  # DOWN
                    camera_pitch -= pitch_speed
                    camera_updated = True
                elif key == 65295:  # LEFT
                    camera_yaw -= yaw_speed
                    camera_updated = True
                elif key == 65296:  # RIGHT
                    camera_yaw += yaw_speed
                    camera_updated = True
                # W y S para zoom
                elif key == ord('w'):
                    camera_distance = max(0.5, camera_distance - distance_speed)
                    camera_updated = True
                elif key == ord('s'):
                    camera_distance += distance_speed
                    camera_updated = True
        
        # Limitar ángulos
        camera_pitch = max(-89, min(89, camera_pitch))
        camera_yaw = camera_yaw % 360
        
        # Actualizar cámara si hubo cambios
        if camera_updated:
            p.resetDebugVisualizerCamera(camera_distance, camera_yaw, camera_pitch, camera_target)
            print(f"Distance: {camera_distance:.2f}, Yaw: {camera_yaw:.1f}°, Pitch: {camera_pitch:.1f}°")
        
        # Mostrar posición del cubo cada 2 segundos
        current_time = time.time()
        if current_time - last_update >= 2.0:
            cubePos, cubeOrn = p.getBasePositionAndOrientation(cubeId)
            cubeEuler = p.getEulerFromQuaternion(cubeOrn)
            print(f"\nPosición del cubo: x={cubePos[0]:.3f}, y={cubePos[1]:.3f}, z={cubePos[2]:.3f}")
            print(f"Orientación (Euler): roll={cubeEuler[0]:.3f}, pitch={cubeEuler[1]:.3f}, yaw={cubeEuler[2]:.3f}")
            last_update = current_time
        
        step += 1

except KeyboardInterrupt:
    print("\n\nSimulación detenida por el usuario.")

# Desconectar
p.disconnect()
print("Simulación completada!")
