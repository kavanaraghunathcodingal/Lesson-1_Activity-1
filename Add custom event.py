import pygame

# Initialize
pygame.init()
window = pygame.display.set_mode((800,600))
pygame.display.set_caption("Sprites with Custom Event")

# Custom event
CHANGE_COLOR = pygame.USEREVENT + 1

# Sprite class
class Box(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect(center=(x, y))

    def change_color(self, new_color):
        self.color = new_color
        self.image.fill(self.color)

# Create sprites
box1 = Box(150, 300, (255, 0, 0))   # Red
box2 = Box(650, 300, (0, 0, 255))   # Blue

# Sprite group
all_sprites = pygame.sprite.Group(box1, box2)

# Main loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            # Trigger custom event
            pygame.event.post(pygame.event.Event(CHANGE_COLOR))
        elif event.type == CHANGE_COLOR:
            # Change colors when custom event is fired
            box1.change_color((0, 255, 0))   # Green
            box2.change_color((255, 255, 0)) # Yellow

    window.fill((255,255,255))
    all_sprites.draw(window)
    pygame.display.flip()

pygame.quit()
