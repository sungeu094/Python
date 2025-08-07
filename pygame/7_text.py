### 충돌처리

import pygame

pygame.init()   # 초기화 (반드시 필요)  만약 python-linting이 enable되어 있으면 오탐지가 될 수도 있음. CPython으로 되어있는 코드이면 python-linting이 탐지하기 어렵기 때문이다.

## 화면 크기 설정
screen_width = 480  # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width,screen_height))

## 화면 타이틀 설정
pygame.display.set_caption("SEWGAME")   # 게임 이름

## FPS
clock = pygame.time.Clock()

## 배경 이미지 불러오기
background = pygame.image.load("C:/Users/sunge/OneDrive/Desktop/PythonWorkspace/pygame/background.png")

## 캐릭터 불러오기 (캐릭터는 배경과 달리 움직이기 때문에 정보가 더 필요함)
character = pygame.image.load("C:/Users/sunge/OneDrive/Desktop/PythonWorkspace/pygame/character.png")
character_size = character.get_rect().size  # 이미지의 크기를 구해옴
character_width = character_size[0]         # 캐릭터 가로
character_height = character_size[1]        # 캐릭터 세로
character_x_pos = screen_width / 2 - character_width / 2        # 화면 가로의 중간에 위치
character_y_pos = screen_height - character_height              # 화면의 가장 밑에 위치


## enemy 캐릭터
enemy = pygame.image.load("C:/Users/sunge/OneDrive/Desktop/PythonWorkspace/pygame/enemy.png")
enemy_size = enemy.get_rect().size  # 이미지의 크기를 구해옴
enemy_width = enemy_size[0]         # 캐릭터 가로
enemy_height = enemy_size[1]        # 캐릭터 세로
enemy_x_pos = screen_width / 2 - enemy_width / 2        # 화면 가로의 중간에 위치
enemy_y_pos = screen_height / 2 - enemy_height / 2              # 화면의 가장 밑에 위치


## 이동할 좌표
to_x = 0
to_y = 0


## 이동 속도
character_speed = 0.6

## 폰트 정의
game_font = pygame.font.Font(None, 40)  # 폰트 객체 생성(폰트, 크기)

## 총 시간
total_time = 10

## 시작 시간
start_ticks = pygame.time.get_ticks()   # 시작 tick을 받아옴

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
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
            
        if event.type == pygame.KEYUP:  # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
                
    character_x_pos += to_x * dt        
    character_y_pos += to_y * dt 

    coord_text = f"({int(character_x_pos)}, {int(character_y_pos)})"
    font = pygame.font.Font(None, 15)
    text_surface = font.render(coord_text, True, (255,255,255))     # render의 첫 인자가 str이기 때문에 f-string을 통해 coord_text를 만들어준 것이다.

    ## 가로 경계값 처리    
    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width :
        character_x_pos = screen_width - character_width
    
    
    ## 세로 경계값 처리
    if character_y_pos < 0 :
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height :
        character_y_pos = screen_height - character_height
    
    
    ## 충돌 처리
    character_rect = character.get_rect() 
    # rect는 순서대로 인자가 left, top, width, height이기 때문에 우리는 left, top만 바꿔주면 된다.
    
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos
    
    ## 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌, 게임 종료")
        running = False
        pass
    
    screen.blit(background, (0, 0))     # 이미지를 가져와서 해당 위치에 넣음
    # screen.fill((0, 0, 255))   # 이미지를 가져오는 것이 아닌 색깔을 채움
    
    ## 캐릭터 그리기 -> 두번째 인자로 들어가는 좌표는 결국 왼쪽 상단을 지칭하기 때문에 잘 고려해야한다.    
    screen.blit(character, (character_x_pos, character_y_pos))  
    screen.blit(text_surface, (character_x_pos, character_y_pos))
    
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
    
    ## 타이머 - 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000   
    
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255,255,255))
    screen.blit(timer, (10,10))
    
    if total_time - elapsed_time <= 0:
        print("타임 아웃")
        running = False
    
    
    pygame.display.update()     
    # flip() vs update() : 인자가 없을 때는 동일하게 전체 화면 갱신이지만 update는 인자를 넣어줄 수 있다.

## 잠시 대기
pygame.time.delay(2000)

## running이 False가 된 상황 : pygame 종료
pygame.quit()