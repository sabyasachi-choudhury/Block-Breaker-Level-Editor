# Imports
import pygame
from pygame.locals import *
import object_classes as cls

# Init
pygame.init()

# Norm vars
s_width = 900
s_height = 800
run = True

# Global vars
dragging = False
testing = False
extra_detect = False
blue_in = True
red_in = True
yellow_in = True
green_in = True
im_in = True
mb_in = True
current_sprite = 0
mov_coords = {}
detect = False

# Screen
screen = pygame.display.set_mode((s_width, s_height))


# Def drag and drop
def drag_drop(body):
    global dragging, current_sprite, blue_in, red_in, yellow_in, green_in, im_in, mb_in, moving_blocks, detect
    if event.type == MOUSEBUTTONDOWN:
        if body.rect.collidepoint(pygame.mouse.get_pos()):
            dragging = True
            current_sprite = body

    if event.type == MOUSEBUTTONUP:
        dragging = False

    if event.type == MOUSEMOTION:
        if dragging:
            current_sprite.rect.center = pygame.mouse.get_pos()
            if current_sprite == white_block:
                blue_in = False
            elif current_sprite == red_block:
                red_in = False
            elif current_sprite == yellow_block:
                yellow_in = False
            elif current_sprite == grey_block:
                green_in = False
            elif current_sprite == im_block:
                im_in = False
            elif current_sprite == mov_block:
                mb_in = False


# Objects
white_block = cls.BlueBlock()
red_block = cls.RedBlock()
grey_block = cls.GreenBlock()
yellow_block = cls.YellowBlock()
im_block = cls.Immovable()
mov_block = cls.Moving()

# Groups and obj lists
editor_sprites = pygame.sprite.Group(white_block, red_block, grey_block, yellow_block, im_block, mov_block)
moving_blocks = pygame.sprite.Group(mov_block)

print("Remember, d and t!")

# Main loop
while run:

    # Screen fill
    screen.fill((0, 0, 0))

    # Event detection
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False

        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                run = False
            if event.key == K_BACKSPACE:
                current_sprite.kill()

            if event.key == K_t:
                testing = not testing
                extra_detect = True
            if event.key == K_d:
                detect = True

        # Drag and drop call
        for sprite in editor_sprites:
            drag_drop(sprite)

    # Elements space
    pygame.draw.rect(screen, (0, 255, 0), (700, 0, 200, 800), 0)

    # Replacing empty places
    if not blue_in:
        editor_sprites.add(cls.BlueBlock())
        blue_in = True
    elif not red_in:
        editor_sprites.add(cls.RedBlock())
        red_in = True
    elif not yellow_in:
        editor_sprites.add(cls.YellowBlock())
        yellow_in = True
    elif not green_in:
        editor_sprites.add(cls.GreenBlock())
        green_in = True
    elif not im_in:
        editor_sprites.add(cls.Immovable())
        im_in = True
    elif not mb_in:
        x = cls.Moving()
        editor_sprites.add(x)
        mb_in = True

    # First creation of moving_blocks
    for s in editor_sprites:
        if s.id == 'MB' and s.rect.centerx != 800:
            moving_blocks.add(s)

    # Refining moving_blocks
    for b in moving_blocks:
        if b.rect.centerx == 800:
            moving_blocks.remove(b)

    # Moving and resetting
    if testing:
        for x in moving_blocks:
            x.motion()
    elif not testing and extra_detect:
        a = 0
        for x in moving_blocks:
            a += 1
            x.rect.center = mov_coords['block ' + str(a)]
        extra_detect = False

    # Detecting new positions
    if detect:
        index = 0
        for mb in moving_blocks:
            index += 1
            mov_coords['block ' + str(index)] = mb.rect.center

    # Resetting detect so it only lasts one frame
    detect = False

    for a in moving_blocks:
        for b in editor_sprites:
            if b.id == 'IM' and a.rect.colliderect(b):
                a.vel = -a.vel

    # Blit
    for s in editor_sprites:
        screen.blit(s.surf, s.rect)
        if s.id != 'MB':
            s.rect.center = [round(s.rect.centerx/50) * 50, round(s.rect.centery/15) * 15]

    # Flip
    pygame.display.flip()

# Quit
pygame.quit()

# Generating nuclear codes
code = []

for x in editor_sprites:
    if x.rect.centerx == 800:
        editor_sprites.remove(x)

for x in editor_sprites:
    code.append([x.id, x.rect.centerx, x.rect.centery])

print(code)
# i = 0
# for x in moving_blocks:
#     i += 1
# print(i)
print(mov_coords)