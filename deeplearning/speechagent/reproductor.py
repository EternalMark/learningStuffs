# reproductor.py
import pygame
import keyboard
import os
import time

# Configura la carpeta de audios
CARPETA = "./audios"
EXTENSIONES = (".mp3", ".wav", ".ogg")

# Inicializa el reproductor
pygame.mixer.init()
audios = [os.path.join(CARPETA, f) for f in os.listdir(CARPETA) if f.endswith(EXTENSIONES)]
playlist = []
index = 0

def reproducir(i):
    if 0 <= i < len(audios):
        pygame.mixer.music.load(audios[i])
        pygame.mixer.music.play()
        print(f"Reproduciendo: {os.path.basename(audios[i])}")

print("Controles:")
print(" [ESPACIO] reproducir/pausar | [n] siguiente | [a] agregar a playlist | [s] guardar playlist | [q] salir")

while True:
    if keyboard.is_pressed("space"):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()
        keyboard.wait("space")

    elif keyboard.is_pressed("n"):
        index = (index + 1) % len(audios)
        reproducir(index)
        keyboard.wait("n")

    elif keyboard.is_pressed("a"):
        playlist.append(audios[index])
        print(f"Añadido: {os.path.basename(audios[index])}")
        keyboard.wait("a")

    elif keyboard.is_pressed("s"):
        with open("playlist.txt", "w") as f:
            for item in playlist:
                f.write(item + "\n")
        print("Playlist guardada.")
        keyboard.wait("s")

    elif keyboard.is_pressed("q"):
        print("Saliendo.")
        break

    time.sleep(0.1)