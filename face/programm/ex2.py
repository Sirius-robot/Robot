import pygame

pygame.init()

screen = pygame.display.set_mode((300, 300))
s_r = screen.get_rect()
player = pygame.Rect((100, 100, 50, 50))
timer = pygame.time.Clock()
flash = 0
grow = True
color = pygame.color.Color('Black')

E_OUTSIDE = pygame.USEREVENT  + 1
E_MOUSE   = pygame.USEREVENT  + 2

conditions = [ # blink if player is outside screen
              (lambda: not s_r.contains(player), pygame.event.Event(E_OUTSIDE)),
               # if mouse if over player then grow and shrink player
              (lambda: player.collidepoint(pygame.mouse.get_pos()), pygame.event.Event(E_MOUSE))]

while True:
    # generate events from conditions
    map(pygame.event.post, [e for (c, e) in conditions if c()])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raise
        elif event.type == E_OUTSIDE and not flash:
            flash = 5
        elif event.type == E_MOUSE:
            if grow:
                player.inflate_ip(4, 4)
                grow = player.width < 75
            else:
                player.inflate_ip(-4, -4)
                grow = player.width < 50

    flash = max(flash - 1, 0)
    if flash % 2:
        color = pygame.color.Color('White')

    pressed = pygame.key.get_pressed()
    l, r, u, d = map(lambda x: x*4, [pressed[k] for k in pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s])
    player.move_ip((-l + r, -u + d))

    screen.fill(color)
    color = pygame.color.Color('Black')

    pygame.draw.rect(screen, pygame.color.Color('Grey'), player)

    pygame.display.flip()
    timer.tick(25)