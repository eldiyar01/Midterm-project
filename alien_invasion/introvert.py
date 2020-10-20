import pygame

pygame.init()

display_width =500
display_height=500

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Running Introvert')

intro_width = 90
intro_height= 150
intro_x= display_width // 3
intro_y= display_height - intro_height - 100


clock = pygame.time.Clock()


class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        super(MySprite, self).__init__()
        self.images = []
        self.images.append(pygame.image.load('img/spaceship_1.png'))
        self.images.append(pygame.image.load('img/spaceship_2.png'))
        self.images.append(pygame.image.load('img/spaceship_3.png'))
        self.index = 0
        self.image = self.images[self.index]

        self.rect = pygame.Rect(5, 5, 120, 303)

    def update(self, screen):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        screen.blit(self.image, self.rect)

def start_game():
    my_introvert = MySprite()
    my_group = pygame.sprite.Group(my_introvert)
    game=True
    screen.fill((255, 255, 255))
    while game:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

        my_group.update(screen)
        
        pygame.display.update()
        clock.tick(10)

start_game()
