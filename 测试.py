import pygame

# 定义一些颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Button(pygame.sprite.Sprite):
    def __init__(self, text, position):
        super().__init__()
        self.text = text
        self.font = pygame.font.SysFont(None, 48)
        self.image = self.font.render(text, True, BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = position

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# 初始化Pygame
pygame.init()

# 创建屏幕
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Chess Game")

# 创建按钮
player_vs_player_button = Button("Player vs. Player", (400, 300))
player_vs_ai_button = Button("Player vs. AI", (400, 400))

# 创建按钮组
button_group = pygame.sprite.Group()
button_group.add(player_vs_player_button)
button_group.add(player_vs_ai_button)

# 主循环
running = True
while running:
    # 事件处理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 检查鼠标是否点击了按钮
            if player_vs_player_button.rect.collidepoint(event.pos):
                print("Player vs. Player button clicked")
            elif player_vs_ai_button.rect.collidepoint(event.pos):
                print("Player vs. AI button clicked")

    # 绘制按钮
    screen.fill(WHITE)
    button_group.draw(screen)

    # 刷新屏幕
    pygame.display.flip()

# 退出Pygame
pygame.quit()




# import pygame

# # 初始化Pygame
# pygame.init()

# # 创建屏幕
# screen = pygame.display.set_mode((800, 600))
# pygame.display.set_caption("Chess Game")

# # 加载图像
# button_image = pygame.image.load("C:/Users/22739/Desktop/xiangqi.png")

# # 绘制图像
# screen.blit(button_image, (100, 100))

# # 刷新屏幕
# pygame.display.flip()

# # 主循环
# running = True
# while running:
#     # 事件处理
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

# # 退出Pygame
# pygame.quit()
