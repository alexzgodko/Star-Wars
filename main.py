from constants import *
import pygame
from class_player import Player
from class_explosion import Explosion
from class_meteor import Meteor
from class_bullet import Bullet
import random


def shoot_outside_class(self):
    """Creates a bullet. There must be a minimum amount of time between shots.

    Args:
        None

    Returns:
        None
    """

    now = pygame.time.get_ticks()
    if now - self.last_update > 300:
        self.last_update = now
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)
        shoot_sound.play()


Player.shoot = shoot_outside_class


def explosion_update_outside_class(self):
    """Displays animation frames sequentially based on elapsed time.

    Args:
        None

    Returns:
        None
    """

    now = pygame.time.get_ticks()
    if now - self.last_update > self.frame_rate:
        self.last_update = now
        self.frame += 1
        if self.frame == len(explosion_anim[self.size]):
            self.kill()
        else:
            center = self.rect.center
            self.image = explosion_anim[self.size][self.frame]
            self.rect = self.image.get_rect()
            self.rect.center = center


Explosion.update = explosion_update_outside_class


def draw_text(surf, text, size, x, y):
    font = pygame.font.SysFont("Britannic Bold", size, True)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def newmeteor():
    m = Meteor()
    all_sprites.add(m)
    meteors.add(m)


def draw_shield_bar(surf, x, y, pct):
    if pct < 0:
        pct = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 10
    fill = (pct / 100) * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, GREEN, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)


# Оѝновной цикл игры
running = True
game_over = False
start = True


def show_go_screen():
    global running
    screen.blit(background, background_rect)
    draw_text(screen, "STAR", 65, WIDTH / 2, HEIGHT / 4)
    draw_text(screen, "WARS", 65, WIDTH / 2, HEIGHT / 3)
    draw_text(screen, "Стрелки - перемещатьѝѝ, Пробел - ѝтрелѝть", 27,
              WIDTH / 2, HEIGHT / 2)
    draw_text(screen, "Нажмите любую клавишу длѝ продолжениѝ",
              22, WIDTH / 2, HEIGHT * 0.6)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                waiting = False

        if event.type == pygame.KEYUP:
            waiting = False


def show_game_over_screen(score):
    global running
    screen.blit(background, background_rect)
    draw_text(screen, "GAME", 56, WIDTH / 2, HEIGHT / 4)
    draw_text(screen, "OVER", 56, WIDTH / 2, HEIGHT / 3)
    draw_text(screen, "Your Score: " + str(score), 30,
              WIDTH / 2, HEIGHT / 2)

    font = pygame.font.SysFont("Britannic Bold", 30, True)
    restart_button_rect = pygame.Rect(
        WIDTH // 2 - BUTTON_WIDTH // 2, HEIGHT // 2 + 70, BUTTON_WIDTH, BUTTON_HEIGHT)
    restart_button_text = font.render("Restart Game", True, WHITE)
    restart_button_text_rect = restart_button_text.get_rect(
        center=restart_button_rect.center)

    screen.blit(restart_button_text, restart_button_text_rect)
    pygame.draw.rect(screen, WHITE, restart_button_rect, 3)

    pygame.display.flip()

    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if restart_button_rect.collidepoint(mouse_pos):
                    waiting = False


# Оѝновное окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(
    "Star Wars 1.0")
clock = pygame.time.Clock()

# Загрузка изображений длѝ взрывов
explosion_anim = {}
explosion_anim['lg'] = []
explosion_anim['sm'] = []
for i in range(9):
    filename = 'regularExplosion0{}.png'.format(i)
    img = pygame.image.load(path.join(img_dir, filename)).convert()
    img.set_colorkey(BLACK)
    img_lg = pygame.transform.scale(img, (75, 75))
    explosion_anim['lg'].append(img_lg)
    img_sm = pygame.transform.scale(img, (32, 32))
    explosion_anim['sm'].append(img_sm)

# Загрузка мелодий игры
shoot_sound = pygame.mixer.Sound(path.join(snd_dir, 'sfx_laser1.ogg'))
expl_sounds = []
for snd in ['sfx_shieldDown.ogg', 'sfx_shieldUp.ogg']:
    expl_sounds.append(pygame.mixer.Sound(path.join(snd_dir, snd)))


# Загрузка игровой графики
background = pygame.image.load(
    path.join(img_dir, "purple.png")).convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
background_rect = background.get_rect()
player_img = pygame.image.load(
    path.join(img_dir, "playerShip1_orange.png")).convert()
bullet_img = pygame.image.load(path.join(img_dir, "laserRed16.png")).convert()

for img in meteor_list:
    meteor_images.append(pygame.image.load(path.join(img_dir, img)).convert())


Bullet.image = bullet_img
Player.image = pygame.transform.scale(player_img, (50, 38))


while running:
    if start:
        show_go_screen()
        if running == False:
            break
        all_sprites = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        meteors = pygame.sprite.Group()
        start = False
        game_over = False
        player = Player()
        all_sprites.add(player)
        for i in range(8):
            newmeteor()
        score = 0

    if game_over:
        show_game_over_screen(score)
        if running == False:
            break
        game_over = False
        all_sprites = pygame.sprite.Group()
        meteors = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        player = Player()
        all_sprites.add(player)
        for i in range(8):
            newmeteor()
        score = 0

    clock.tick(FPS)

    # Рендеринг игрового полѝ
    screen.blit(background, background_rect)
    all_sprites.update()
    all_sprites.draw(screen)
    draw_text(screen, str(score), 25, WIDTH / 2, 10)
    draw_shield_bar(screen, 5, 5, player.shield)

    # Отображение ѝкрана
    pygame.display.flip()

    # Проверка, не ударил ли метеор игрока
    hits = pygame.sprite.spritecollide(
        player, meteors, True, pygame.sprite.collide_circle)
    for hit in hits:
        player.shield -= hit.radius * 3
        expl = Explosion(hit.rect.center, 'sm', explosion_anim)
        all_sprites.add(expl)
        newmeteor()
        if player.shield <= 0:
            game_over = True
            # running = False

    # Проверка, не попала ли пулѝ в метеор
    hits = pygame.sprite.groupcollide(meteors, bullets, True, True)

    for hit in hits:
        # Переѝчет add_speed
        if (score < 500 and score + (50 - hit.radius) // 2 >= 500):
            add_speed = 4
        elif (score < 1000 and score + (50 - hit.radius) // 2 >= 1000):
            add_speed = 7
        elif (score < 1500 and score + (50 - hit.radius) // 2 >= 1500):
            add_speed = 10

        score += (50 - hit.radius) // 2
        random.choice(expl_sounds).play()
        expl = Explosion(hit.rect.center, 'lg', explosion_anim)
        all_sprites.add(expl)
        newmeteor()

    # Отѝлеживание ѝобытий
    for event in pygame.event.get():
        # Выход из приложениѝ
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()


# Выход из игры
pygame.quit()
