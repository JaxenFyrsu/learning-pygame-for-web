import pygbag.aio as asyncio
import pygame

class Game: 
    # Initialize the game
    def __init__(self):
        
        # Window setup
        pygame.display.set_caption("RPG Game")
        self.size = self.width, self.height = 800, 800
        self.screen = pygame.display.set_mode((self.size))

        # Background
        self.bg_color = (255, 255, 255)
        self.bg_layer = pygame.Surface(self.screen.get_size())
        self.bg_layer.fill(self.bg_color)
        bg_image = pygame.image.load('assets/background.png')
        self.background = pygame.transform.scale(bg_image, (self.screen.get_size()))

        # Treasure
        treasure_image = pygame.image.load('assets/treasure.png')
        self.treasure = pygame.transform.scale(treasure_image, (50, 50))

    # Draw the game objects
    def draw_objects(self):
        # Draw the background
        self.screen.blit(self.bg_layer, (0, 0))
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.treasure, (375, 50))
                    
        # Update the display
        pygame.display.flip()
            
    # Game loop
    async def run_game_loop(self):
        running = True
        while running:
            
            # Event handling
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    running = False
            
            # Execute logic
            self.draw_objects()  # Draw the game objects
            await asyncio.sleep(0)  # Yield control for smooth execution

    # Start the game
    def start(self):
        asyncio.run(self.run_game_loop()) # Run the main loop asynchronously