#blender --background --python /blender-4.4.3-linux-x64/ejemplos/llantaCarreta.py
#blender --background --python /mnt/SSD2T/GITHUB/learningStuffs/deeplearning/blender/llantaCarreta.py 
#
# blender --background --python /mnt/SSD2T/GITHUB/learningStuffs/deeplearning/blender/llantaCarreta.py  --render-output /mnt/SSD2T/GITHUB/learningStuffs/deeplearning/blender/ --render-format PNG --render-frame 100
# blender --background --python /mnt/SSD2T/GITHUB/learningStuffs/deeplearning/blender/planetaGiratorio.py  --render-output /mnt/SSD2T/GITHUB/learningStuffs/deeplearning/blender/ --render-format PNG --render-frame 100



import bpy
import bmesh
import math

def crear_aro(radio_exterior, radio_interior, segmentos=32, nombre="AroCarreta"):
    """Crea el aro exterior de la llanta."""
    bpy.ops.mesh.primitive_torus_add(
        major_radius=radio_exterior,
        minor_radius=radio_exterior - radio_interior,
        major_segments=segmentos,  # Cambiar 'segments' a 'major_segments'
        minor_segments=segmentos // 4,
        align='WORLD',
        location=(0, 0, 0),
        rotation=(0, 0, 0)
    )
    aro = bpy.context.object
    aro.name = nombre
    return aro

def crear_radio(longitud, ancho=0.2, grosor=0.1, nombre="RadioCarreta"):
    """Crea un radio de la llanta."""
    bpy.ops.mesh.primitive_cube_add(size=1, align='WORLD', location=(0, 0, 0))
    radio = bpy.context.object
    radio.name = nombre
    radio.scale = (ancho, grosor, longitud)
    return radio

def posicionar_radio(radio_objeto, angulo_rad, radio_interior_aro):
    """Posiciona un radio individual."""
    x = radio_interior_aro * math.cos(angulo_rad)
    y = radio_interior_aro * math.sin(angulo_rad)
    radio_objeto.location = (x, y, 0)
    # Apuntar el radio hacia el centro (eje Z)
    direccion = -math.atan2(y, x)
    radio_objeto.rotation_euler = (0, 0, direccion)

def crear_llanta(radio_exterior=2.0, radio_interior=1.5, num_radios=8):
    """Crea la llanta completa de la carreta."""
    # 1. Crear el aro
    aro = crear_aro(radio_exterior, radio_interior)

    # 2. Crear y posicionar los radios
    radios_padre = bpy.data.objects.new("Radios", None)
    bpy.context.collection.objects.link(radios_padre)

    for i in range(num_radios):
        angulo = 2 * math.pi * i / num_radios
        radio = crear_radio(longitud=radio_exterior - radio_interior)
        posicionar_radio(radio, angulo, radio_interior)
        radio.parent = radios_padre

    # 3. Centrar todo
    llanta_padre = bpy.data.objects.new("LlantasCarreta", None)
    bpy.context.collection.objects.link(llanta_padre)
    aro.parent = llanta_padre
    radios_padre.parent = llanta_padre

    return llanta_padre

if __name__ == "__main__":
    # Deseleccionar todo
    bpy.ops.object.select_all(action='DESELECT')

    # Eliminar objetos existentes (opcional)
    # bpy.ops.object.delete(use_global=False)

    # Crear la llanta
    llanta = crear_llanta()

    print("¡Llanta de carreta creada!")