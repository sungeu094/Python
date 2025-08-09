'''
Quiz : 하늘에서 떨어지는 똥 피하기 게임을 만드시오.

[게임 조건]
1. 캐릭터는 화면 가장 아래에 위치, 좌우로만 이동 가능
2. 똥은 화면 가장 위에서 떨어짐. x 좌표는 매번 랜덤으로 설정
3. 캐릭터가 똥을 피하면 다음 똥이 다시 떨어짐
4. 캐릭터가 똥과 충돌하면 게임 종료
5. FPS는 30으로 고정
'''

#Sol
import pygame

class GameConfig:
    SCREEN_WIDTH = 480
    SCREEN_HEIGHT = 640
    
    CHARACTER_WIDTH, CHARACTER_HEIGHT = (70, 70)
    
    pass


class GameResource:
    # 게임 실행에 필요한 자원 모음
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((GameConfig.SCREEN_WIDTH, GameConfig.SCREEN_HEIGHT))
        pass
    pass


class GameCharacter:    # 피하는 사람, 내려오는 장애물(하나는 x좌표 고정, 하나는 y좌표 고정)
    def __init__(self, image_path, x_pos = GameConfig.SCREEN_WIDTH, y_pos = -GameConfig.CHARACTER_HEIGHT, speed = 0.6):
        self.image = pygame.image.load(image_path)
        self.width, self.height = self.image.get_rect().size
        self.speed = speed
        
        self.x = max(0, min(x_pos, GameConfig.SCREEN_WIDTH - self.width))
        self.y = max(0, min(y_pos, GameConfig.SCREEN_HEIGHT - self.height))

        self.velocity_x = 0
        self.velocity_y = 0
    
    

class EventHandler:
    '''
    떨어지기(위아래)
    피하기(좌우)
    게임 종료
    '''
    def __init__(self):
        pass
    pass

class GameTimer:
    def __init__(self):
        pass
    pass

class Game:
    def __init__(self):
        self.resources = GameResource()
        self.running = True
    
    def run(self):
        running  = True
        while self.running:
            pass
        pygame.quit() 



#===================================================
if __name__ == "__main__":
    game = Game()
    game.run()