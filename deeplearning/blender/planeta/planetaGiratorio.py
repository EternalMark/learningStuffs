# blender /mnt/SSD2T/GITHUB/learningStuffs/deeplearning/blender/planeta/planeta.blend --background --python /mnt/SSD2T/GITHUB/learningStuffs/deeplearning/blender/planeta/planetaGiratorio.py --render-anim
# blender /ruta/a/tu/archivo/planeta_animado.blend --background --render-output /ruta/para/guardar/frames/ --render-anim

# blender /mnt/SSD2T/GITHUB/learningStuffs/deeplearning/blender/diorama/cube_diorama.blend --background --render-output /mnt/SSD2T/GITHUB/learningStuffs/deeplearning/blender/diorama/frames/ --render-anim


import bpy
import math
import random

# --- Configuración ---
planet_radius = 3
particle_count = 500
emission_rate = 10  # Partículas emitidas por frame (ajustable)
particle_lifetime = 100  # Número de frames que vive una partícula
emission_speed = 0.5
planet_location = (0, 0, 0)

# --- Limpiar la escena por defecto ---
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)


# --- Crear el planeta ---
bpy.ops.mesh.primitive_uv_sphere_add(radius=planet_radius, location=planet_location)
planet = bpy.context.object
planet.name = "Planeta"

# --- Crear el sistema de partículas como un data block ---
particle_data = bpy.data.particles.new(name="EmisionParticulasData")

# --- Añadir un ParticleSettings al objeto ---
particle_system = planet.particle_systems.new(name="EmisionParticulas")
particle_system.settings = particle_data
settings = particle_system.settings

# --- Configurar las propiedades de las partículas ---
settings.count = particle_count
settings.frame_start = 1
settings.frame_end = 1
settings.lifetime = particle_lifetime
settings.emit_from = 'FACE'
settings.normal_factor = emission_speed
settings.render_type = 'HALO'

# --- Configurar la rotación del planeta ---
def rotate_planet(frame):
    planet.rotation_euler[2] = math.radians(frame * 2) # Rotación en el eje Z

# --- Crear el controlador de animación (handler) ---
def update_particles(scene):
    frame = scene.frame_current
    rotate_planet(frame)

    # Emitir nuevas partículas cada cierto número de frames (simulando una tasa de emisión)
    if frame % (bpy.context.scene.render.fps // emission_rate) == 0:
        bpy.ops.ptcache.bake_all(bake=False) # Esto puede ser necesario para actualizar la simulación

bpy.app.handlers.frame_change_post.append(update_particles)

# --- Configurar la escena para la animación ---
bpy.context.scene.frame_start = 1
bpy.context.scene.frame_end = 300 # Duración de la animación en frames
bpy.context.scene.render.fps = 24 # Cuadros por segundo


# Especifica la ruta y el nombre del archivo donde quieres guardar
filepath = "./planeta.blend"

# Guarda el archivo .blend
bpy.ops.wm.save_as_mainfile(filepath=filepath)

print(f"Archivo guardado en: {filepath}")

print("¡Planeta giratorio con emisión de partículas creado!")