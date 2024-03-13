import pygame
from pygame import display, Surface
from pygbag import aio as asyncio
from assets.scripts.settings import *
from assets.scripts.gameObject import GameObject
from assets.scripts.player import Player
from assets.scripts.enemy import Enemy
from assets.scripts.plugins.debug import debug

class Game: 
    # Initialize the game
    def __init__(self):
        
        # Window setup
        display.set_caption("RPG Game")
        self.size = self.width, self.height = WIDTH, HEIGHT
        self.screen = display.set_mode((self.size))
        self.clock = pygame.time.Clock()

        # Background
        self.bg_color = (255, 255, 255)
        self.bg_layer = Surface(self.screen.get_size())
        self.bg_layer.fill(self.bg_color)
        self.background = GameObject(0, 0, self.width, self.height, 'assets/backgrounds/old_base.png')

        # Treasure
        self.treasure = GameObject(375, 50, 48, 48, 'assets/sprites/treasure.png')

        self.level = 1.0

        self.reset_map()
    
    # Game Level
    def reset_map(self):
        # Player
        self.player = Player(375, 550, 48, 48, 'assets/avatars/player.png', 10)

        speed = 5 + (self.level * 5)

        if self.level >= 4.0:
            self.enemies = [
                Enemy(0, 450, 32, 32, 'assets/avatars/enemy.png', speed),
                Enemy(750, 300, 32, 32, 'assets/avatars/enemy.png', speed),
                Enemy(0, 150, 32, 32, 'assets/avatars/enemy.png', speed)
            ]
        elif self.level >= 2.0:
            self.enemies = [
                Enemy(0, 450, 32, 32, 'assets/avatars/enemy.png', speed),
                Enemy(750, 300, 32, 32, 'assets/avatars/enemy.png', speed)
            ]
        else:
            self.enemies = [
                Enemy(0, 450, 32, 32, 'assets/avatars/enemy.png', speed)
            ]

    # Draw the game objects
    def draw_objects(self):
        # Draw the background
        self.screen.blit(self.bg_layer, (0, 0))
        self.screen.blit(self.background.image, (self.background.x, self.background.y))
        self.screen.blit(self.treasure.image, (self.treasure.x, self.treasure.y))
        self.screen.blit(self.player.image, (self.player.x, self.player.y))
        
        for enemy in self.enemies:
            self.screen.blit(enemy.image, (enemy.x, enemy.y))
                    
        # Update the display
        debug('test')
        # debug(pygame.mouse.get_pos())
        # debug(pygame.mouse.get_pressed(),40)
        # debug('mouse!', pygame.mouse.get_pos()[1], pygame.mouse.get_pos()[0])
        display.flip()
        self.clock.tick(FPS)

    # Move the game objects
    def move_objects(self, player_dy):
        self.player.move(player_dy, self.height)
        for enemy in self.enemies: 
            enemy.move(self.width)
    
    def detect_collision(self, object_1, object_2):
        if object_1.y > (object_2.y + object_2.height):
            return False
        elif (object_1.y + object_1.height) < object_2.y:
            return False

        if object_1.x > (object_2.x + object_2.width):
            return False
        elif (object_1.x + object_1.width) < object_2.x:
            return False

        return True

    def check_if_collided(self):
        for enemy in self.enemies:
            if self.detect_collision(self.player, enemy):
                self.level = 1.0
                return True
        if self.detect_collision(self.player, self.treasure):
            self.level += 0.5
            return True
        return False

    # Game loop
    async def run_game_loop(self):
        
        player_dy = 0

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
                        player_dy = -1
                    elif event.key == pygame.K_DOWN:
                        player_dy = 1
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        player_dy = 0
            
            # Execute logic
            self.move_objects(player_dy)
            self.draw_objects()  # Draw the game objects
            await asyncio.sleep(0)  # Yield control for smooth execution

            # Collision detection
            if self.check_if_collided():
                self.reset_map()

    # Start the game
    def start(self):
        asyncio.run(self.run_game_loop()) # Run the main loop asynchronously
