from const import *
from enum import Enum
from map import Map


class ObstacleType(Enum):
    PLANT_POT = 1
    ROOM = 2

class Obstacle:
    def __init__(self, originX, originY, obstacle_type: ObstacleType):
        self.originX = originX
        self.originY = originY
        self.pattern = obstacle_type
    
    def check_obs_size_ROOM(map: Map, originX, originY) -> bool:
        if (originX + 3 <= map.row 
            and originY + 2 <= map.col):
                return True
        
    def check_obs_size(map: Map, originX, originY, obstacle_type: ObstacleType) -> bool:
        if (obstacle_type == ObstacleType.PLANT_POT):
             return True # 1x1 obstacle, always drawable
        if (obstacle_type == ObstacleType.ROOM):
            return Obstacle.check_obs_size_ROOM(map, originX, originY)