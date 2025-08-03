# 처음 pygame을 import하고 왜 init을 해주어야하는가?

'''
pygame -> SDL(Simple DirectMedia Layer, C언어로 작성된 저수준 멀티미디어 라이브러리로 하드웨어와 직접적 소통(그래픽 카드와 연결, 사운드 카드 초기화, 키보드/마우스 입력 시스템 준비, 메모리 할당, os 윈도우 시스템과 연결..)) 라이브러리를 파이썬에서 사용하도록 만들어 놓은 것.
초기화하지 않으면 관련한 에러가 발생(초기화 전과 후의 값이 다름)

EX.
import pygame

print("초기화 전:")
print(f"디스플레이 초기화됨: {pygame.display.get_init()}")  # False
print(f"폰트 초기화됨: {pygame.font.get_init()}")           # False  
print(f"믹서 초기화됨: {pygame.mixer.get_init()}")         # False

pygame.init()

print("\n초기화 후:")
print(f"디스플레이 초기화됨: {pygame.display.get_init()}")  # True
print(f"폰트 초기화됨: {pygame.font.get_init()}")           # True
print(f"믹서 초기화됨: {pygame.mixer.get_init()}")         # True


처음부터 초기화 하지 않는 이유

리소스 절약 - 필요할 때만 하드웨어 점유
안전성 - 하드웨어 문제 시 에러 방지
유연성 - 개발자가 필요한 것만 선택적 초기화
충돌 방지 - 다른 프로그램과의 하드웨어 경쟁 방지
에러 처리 - 초기화 실패 시 대응 가능

import를 하는건 하드웨어와 연결되는게 아니라 모듈 코드를 가져오는 것으로 함수와 클래스 정의만 불러온다.
그렇기 때문에 init부터가 실제 초기화인 것이다. 모듈 접근만 가능한 상태.
'''