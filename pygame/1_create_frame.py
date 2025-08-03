import pygame

pygame.init()   # 초기화 (반드시 필요)  만약 python-linting이 enable되어 있으면 오탐지가 될 수도 있음. CPython으로 되어있는 코드이면 python-linting이 탐지하기 어렵기 때문이다.

# 화면 크기 설정
screen_width = 480  # 가로 크기
screen_height = 640 # 세로 크기
pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("SEWGAME")   # 게임 이름

# 이벤트 루프
running = True  # 게임이 진행중인가?
while running :
    for event in pygame.event.get():    # pygame에 꼭 필요한 것으로 사용자의 입력을 계속해서 체크하는 부분이다.
        pass
        

# running이 False가 된 상황 : pygame 종료
pygame.quit()