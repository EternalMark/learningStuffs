#include <SDL2/SDL.h>
#include <iostream>

int main(int argc, char* argv[]) {
    // Inicializar SDL
    if (SDL_Init(SDL_INIT_VIDEO | SDL_INIT_JOYSTICK | SDL_INIT_GAMECONTROLLER) != 0) {
        std::cerr << "Error inicializando SDL: " << SDL_GetError() << std::endl;
        return 1;
    }

    // Comprobar cuántos joysticks están conectados
    int numJoysticks = SDL_NumJoysticks();
    if (numJoysticks < 1) {
        std::cout << "No se encontraron joysticks." << std::endl;
    } else {
        std::cout << "Se encontraron " << numJoysticks << " joystick(s)." << std::endl;
    }

    // Abrir el primer joystick
    SDL_GameController* gameController = nullptr;
    if (SDL_IsGameController(0)) {
        gameController = SDL_GameControllerOpen(0);
        if (gameController) {
            std::cout << "Controlador abierto: " << SDL_GameControllerName(gameController) << std::endl;
        } else {
            std::cerr << "No se pudo abrir el controlador: " << SDL_GetError() << std::endl;
        }
    } else {
        std::cerr << "El dispositivo 0 no es un controlador de juegos compatible." << std::endl;
    }

    // Crear una ventana
    SDL_Window* window = SDL_CreateWindow("Evento de Gamepad SDL2",
                                          SDL_WINDOWPOS_CENTERED,
                                          SDL_WINDOWPOS_CENTERED,
                                          800, 600, 0);
    if (!window) {
        std::cerr << "Error creando la ventana: " << SDL_GetError() << std::endl;
        SDL_Quit();
        return 1;
    }

    // Crear un renderer
    SDL_Renderer* renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);
    if (!renderer) {
        std::cerr << "Error creando el renderer: " << SDL_GetError() << std::endl;
        SDL_DestroyWindow(window);
        SDL_Quit();
        return 1;
    }

    // Bucle principal
    bool running = true;
    SDL_Event event;
    while (running) {
        while (SDL_PollEvent(&event)) {
            if (event.type == SDL_QUIT) {
                running = false;
            } else if (event.type == SDL_CONTROLLERBUTTONDOWN) {
                std::cout << "Botón del gamepad presionado: " << (int)event.cbutton.button << std::endl;
            } else if (event.type == SDL_CONTROLLERBUTTONUP) {
                std::cout << "Botón del gamepad soltado: " << (int)event.cbutton.button << std::endl;
            } else if (event.type == SDL_CONTROLLERAXISMOTION && (int)event.caxis.axis !=0 && (int)event.caxis.axis !=1 ) {
                std::cout << "Moooovimiento del eje del gamepad: " << (int)event.caxis.axis
                          << " Valor: " << event.caxis.value << std::endl;
            }
        }

        // Renderizar
        SDL_SetRenderDrawColor(renderer, 0, 0, 255, 255);  // Azul
        SDL_RenderClear(renderer);
        SDL_RenderPresent(renderer);
    }

    // Limpiar recursos
    if (gameController) {
        SDL_GameControllerClose(gameController);
    }
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();

    return 0;
}