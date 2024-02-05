import pygame

pygame.init()
window = pygame.display.set_mode((500, 150))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 100)


text = 'Hello World'
text_len = 0
typewriter_event = pygame.USEREVENT+1
pygame.time.set_timer(typewriter_event, 100)
text_surf = None

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == typewriter_event:
            text_len += 1
            if text_len > len(text):
                text_len = 0
            text_surf = None if text_len == 0 else font.render(text[:text_len], True, (255, 255, 128))

    if text_surf:
        window.blit(text_surf, text_surf.get_rect(midleft = window.get_rect().midleft).move(40, 0))
    pygame.display.flip()

pygame.quit()
exit()