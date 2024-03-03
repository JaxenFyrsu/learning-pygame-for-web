import pygame, pygbag.aio as asyncio  # Keep import temporarily for compatibility checks
from game import Game

async def main():
    
    game = Game()
    await game.run_game_loop()  # Assuming run_game_loop made asynchronous

if __name__ == '__main__':
    # Remove Pygame initialization for the web environment
    # pygame.init()  # Not needed for pygbag

    asyncio.run(main())
