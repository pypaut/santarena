#include <SDL2/SDL.h>

int main(void) {

    SDL_Init(SDL_INIT_VIDEO|SDL_INIT_AUDIO);

    SDL_Window *window = SDL_CreateWindow(
        "An SDL2 window",                  // window title
        SDL_WINDOWPOS_UNDEFINED,           // initial x position
        SDL_WINDOWPOS_UNDEFINED,           // initial y position
        640,                               // width, in pixels
        480,                               // height, in pixels
        SDL_WINDOW_OPENGL                  // flags - see below
    );

    SDL_Delay(3000);

    SDL_DestroyWindow(window);

    SDL_Quit();

    return 0;
}
