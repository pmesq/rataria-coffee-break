from config import Config
class Collision(Exception): 
    Ground = 1
    Flying = 2
    Side = 3

    def __init__(self, cod_type, height=Config.SCREEN_HEIGHT - 2*Config.BLOCK_SIZE, damage=0, rebound=0):
        super().__init__()
        self.type = cod_type
        self.height = height
        self.damage = damage
        self.rebound = rebound