import pygbag.aio as asyncio
import pygame
from gameObject import GameObject
from player import Player

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
        self.background = GameObject(0, 0, self.width, self.height, 'assets/background.png')

        # Treasure
        self.treasure = GameObject(375, 50, 50, 50, 'assets/treasure.png')

        # Player
        self.player = Player(375, 700, 50, 50, 'assets/player.png', 10)

    # Draw the game objects
    def draw_objects(self):
        # Draw the background
        self.screen.blit(self.bg_layer, (0, 0))
        self.screen.blit(self.background.image, (self.background.x, self.background.y))
        self.screen.blit(self.treasure.image, (self.treasure.x, self.treasure.y))
        self.screen.blit(self.player.image, (self.player.x, self.player.y))
                    
        # Update the display
        pygame.display.flip()
            
    # Game loop
    async def run_game_loop(self):
        
        player_direction = 0

        # Main game loop
        running = True
        while running:
            
            # Event handling
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        player_direction = -1
                    elif event.key == pygame.K_DOWN:
                        player_direction = 1
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        player_direction = 0
            
            # Execute logic
            self.player.move(player_direction)
            self.draw_objects()  # Draw the game objects
            await asyncio.sleep(0)  # Yield control for smooth execution

    # Start the game
    def start(self):
        asyncio.run(self.run_game_loop()) # Run the main loop asynchronously
