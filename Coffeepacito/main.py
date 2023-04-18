
import EndScreen
import pygame as py, sys, random
from pygame import mixer

py.init()
mixer.init()

# constants
DIMEN = WIDTH, HEIGHT = 1024, 600
FPS = 120
# clock

clock = py.time.Clock()
clock.tick(FPS)
teaX, teaY = random.randint(1, 1024), random.randint(1, 600)

fireX, fireY = random.randint(1, 1024), random.randint(1, 600)
cokeX, cokeY = random.randint(1, 1024), random.randint(1, 600)

print(teaX, teaY, fireX, fireY, cokeX, cokeY)

screen = py.display.set_mode(DIMEN)
py.display.set_caption("Coffeepacito")
running = False
point = 0
high_score = 0
font = py.font.Font('assets/vampire-wars.ttf', 32)

endpic = py.image.load('assets/endscreen.png').convert_alpha()

#sound effects
cupbeansnd = mixer.Sound("sounds/cupbean.wav")
cupfiresnd = mixer.Sound("sounds/cupfire.mp3")
cupcokesnd = mixer.Sound("sounds/cupcoke.wav")
cupteasnd = mixer.Sound("sounds/cuptea.wav")
wallhitsnd = mixer.Sound("sounds/wallhit.ogg")

class Bean(py.sprite.Sprite):
    def __init__(self, path):
        super().__init__()
        self.image = py.image.load(path).convert_alpha()
        self.rect = self.image.get_rect()
        self.x_speed = 3
        self.y_speed = 2

    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        if self.rect.right >= 1024 or self.rect.left <= 0:
            self.x_speed *= -1
            mixer.Sound.play(wallhitsnd)

        if self.rect.bottom >= 600 or self.rect.top <= 0:
            self.y_speed *= -1 
            mixer.Sound.play(wallhitsnd)


class CoffeeCup(py.sprite.Sprite):
    def __init__(self, path):
        super().__init__()

        self.image = py.image.load(path)
        self.rect = self.image.get_rect()
        self.rect.center = (500, 500)

class Tea(py.sprite.Sprite):
    def __init__(self, path):
        super().__init__()
        self.image = py.image.load(path).convert_alpha()
        self.rect = self.image.get_rect()
        self.x_speed = 3
        self.y_speed = 2
        self.rect.center = (teaX, teaY)

    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        if self.rect.right >= 1024 or self.rect.left <= 0:
            self.x_speed *= -1
            mixer.Sound.play(wallhitsnd)

        if self.rect.bottom >= 600 or self.rect.top <= 0:
            self.y_speed *= -1
            mixer.Sound.play(wallhitsnd)


class Fire(py.sprite.Sprite):
    def __init__(self, path):
        super().__init__()
        self.image = py.image.load(path).convert_alpha()
        self.rect = self.image.get_rect()
        self.x_speed = 3
        self.y_speed = 2
        self.rect.center = (fireX, fireY)

    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        if self.rect.right >= 1024 or self.rect.left <= 0:
            self.x_speed *= -1
            mixer.Sound.play(wallhitsnd)

        if self.rect.bottom >= 600 or self.rect.top <= 0:
            self.y_speed *= -1
            mixer.Sound.play(wallhitsnd)

class Coke(py.sprite.Sprite):
    def __init__(self, path):
        super().__init__()
        self.image = py.image.load(path).convert_alpha()
        self.rect = self.image.get_rect()
        self.x_speed = 3
        self.y_speed = 2
        self.rect.center = (cokeX, cokeY)

    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        if self.rect.right >= 1024 or self.rect.left <= 0:
            self.x_speed *= -1
            mixer.Sound.play(wallhitsnd)

        if self.rect.bottom >= 600 or self.rect.top <= 0:
            self.y_speed *= -1
            mixer.Sound.play(wallhitsnd)

# player instant
cup = CoffeeCup('assets/playerCup.png')
cup_group = py.sprite.Group()
cup_group.add(cup)

#loading background
bg = py.image.load('assets/bg.png')

#enemy tea instant
tea = Tea("assets/tea.png")
enemy_group = py.sprite.Group()
enemy_group.add(tea)

#enemy fire instant
fire = Fire("assets/fire.png")
enemy_group.add(fire)

#bean instance
bean = Bean("assets/bean.png")
bean_group = py.sprite.Group()
bean_group.add(bean)

# coke instance 
coke = Coke('assets/coke.png')
coke_group = py.sprite.Group()
coke_group.add(coke)

font = py.font.Font('assets/vampire-wars.ttf', 32)


# game loop
while True:
    while not running:
        screen.blit(bg, (0, 0))
        
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()
        
        key_pressed = py.key.get_pressed()
        
        if key_pressed[py.K_UP]: 
            cup.rect.y -= 5

        if key_pressed[py.K_DOWN]:
            cup.rect.y += 5
                
        if key_pressed[py.K_LEFT]:
            cup.rect.x -= 5

        if key_pressed[py.K_RIGHT]:
            cup.rect.x += 5

        if cup.rect.right >= 1024: 
            cup.rect.x -= 5
            mixer.Sound.play(wallhitsnd)

        if cup.rect.left <= 0:
            cup.rect.x += 5
            mixer.Sound.play(wallhitsnd)

        if cup.rect.bottom >= 600:
            cup.rect.y -= 5
            mixer.Sound.play(wallhitsnd)

        if cup.rect.top <= 0:
            cup.rect.y += 5
            mixer.Sound.play(wallhitsnd)

        text = font.render(f'score: {point}', True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (WIDTH // 2, HEIGHT // 2)

        screen.blit(text, textRect)
        cup_group.draw(screen)
        enemy_group.draw(screen)
        bean_group.draw(screen)
        coke_group.draw(screen)
        tea.update()
        fire.update()
        bean.update()
        coke.update()

        if bean.rect.colliderect(cup.rect):
            bean.kill()
            bean_group.add(bean)
            bean.rect.center = (random.randint(1, 1024), random.randint(1, 600))
            bean_group.draw(screen)
            bean_group.update()
            point += 1
            mixer.Sound.play(cupbeansnd)
            

        with open('highscore.txt', 'r') as f: 
            score = f.read()

        if cup.rect.colliderect(fire.rect) or cup.rect.colliderect(tea.rect) or cup.rect.colliderect(coke.rect):
            
            if cup.rect.colliderect(fire.rect): mixer.Sound.play(cupfiresnd)
            elif cup.rect.colliderect(tea.rect): mixer.Sound.play(cupteasnd)
            elif cup.rect.colliderect(coke.rect): mixer.Sound.play(cupcokesnd)

            if point > int(score): score = point 
            
            with open('highscore.txt', 'w') as f: f.write(str(score))

            endscreen = EndScreen.EndScreen(score, point, WIDTH, HEIGHT)
            endscreen.run()
            break

        py.display.update()
