## 코드 정리
from types import SimpleNamespace
import pygame

# ====================== 기본 초기화 ===========================
## 상수 namespace로 나열
GameConfig = SimpleNamespace(
    SCREEN_WIDTH = 480,
    SCREEN_HEIGHT = 640,
    TOTAL_TIME = 10,
    TITLE = "SEWGAME"
)

## 초기화 함수
def init_pygame():
    pygame.init()
    screen = pygame.display.set_mode((GameConfig.SCREEN_WIDTH, GameConfig.SCREEN_HEIGHT))
    pygame.display.set_caption(GameConfig.TITLE)
    clock = pygame.time.Clock()
    start_ticks = pygame.time.get_ticks()
    return screen, clock, start_ticks

screen, clock, start_ticks = init_pygame()

## 폰트 정의
game_font = pygame.font.Font(None, 40)  # 폰트 객체 생성(폰트, 크기)
# ===============================================================

# ===================== 사용자 게임 초기화 ======================
background = pygame.image.load("C:/Users/sunge/OneDrive/Desktop/PythonWorkspace/pygame/background.png")

## 캐릭터 불러오기 (캐릭터는 배경과 달리 움직이기 때문에 정보가 더 필요함)
class GameCharacter :
    def __init__(self, directory, x_pos, y_pos):
        self.directory = directory
        self.character = pygame.image.load(self.directory)
        self.character_size = self.character.get_rect().size  
        self.character_width = self.character_size[0]         
        self.character_height = self.character_size[1]
        self.x = (
            max(0, x_pos)
            if x_pos <= GameConfig.SCREEN_WIDTH - self.character_width
            else GameConfig.SCREEN_WIDTH - self.character_width
        )
        self.y = (
            max(0, y_pos)
            if y_pos <= GameConfig.SCREEN_HEIGHT - self.character_height 
            else GameConfig.SCREEN_HEIGHT - self.character_height 
        )
        ## 이동할 좌표
        self.to_x = 0
        self.to_y = 0
        
        ## 이동 속도
        self.character_speed = 0.6
        
    def moving(self, to_x, to_y):
        self.to_x += to_x
        self.to_y += to_y
        print(self.to_x, self.to_y, sep = "  ")
        
    def check_position(self):
        self.x = (
            max(0, self.x)
            if self.x <= GameConfig.SCREEN_WIDTH - self.character_width
            else GameConfig.SCREEN_WIDTH - self.character_width
        )
        self.y = (
            max(0, self.y)
            if self.y <= GameConfig.SCREEN_HEIGHT - self.character_height 
            else GameConfig.SCREEN_HEIGHT - self.character_height 
        )
    
    def collision(self) :  
        ## 충돌 처리
        character_rect = self.character.get_rect() 
        character_rect.left = self.x
        character_rect.top = self.y
        
        return character_rect
    
    def draw_coord_text(self, screen, font):
        coord_text= f"({int(self.x)}, {int(self.y)})"
        text_surface = font.render(coord_text, True, (255,255,255))
        screen.blit(text_surface, (self.x, self.y))

myCharacter = GameCharacter("C:/Users/sunge/OneDrive/Desktop/PythonWorkspace/pygame/character.png", 100,100)
enemy = GameCharacter("C:/Users/sunge/OneDrive/Desktop/PythonWorkspace/pygame/enemy.png", 300, 300)
    


## 이벤트 루프
running = True  # 게임이 진행중인가?
while running :
    dt = clock.tick(60)     # 게임화면의 초당 프레임 수를 설정
    # print("fps : " + str(clock.get_fps()))
    
    for event in pygame.event.get():    # pygame에서 필수로 사용자의 입력(이벤트)을 계속해서 체크하는 부분이다.
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_F5):   # 창이 닫히는 이벤트가 발생하였는가?
            running = False
        
        # 키보드 입력을 통한 캐릭터 이동
        if event.type == pygame.KEYDOWN:    # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:  # 캐릭터를 왼쪽으로
                myCharacter.moving((-1)*myCharacter.character_speed, 0)
            elif event.key == pygame.K_RIGHT:
                myCharacter.moving(myCharacter.character_speed, 0)
            elif event.key == pygame.K_UP:
                myCharacter.moving(0, (-1)*myCharacter.character_speed)
            elif event.key == pygame.K_DOWN:
                myCharacter.moving(0, myCharacter.character_speed)
            
        if event.type == pygame.KEYUP:  # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                myCharacter.to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                myCharacter.to_y = 0
                
    myCharacter.x += myCharacter.to_x * dt
    myCharacter.y += myCharacter.to_y * dt
    myCharacter.check_position()
    
    print(myCharacter.x, myCharacter.y)

    ## 충돌 처리 & 체크 (ok)
    myRect = myCharacter.collision()
    enemyRect = enemy.collision()
    
    if myRect.colliderect(enemyRect):
        print("충돌, 게임 종료")
        running = False
    
    ## 배경 그리기 (ok)
    screen.blit(background, (0, 0))     # 이미지를 가져와서 해당 위치에 넣음
    # fill((0, 0, 255))   # 이미지를 가져오는 것이 아닌 색깔을 채움
    
    ## 캐릭터 그리기 (ok)    
    screen.blit(myCharacter.character, (myCharacter.x, myCharacter.y))  
    screen.blit(enemy.character, (enemy.x, enemy.y))
    
    ## 내 캐릭터의 좌표 (ok)
    myCharacter.draw_coord_text(screen, pygame.font.Font(None, 15))
    
    ## 타이머 - 경과 시간 계산 (ok)
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000   
    timer = game_font.render(str(int(GameConfig.TOTAL_TIME - elapsed_time)), True, (255,255,255))
    screen.blit(timer, (10,10))
    
    if GameConfig.TOTAL_TIME - elapsed_time <= 0:
        print("타임 아웃")
        running = False
    
    
    pygame.display.update()     
    # flip() vs update() : 인자가 없을 때는 동일하게 전체 화면 갱신이지만 update는 인자를 넣어줄 수 있다.

## 잠시 대기
#pygame.time.delay(2000)

## running이 False가 된 상황 : pygame 종료
pygame.quit()