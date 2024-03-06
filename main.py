from pyboy import PyBoy
with PyBoy('./test-game/build/rom/game.gb') as pyboy:
    while not pyboy.tick():
        pass