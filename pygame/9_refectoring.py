## 완전 리팩토링된 코드
from types import SimpleNamespace
import pygame

# ====================== 설정 및 상수 ===========================
class GameConfig:
    SCREEN_WIDTH = 480
    SCREEN_HEIGHT = 640
    TOTAL_TIME = 10
    TITLE = "SEWGAME"
    FPS = 60
    
    # 폰트 크기
    TIMER_FONT_SIZE = 40
    COORD_FONT_SIZE = 15
    
    # 색상
    WHITE = (255, 255, 255)
    
    # 위치
    TIMER_POS = (10, 10)

# ====================== 리소스 관리 클래스 ===========================
class GameResources:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((GameConfig.SCREEN_WIDTH, GameConfig.SCREEN_HEIGHT))
        pygame.display.set_caption(GameConfig.TITLE)
        self.clock = pygame.time.Clock()
        self.timer_font = pygame.font.Font(None, GameConfig.TIMER_FONT_SIZE)
        self.coord_font = pygame.font.Font(None, GameConfig.COORD_FONT_SIZE)
        self.background = pygame.image.load("C:/Users/sunge/OneDrive/Desktop/PythonWorkspace/pygame/background.png")

# ====================== 게임 캐릭터 클래스 ===========================
class GameCharacter:
    def __init__(self, image_path, x_pos, y_pos, speed=0.6):
        self.image = pygame.image.load(image_path)
        self.width, self.height = self.image.get_rect().size
        self.speed = speed
        
        # 초기 위치 설정 (경계 체크)
        self.x = max(0, min(x_pos, GameConfig.SCREEN_WIDTH - self.width))
        self.y = max(0, min(y_pos, GameConfig.SCREEN_HEIGHT - self.height))
        
        # 이동 벡터
        self.velocity_x = 0
        self.velocity_y = 0
        
    def move(self, dx, dy):
        """이동 벡터 설정"""
        self.velocity_x += dx
        self.velocity_y += dy
        
    def stop_horizontal(self):
        """수평 이동 정지"""
        self.velocity_x = 0
        
    def stop_vertical(self):
        """수직 이동 정지"""
        self.velocity_y = 0
        
    def update(self, dt):
        """위치 업데이트 및 경계 체크"""
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt
        self._check_boundaries()
        
    def _check_boundaries(self):
        """화면 경계 체크"""
        self.x = max(0, min(self.x, GameConfig.SCREEN_WIDTH - self.width))
        self.y = max(0, min(self.y, GameConfig.SCREEN_HEIGHT - self.height))
        
    def get_rect(self): # collision
        """충돌 감지용 rect 반환"""
        rect = self.image.get_rect()
        rect.left = self.x
        rect.top = self.y
        return rect
        
    def draw(self, screen):
        """캐릭터 그리기"""
        screen.blit(self.image, (self.x, self.y))
        
    def draw_coordinates(self, screen, font):
        """좌표 텍스트 그리기"""
        coord_text = f"({int(self.x)}, {int(self.y)})"
        text_surface = font.render(coord_text, True, GameConfig.WHITE)
        screen.blit(text_surface, (self.x, self.y))

# ====================== 게임 타이머 클래스 ===========================
class GameTimer:
    def __init__(self, total_time):
        self.total_time = total_time
        self.start_time = pygame.time.get_ticks()
        
    def get_remaining_time(self):
        """남은 시간 계산"""
        elapsed = (pygame.time.get_ticks() - self.start_time) / 1000
        return max(0, self.total_time - elapsed)
        
    def is_time_up(self):
        """시간 종료 여부"""
        return self.get_remaining_time() <= 0
        
    def draw(self, screen, font):
        """타이머 그리기"""
        remaining = int(self.get_remaining_time())
        timer_text = font.render(str(remaining), True, GameConfig.WHITE)
        screen.blit(timer_text, GameConfig.TIMER_POS)

# ====================== 이벤트 처리 클래스 ===========================
class EventHandler:
    @staticmethod
    def handle_events(character):
        """이벤트 처리"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_F5):
                return False
                
            EventHandler._handle_movement(event, character)
        return True
        
    @staticmethod
    def _handle_movement(event, character):
        """키보드 이동 처리"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character.move(-character.speed, 0)
            elif event.key == pygame.K_RIGHT:
                character.move(character.speed, 0)
            elif event.key == pygame.K_UP:
                character.move(0, -character.speed)
            elif event.key == pygame.K_DOWN:
                character.move(0, character.speed)
                
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                character.stop_horizontal()
            elif event.key in [pygame.K_UP, pygame.K_DOWN]:
                character.stop_vertical()

# ====================== 충돌 감지 클래스 ===========================
class CollisionDetector:
    @staticmethod
    def check_collision(obj1, obj2):
        """두 객체 간 충돌 체크"""
        return obj1.get_rect().colliderect(obj2.get_rect())

# ====================== 메인 게임 클래스 ===========================
class Game:
    def __init__(self):
        self.resources = GameResources()
        self.timer = GameTimer(GameConfig.TOTAL_TIME)
        self.event_handler = EventHandler()
        self.collision_detector = CollisionDetector()
        
        # 게임 객체 생성
        self.player = GameCharacter(
            "C:/Users/sunge/OneDrive/Desktop/PythonWorkspace/pygame/character.png", 
            100, 100
        )
        self.enemy = GameCharacter(
            "C:/Users/sunge/OneDrive/Desktop/PythonWorkspace/pygame/enemy.png", 
            300, 300
        )
        
        self.running = True
        
    def run(self):
        """메인 게임 루프"""
        while self.running:
            dt = self.resources.clock.tick(GameConfig.FPS)
            
            # 이벤트 처리
            self.running = self.event_handler.handle_events(self.player)
            
            # 게임 로직 업데이트
            self._update_game(dt)
            
            # 충돌 체크
            if self._check_collisions():
                break
                
            # 타이머 체크
            if self.timer.is_time_up():
                print("타임 아웃")
                break
                
            # 화면 그리기
            self._draw_all()
            
        pygame.quit()
        
    def _update_game(self, dt):
        """게임 로직 업데이트"""
        self.player.update(dt)
        # enemy는 정적이므로 업데이트 필요 없음
        
    def _check_collisions(self):
        """충돌 체크"""
        if self.collision_detector.check_collision(self.player, self.enemy):
            print("충돌, 게임 종료")
            return True
        return False
        
    def _draw_all(self):
        """모든 요소 그리기"""
        # 배경
        self.resources.screen.blit(self.resources.background, (0, 0))
        
        # 캐릭터들
        self.player.draw(self.resources.screen)
        self.enemy.draw(self.resources.screen)
        
        # UI
        self.player.draw_coordinates(self.resources.screen, self.resources.coord_font)
        self.timer.draw(self.resources.screen, self.resources.timer_font)
        
        pygame.display.update()

# ====================== 메인 실행 ===========================
if __name__ == "__main__":
    game = Game()
    game.run()