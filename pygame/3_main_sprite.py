import pygame

pygame.init()   # 초기화 (반드시 필요)  만약 python-linting이 enable되어 있으면 오탐지가 될 수도 있음. CPython으로 되어있는 코드이면 python-linting이 탐지하기 어렵기 때문이다.

# 화면 크기 설정
screen_width = 480  # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("SEWGAME")   # 게임 이름

# 배경 이미지 불러오기
background = pygame.image.load("C:/Users/sunge/OneDrive/Desktop/PythonWorkspace/pygame/background.png")

# 캐릭터 불러오기 (캐릭터는 배경과 달리 움직이기 때문에 정보가 더 필요함)
character = pygame.image.load("C:/Users/sunge/OneDrive/Desktop/PythonWorkspace/pygame/character.png")
character_size = character.get_rect().size  # 이미지의 크기를 구해옴
character_width = character_size[0]         # 캐릭터 가로
character_height = character_size[1]        # 캐릭터 세로
character_x_pos = screen_width / 2          # 화면 가로의 중간에 위치
character_y_pos = screen_height             # 화면의 가장 밑에 위치

# 이벤트 루프
running = True  # 게임이 진행중인가?
while running :
    for event in pygame.event.get():    # pygame에서 필수로 사용자의 입력(이벤트)을 계속해서 체크하는 부분이다.
        if event.type == pygame.QUIT:   # 창이 닫히는 이벤트가 발생하였는가?
            running = False
    screen.blit(background, (0, 0))     # 이미지를 가져와서 해당 위치에 넣음
    # screen.fill((0, 0, 255))   # 이미지를 가져오는 것이 아닌 색깔을 채움
    
    screen.blit(character, (character_x_pos - character_width / 2, character_y_pos - character_height))  
    # 캐릭터 그리기 (화면의 중간이면서 가장 밑) -> 해당 좌표는 결국 왼쪽 상단을 지칭하기 때문에 잘 고려해야한다.
    
    pygame.display.update()     
    # flip() vs update() : 인자가 없을 때는 동일하게 전체 화면 갱신이지만 update는 인자를 넣어줄 수 있다.
    
    
    
    
# running이 False가 된 상황 : pygame 종료
pygame.quit()