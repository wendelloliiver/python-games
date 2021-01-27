import pyxel

WIDTH = 196
HEIGHT = 128

RACKET_WIDTH = 8
RACKET_HEIGHT = 32

RACKET_COLOR = 7
BALL_COLOR = 7

score_racket01 = 0
score_racket02 = 0

# -----------------------------------------------

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        # 10 frames por segundos
        self.framerate = pyxel.DEFAULT_FPS % 20

        # velocidade da bola em [x, y]
        # velores da velocidade armazenado em lista (0, 1, 2, 3 ... n)
        # speed[0] = x, speed[1] = y
        self.speed = [.3, .3]

    # checar e atualizar os valores da bola
    def update(self):
        self.x -= self.speed[0] * self.framerate
        self.y -= self.speed[1] * self.framerate

        self.collision_with_wall()
    
    # checar a colisão com o topo da tela
    # ou em baixo da tela
    def collision_with_wall(self):
        if self.y < 0:
            self.speed[1] *= -1
            
        if self.y > HEIGHT:
            self.speed[1] *= -1

    # desenhar a bola
    def draw(self):
        pyxel.circ(self.x, self.y, 2, BALL_COLOR)

# -----------------------------------------------

class Racket:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # desenhar a raquete
    def draw(self):
        pyxel.rect(self.x - 4, self.y - 16, RACKET_WIDTH, RACKET_HEIGHT, RACKET_COLOR)

# -----------------------------------------------

class App:
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, caption='Pong For Two!', fps=21)

        self.ball = Ball(WIDTH / 2, HEIGHT / 2)
        
        self.racket1 = Racket(8, 64)
        self.racket2 = Racket(WIDTH - 8, 64)
        
        pyxel.run(self.update, self.draw)

    # sistema de pontuação
    def score(self):
        global score_racket01
        global score_racket02

        if self.ball.x < 0:
            score_racket02 += 1
        elif self.ball.x > WIDTH:
            score_racket01 += 1

    # resetar a positcao da bola ao sair da tela
    def reset(self):
        if self.ball.x < - 2 or self.ball.x > WIDTH + 2:
            self.ball.x = WIDTH / 2
            self.ball.y = HEIGHT / 2

    # loop principal do jogo
    def update(self):
        self.framerate = pyxel.DEFAULT_FPS % 20
        
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        # BOLA
        self.ball.update()

        # RAQUETE ESQUERDA
        if pyxel.btn(pyxel.KEY_A):
            self.racket1.y -= self.framerate * 0.5
        elif pyxel.btn(pyxel.KEY_Z):
            self.racket1.y += self.framerate * 0.5

        # RAQUETE DIREITA
        if pyxel.btn(pyxel.KEY_UP):
            self.racket2.y -= self.framerate * 0.5
        elif pyxel.btn(pyxel.KEY_DOWN):
            self.racket2.y += self.framerate * 0.5


        # COLISAO DA BOLA COM A RAQUETE ESQUERDA
        if self.ball.x < self.racket1.x + 5 and self.ball.y > self.racket1.y - 18 \
           and self.ball.y < self.racket1.y + 18:
            self.ball.speed[0] = self.hit_factor(self.racket1.x, self.ball.x, RACKET_WIDTH)
            self.ball.speed[1] = self.hit_factor(self.racket1.y, self.ball.y, RACKET_HEIGHT)
        # COLISAO DA BOLA COM A RAQUETE DIREITA
        if self.ball.x > self.racket2.x - 5 and self.ball.y < self.racket2.y + 18 \
           and self.ball.y > self.racket2.y - 18:
            self.ball.speed[0] = self.hit_factor(self.racket2.x, self.ball.x, RACKET_WIDTH - 4)
            self.ball.speed[1] = self.hit_factor(self.racket2.y, self.ball.y, RACKET_HEIGHT)

        self.reset()
        self.score()
        
    # checar e retornar o valor da direção da bola
    # ao ser rebatido pela raquete
    def hit_factor(self, racket_position, ball_position, racket_size):
        v = (racket_position - ball_position) / racket_size
        return -.3 if v < 0 else .3

    # desenho do jogo principal
    def draw(self):
        pyxel.cls(0)

        self.ball.draw()
        
        self.racket1.draw()
        self.racket2.draw()

        pyxel.text((WIDTH / 2) - 20, 10, str(score_racket01), 7)
        pyxel.text((WIDTH / 2) + 20, 10, str(score_racket02), 7)

        pyxel.line(WIDTH / 2, 0, WIDTH / 2, HEIGHT, 7)

# -----------------------------------------------

App() # execução do jogo!
