'''надо будет сделать главное меню еще, и чтобы можно было нажимать короче на кнопочки и они становились другого цвета и ваще ебать кайф тогда'''
import pygame
from sys import exit
from random import randint

class Player (pygame.sprite.Sprite):
    def __init__(self, side, speed=None):
        super().__init__()
        self.side = side
        self.speed = 8
        self.aispeed = speed
        if side == 'player1':
            self.image = pygame.image.load ('Game_pong\graphics_2ndgame\Player1.png').convert_alpha()
            self.rect = self.image.get_rect(midbottom = (50, 300))
        elif side == 'player2' or side == "AI":
            self.image = pygame.image.load ('Game_pong\graphics_2ndgame\Player2.png').convert_alpha()
            self.rect = self.image.get_rect (midbottom = (750, 300))
        
    def movement (self):
        keys = pygame.key.get_pressed()
        if self.side == 'player1':
            if keys[pygame.K_w]: self.rect.y += -self.speed
            elif keys[pygame.K_s]: self.rect.y += self.speed
        elif self.side == 'player2':
            if keys[pygame.K_KP8]: self.rect.y += -self.speed
            elif keys[pygame.K_KP2]: self.rect.y += self.speed
        elif self.side == 'AI':
            if self.rect.y < ball.sprite.rect.y: self.rect.y += self.aispeed
            if self.rect.bottom > ball.sprite.rect.bottom: self.rect.bottom += -self.aispeed
            if keys[pygame.K_BACKSPACE]:
                self.rect.midbottom = (750,300)
            
        if self.rect.bottom > 600: self.rect.bottom = 600
        if self.rect.top < 0: self.rect.top = 0
        
    def update (self):
        self.movement()

class Ball (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load ('Game_pong\graphics_2ndgame/ball.png')
        self.rect = self.image.get_rect (midbottom = (350, 300))
        self.max_speed = 7
        self.speedX = self.max_speed
        self.speedY = 0
    
    def movement (self):
        self.rect.x += self.speedX
        self.rect.y += self.speedY
        if self.rect.y < 0: 
            self.rect.y = 0
            self.speedY *= -1
            
        if self.rect.y > 575: 
            self.rect.y = 575
            self.speedY *= -1
        
    def update (self):
        self.movement()

class Button:
    def __init__ (self, x, y, width, height, text = 'Button', font=30):
        #essentials
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font = pygame.font.Font(None, font)
        #surf and rect
        self.buttonrect = pygame.Rect((self.x, self.y), (self.width, self.height))
        self.text_surface = self.font.render(text, True, 'black' )
        self.text_rect = self.text_surface.get_rect(center = self.buttonrect.center)
        #miscellaneous
        self.color = "white"
        self.is_pressed = False
    
    def draw (self):
        pygame.draw.rect(display, self.color, self.buttonrect, border_radius=20)
        display.blit (self.text_surface, self.text_rect)

    def check_click (self):
        mouse_pos = pygame.mouse.get_pos()
        if self.buttonrect.collidepoint(mouse_pos):
            self.color = 'light blue'
            if pygame.mouse.get_pressed()[0]:
                self.color = 'blue'
                self.is_pressed = True
            else:
                if self.is_pressed:
                    self.is_pressed = False
                    return True
        else:
            self.is_pressed = False
            self.color = 'white'
        
    def update (self):
        self.draw()
        return self.check_click()
        
def collision ():
    if pygame.sprite.spritecollide(ball.sprite, players, False):
        if ball.sprite.speedX < 0:
            ball.sprite.speedX *= -1
            dif_in_y = ball.sprite.rect.centery - player1.rect.centery 
            reduction_factor = (player1.rect.height / 2) / ball.sprite.max_speed
            y_vel = dif_in_y / reduction_factor
            ball.sprite.speedY = y_vel
            
        else: 
            ball.sprite.speedX *= -1
            dif_in_y = ball.sprite.rect.centery - player2.rect.centery 
            reduction_factor = (player2.rect.height / 2) / ball.sprite.max_speed
            y_vel = dif_in_y / reduction_factor
            ball.sprite.speedY = y_vel

def ball_restart ():
    pygame.time.delay (500)
    ball.sprite.rect.midbottom = (350, 300)
    ball.sprite.speedY = randint (0, 5)

def display_score ():
    global score1, score2
    if ball.sprite.rect.x > Width: 
        score1 += 1
        ball_restart()
    
    elif ball.sprite.rect.x < -50: 
        score2 += 1
        ball_restart()
            
    score_surface = smallerfont.render(f'{score1}          {score2}', True, 'black')
    display.blit(score_surface, (Width/2 - (score_surface.get_width() / 2), 
                                Height / 2 - (score_surface.get_height() / 2)))

def main_menu ():
    global difficulty_menu_control
    global player1 
    global player2
    global game_over
    
    if not difficulty_menu_control:
        main_bg = pygame.Surface((Width, Height))
        main_bg.fill('black')
        display.blit(main_bg, (0,0))
        main_menu_text = Font.render ('Pong Game', True, 'white')
        display.blit (main_menu_text, (Width/2 - (main_menu_text.get_width() / 2), 
                                    Height / 7 - (main_menu_text.get_height() / 2)))
        
        if button_singleplayer.update():
            difficulty_menu_control = True
            
        #adding players here
        elif button_multiplayer.update (): 
            player1 = Player(side='player1')
            players.add(player1)
            player2 = Player(side='player2')
            players.add(player2)
            return True
        
        elif button_quit.update():
            pygame.quit()
            exit()
    else:
        return difficulty_menu() 
        
def difficulty_menu ():
    global difficulty_menu_control
    global player1
    global player2
    
    bg = pygame.Surface((Width, Height))
    bg.fill ('black')
    display.blit(bg, (0,0))
    difficulty_text = Font.render ('Choose Difficulty', True, 'white')
    display.blit (difficulty_text, (Width/2 - (difficulty_text.get_width() / 2), 
                                Height / 7 - (difficulty_text.get_height() / 2)))

    if button_easy.update(): #easy dif
        player1 = Player(side='player1')
        players.add(player1)
        player2 = Player(side='AI', speed=5)
        players.add(player2)
        return True
    
    elif button_medium.update(): #medium dif
        player1 = Player(side='player1')
        players.add(player1)
        player2 = Player(side='AI', speed=7)
        players.add(player2)
        return True
    
    elif button_hard.update(): #hard
        player1 = Player(side='player1')
        players.add(player1)
        player2 = Player(side='AI', speed=8)
        players.add(player2)
        return True
    
    elif button_back.update():
        difficulty_menu_control = False
    
def gameover_screen ():
    global score1, score2, game_over
    if score1 > score2: 
        p1win_text = Font.render('Player 1 has won!', True, 'red')
        display.blit(p1win_text, (Width/2 - (p1win_text.get_width() / 2), 
                                Height / 5 - (p1win_text.get_height() / 2)) )
    elif score2 > score1:
        p1win_text = Font.render('Player 2 has won!', True, 'green')
        display.blit(p1win_text, (Width/2 - (p1win_text.get_width() / 2), 
                                Height / 5 - (p1win_text.get_height() / 2)) )
    if button_restart.update():
        game_over = False
        score1 = 0
        score2 = 0

def main ():
    global score1, score2, game_over
    game_over = False
    mainmenu = True
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        if not mainmenu:
            if not game_over:
                display.blit(tent_background, (0,0))
                
                players.draw(display)
                players.update()
                
                ball.draw(display)
                ball.update()
                
                collision()
                display_score()
                
                if score1 >= 10 or score2 >= 10:
                    game_over = True
            else:
                gameover_screen()
            if button_back_tomenu.update():
                    mainmenu = True
                    players.empty()
                    score1 = 0
                    score2 = 0
                    
        else: 
            if main_menu():
                mainmenu = False
                
        pygame.display.update()
        framerate.tick(60)

pygame.init()

Width = 800
Height = 600
display = pygame.display.set_mode((Width, Height))
pygame.display.set_caption('Digital Football')
framerate = pygame.time.Clock()
Font = pygame.font.Font(None, 50)
smallerfont = pygame.font.Font (None, 35)

tent_background = pygame.Surface((800,600))
tent_background.fill('grey')

ball = pygame.sprite.GroupSingle()
ball.add (Ball()) 

players = pygame.sprite.Group()

score1 = 0
score2 = 0

button_singleplayer = Button((Width/2 - 125 ), 200, 250, 50, 'Singleplayer')
button_multiplayer = Button ((Width/2 - 125 ), 300, 250, 50, 'Multiplayer')
button_easy = Button ((Width/2 - 125 ), 150, 250, 50, 'Easy')
button_medium = Button ((Width/2 - 125 ), 250, 250, 50, 'Medium')
button_hard = Button ((Width/2 - 125 ), 350, 250, 50, 'Hard')
button_back = Button (25, 550, 100, 35, 'Back', font=25)

button_back_tomenu = Button (25, 550, 100, 35, 'To menu', font=25)
button_restart = Button ((Width/2 - 125 ), 150, 250, 50, 'Restart')

button_quit = Button (25, 550, 100, 35, 'Quit', font=25)


difficulty_menu_control = False

if __name__ == '__main__': 
    main()
