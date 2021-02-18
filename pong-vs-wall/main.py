import pyxel

# raquete
velocidade_x = .3

RAQUETE_LARGURA = 32
RAQUETE_ALTURA = 8

class Bola:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.fps = pyxel.DEFAULT_FPS % 20

        self.direcao = [.3, .3]
    
    def update(self):
        self.x -= self.direcao[0] * self.fps
        self.y -= self.direcao[1] * self.fps

        if self.x <= 0 or self.x >= 128:
            self.direcao[0] *= -1
        
        if self.y <= 0: # or self.y >= 196:
            self.direcao[1] *= -1
        
        # limite do movimento da bola na parte debaixo da tela!
        if self.y > 206:
            
            self.x = 64
            self.y = 196 / 2

            self.direcao[1] *= -1

    def draw(self):
        pyxel.circ(self.x, self.y, 2, 7)

class Raquete:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.fps = pyxel.DEFAULT_FPS % 20
    
    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x -= velocidade_x * self.fps
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += velocidade_x * self.fps

    def draw(self):
        pyxel.rect(self.x - 16, self.y, RAQUETE_LARGURA, RAQUETE_ALTURA, 7)

class Pong:
    def __init__(self):
        pyxel.init(128, 196, caption='Pong Vs Wall', fps=21)

        self.raquete = Raquete(64, 176)
        self.bola = Bola(64, 196 / 2)

        pyxel.run(self.update, self.draw)
    
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        
        self.raquete.update()
        self.bola.update()

        # limite do movimento da raquete!
        if self.raquete.x < 0:
            self.raquete.x = 0
        if self.raquete.x > 128:
            self.raquete.x = 128

        # colisão da bola com a raquete!
        if (self.raquete.x + 16 > self.bola.x and self.raquete.x - 16 < self.bola.x and self.raquete.y == self.bola.y):
            self.bola.direcao[0] = self.angulo_colisao(self.raquete.x, self.bola.x, RAQUETE_LARGURA)
            self.bola.direcao[1] = self.angulo_colisao(self.raquete.y, self.bola.y, RAQUETE_ALTURA)
    
    def angulo_colisao(self, raquete_posicao, bola_posicao, raquete_tamanho):
        v = (raquete_posicao - bola_posicao) / raquete_tamanho
        return -.3 if v < 0 else .3
    
    def draw(self):
        pyxel.cls(0)

        self.raquete.draw()
        self.bola.draw()
    
Pong()