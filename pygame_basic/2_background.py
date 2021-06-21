import pygame

pygame.init() #초기화 (반드시 필요)

#화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("First game") # 게임 이름

#배경 이미지 불러오기 경로의 슬러시를 하나씩 더 넣어줘서 탈출문자를 하던가 역슬러쉬를 넣어줌
background = pygame.image.load("C:\\Users\\User\\Desktop\\python_game\\pygame_basic\\background.png")

 # 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님

    # screen.fill((0, 0, 255)) RGB값을 넣어서 배경에 색을 넣을 수도 있음
    screen.blit(background, (0, 0)) #배경 그리기

    pygame.display.update() #  게임화면을 다시 그리기!

# pygame 종료
pygame.quit()
