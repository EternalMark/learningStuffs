#include <SDL2/SDL.h>
#include <iostream>
#include <unordered_map> //https://en.cppreference.com/w/cpp/container/unordered_map

// Constantes para la ventana
const int WINDOW_WIDTH = 800;
const int WINDOW_HEIGHT = 600;

// Estructura para almacenar el estado de un botón
struct ButtonState
{
    bool isPressed;
    Uint32 pressTime;
};

// Umbral de tiempo para considerar una pulsación como larga (en milisegundos)
const Uint32 LONG_PRESS_THRESHOLD = 500;

// Mapa para almacenar el estado de los botones
std::unordered_map<Uint8, ButtonState> buttonStates;

int main(int argc, char *argv[])
{
    // Inicializar SDL
    if (SDL_Init(SDL_INIT_VIDEO | SDL_INIT_JOYSTICK | SDL_INIT_GAMECONTROLLER) != 0)
    {
        std::cerr << "Error inicializando SDL: " << SDL_GetError() << std::endl;
        return 1;
    }

    // Comprobar cuántos joysticks están conectados
    int numJoysticks = SDL_NumJoysticks();
    if (numJoysticks < 1)
    {
        std::cout << "No se encontraron joysticks." << std::endl;
    }
    else
    {
        std::cout << "Se encontraron " << numJoysticks << " joystick(s)." << std::endl;
    }

    // Abrir el primer joystick
    SDL_GameController *gameController = nullptr;
    if (SDL_IsGameController(0))
    {
        gameController = SDL_GameControllerOpen(0);
        if (gameController)
        {
            std::cout << "Controlador abierto: " << SDL_GameControllerName(gameController) << std::endl;
        }
        else
        {
            std::cerr << "No se pudo abrir el controlador: " << SDL_GetError() << std::endl;
        }
    }
    else
    {
        std::cerr << "El dispositivo 0 no es un controlador de juegos compatible." << std::endl;
    }

    // Crear una ventana
    SDL_Window *window = SDL_CreateWindow("Evento de Gamepad SDL2",
                                          SDL_WINDOWPOS_CENTERED,
                                          SDL_WINDOWPOS_CENTERED,
                                          WINDOW_WIDTH,
                                          WINDOW_HEIGHT,
                                          0);
    if (!window)
    {
        std::cerr << "Error creando la ventana: " << SDL_GetError() << std::endl;
        SDL_Quit();
        return 1;
    }

    // Crear un renderer
    SDL_Renderer *renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);
    if (!renderer)
    {
        std::cerr << "Error creando el renderer: " << SDL_GetError() << std::endl;
        SDL_DestroyWindow(window);
        SDL_Quit();
        return 1;
    }

    // Bucle principal
    bool running = true;
    SDL_Event event;
    while (running)
    {
        while (SDL_PollEvent(&event))
        {
            if (event.type == SDL_QUIT)
            {
                running = false;
            }
            else if (event.type == SDL_CONTROLLERBUTTONDOWN)
            {
                // buttonStates[event.cbutton.button] = {true, SDL_GetTicks()};
                buttonStates[event.cbutton.button].isPressed = true;
                buttonStates[event.cbutton.button].pressTime = SDL_GetTicks();
            }
            else if (event.type == SDL_CONTROLLERBUTTONUP)
            {
                ButtonState &state = buttonStates[event.cbutton.button];
                Uint32 currentTime = SDL_GetTicks();
                Uint32 pressDuration = currentTime - state.pressTime;
                state.isPressed = false;
                
                std::cout << std::endl << "Se mantienen los siguientes botones presionados: "<< std::endl;

                for (const auto& [key, value] : buttonStates)// Lo mismo que la linea de arriba
                { 
                    if (value.isPressed == true)
                    {
                        Uint32 d = currentTime - value.pressTime;
                        std::cout << "Botón " << static_cast<int>(key) << "  presionado por " << d << "ms" << std::endl;
                    }
                }
            }
        }

        // Renderizar
        SDL_SetRenderDrawColor(renderer, 0, 0, 255, 255); // Azul
        SDL_RenderClear(renderer);
        SDL_RenderPresent(renderer);
    }

    // Limpiar recursos
    if (gameController)
    {
        SDL_GameControllerClose(gameController);
    }
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();

    return 0;
}