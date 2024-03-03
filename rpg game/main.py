import pygbag.aio as asyncio
import pygame

pygame.init()

# Window setup
pygame.display.set_caption("RPG Game")
size = width, height = 800, 600
screen = pygame.display.set_mode((size))
bg_layer = pygame.Surface(screen.get_size())
bg_color = (255, 255, 255)
bg_layer.fill(bg_color)
# bg_image = pygame.image.load("assets/background.png")
# background = pygame.transform.scale(bg_image, (screen.get_size()))

async def main():
    # Game Loop
    running = True
    while running:
        
        # Event handling
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
        
        # Draw the background
        screen.blit(bg_layer, (0, 0))
#         screen.blit(background, (0, 0))
        
        # Update the display
        pygame.display.flip()  # Immediately update the display
        await asyncio.sleep(0)  # Yield control for smooth execution

if __name__ == "__main__":
    asyncio.run(main())  # Run the main loop asynchronously
