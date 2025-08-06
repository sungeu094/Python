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


# 이벤트 루프
running = True  # 게임이 진행중인가?
while running :
    for event in pygame.event.get():    # pygame에서 필수로 사용자의 입력(이벤트)을 계속해서 체크하는 부분이다.
        if event.type == pygame.QUIT:   # 창이 닫히는 이벤트가 발생하였는가?
            running = False
    
    
    screen.blit(background, (0, 0))     # 이미지를 가져와서 해당 위치에 넣음
    # screen.fill((0, 0, 255))   # 이미지를 가져오는 것이 아닌 색깔을 채움
    pygame.display.update()     
    # flip() vs update() : 인자가 없을 때는 동일하게 전체 화면 갱신이지만 update는 인자를 넣어줄 수 있다.
    
# running이 False가 된 상황 : pygame 종료
pygame.quit()