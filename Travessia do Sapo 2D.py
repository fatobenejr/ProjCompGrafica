from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

global windowWidth,windowHeight,ho,wo,condicao
global pause,texto,xtexto,ytexto,contador,salto
global nivel1,nivel2,nivel3,nivel4,xstep1,xstep2,xstep3,xstep4
global vx1,vy1,vx2,vy2,vx3,vy3,vx4,vy4

#Condições de Início
condicao = 'ANDAMENTO'
pause = False
vivo = True
chegada = False
vidas = 3
contador = 0
texto = 'Vidas: {0:d}  Pontos: {1:d}'.format(vidas, contador)
xtexto = 15
ytexto = 234

#Tamanho altura e largura
windowWidth = 100.0
windowHeight = 100.0

#Tamanho do incremento nas direções x e y
#(número de pixels para se mover a cada intervalo de tempo)
xstep1 = 1.0
xstep2 = 1.0
xstep3 = 1.0
xstep4 = 1.0

#condições do sapo
vivo = True
chegada = False


#Tamanho e posição inicial do sapo
sprop = 1 #sproporcao
salto = 0.5 
sx=175
sy=10
tsx=12*(sprop)
tsy=10*(sprop)

#Tamanho e posição inicial do veículo
#veículo genérico
vprop = 2
tvx=24*vprop
tvy=10*vprop

#veículo1
vx1=170
vy1=55
nivel1 = 1 #nível veículo 1
#veículo2
vx2=60
vy2=85
nivel2 = 2 #nível veículo 2
#veículo3
vx3=120
vy3=125
nivel3 = 3 #nível veículo 3
#veículo3
vx4=40
vy4=155
nivel4 = 4 #nível veículo 4

#cenário
cx=0
cy=0

def sapo():
    #corpo sapo   
    glColor3f(0.2, 0.9, 0.2) # R G B
    glBegin(GL_POLYGON)
    glVertex2d(sx + 2*sprop, sy + 6*sprop)
    glVertex2d(sx + 6*sprop, sy + 10*sprop)
    glVertex2d(sx + 10*sprop, sy + 6*sprop)
    glColor3f(0.2, 0.8, 0.2) # R G B
    glVertex2d(sx + 8*sprop, sy + 2*sprop)
    glVertex2d(sx + 4*sprop, sy + 2*sprop)
    glEnd()
    
    #perna sapo esquerda
    glColor3f(0.2, 0.8, 0.2) # R G B
    glBegin(GL_QUADS)
    glVertex2d(sx, sy+(6*sprop))
    glVertex2d(sx + sprop, sy+(8*sprop))
    glVertex2d(sx + 4*(sprop), sy+(2*sprop))
    glVertex2d(sx + 3*(sprop), sy)
    glEnd()

    #perna sapo direita
    glColor3f(0.2, 0.8, 0.2) # R G B
    glBegin(GL_QUADS)
    glVertex2d(sx + 11*sprop, sy + 8*sprop)
    glVertex2d(sx + 12*sprop, sy + 6*sprop)
    glVertex2d(sx + 9*sprop, sy)
    glVertex2d(sx + 8*sprop, sy + 2*sprop)
    glEnd()

def sapo_morto():

    #sangue
    glColor3f(0.75, 0.0, 0.0) # R G B
    glBegin(GL_POLYGON)
    glVertex2d(sx + 2*sprop - 3, sy + 7.4*sprop)
    glVertex2d(sx + 3*sprop + 3, sy + 7*sprop + 3)
    glVertex2d(sx + 3.3*sprop + 3, sy + 7.3*sprop + 3)
    glVertex2d(sx + 10*sprop + 2, sy + 6*sprop)
    glColor3f(0.5, 0.0, 0.0) # R G B
    glVertex2d(sx + 8*sprop + 3, sy + 2*sprop - 3)
    glVertex2d(sx + 4*sprop - 3, sy + 2*sprop - 3)
    glEnd()

    #corpo sapo   
    glColor3f(0.5, 0.7, 0.4) # R G B
    glBegin(GL_POLYGON)
    glVertex2d(sx + 2*sprop, sy + 6*sprop)
    glVertex2d(sx + 4*sprop, sy + 9*sprop)
    glVertex2d(sx + 6*sprop, sy + 7*sprop)
    glVertex2d(sx + 10*sprop, sy + 6*sprop)
    glVertex2d(sx + 8*sprop, sy + 2*sprop)
    glVertex2d(sx + 4*sprop, sy + 2*sprop)
    glEnd()
    
    #perna sapo esquerda
    glColor3f(0.5, 0.6, 0.4) # R G B
    glBegin(GL_QUADS)
    glVertex2d(sx, sy+(6*sprop))
    glVertex2d(sx + sprop, sy+(8*sprop))
    glVertex2d(sx + 4*(sprop), sy+(2*sprop))
    glVertex2d(sx + 3*(sprop), sy)
    glEnd()

    #perna sapo direita
    glColor3f(0.5, 0.6, 0.4) # R G B
    glBegin(GL_QUADS)
    glVertex2d(sx + 11*sprop, sy + 8*sprop)
    glVertex2d(sx + 12*sprop, sy + 6*sprop)
    glVertex2d(sx + 9*sprop, sy)
    glVertex2d(sx + 8*sprop, sy + 2*sprop)
    glEnd()

def sapo_chegada():
    #corpo sapo   
    glColor3f(0.2, 0.2, 0.6) # R G B
    glBegin(GL_POLYGON)
    glVertex2d(sx + 2*sprop, sy + 6*sprop)
    glVertex2d(sx + 6*sprop, sy + 10*sprop)
    glVertex2d(sx + 10*sprop, sy + 6*sprop)
    glColor3f(0.2, 0.2, 0.45) # R G B
    glVertex2d(sx + 8*sprop, sy + 2*sprop)
    glVertex2d(sx + 4*sprop, sy + 2*sprop)
    glEnd()
    
    #perna sapo esquerda
    glColor3f(0.1, 0.1, 0.36) # R G B
    glBegin(GL_QUADS)
    glVertex2d(sx, sy+(6*sprop))
    glVertex2d(sx + sprop, sy+(8*sprop))
    glVertex2d(sx + 4*(sprop), sy+(2*sprop))
    glVertex2d(sx + 3*(sprop), sy)
    glEnd()

    #perna sapo direita
    glColor3f(0.1, 0.1, 0.36) # R G B
    glBegin(GL_QUADS)
    glVertex2d(sx + 11*sprop, sy + 8*sprop)
    glVertex2d(sx + 12*sprop, sy + 6*sprop)
    glVertex2d(sx + 9*sprop, sy)
    glVertex2d(sx + 8*sprop, sy + 2*sprop)
    glEnd()

    
def cenario():

    #base
    glColor3f(0.15, 0.7, 0.15) # R G B
    glBegin(GL_QUADS)
    glVertex2d(0,0)
    glVertex2d(0,192)
    glColor3f(0.15, 0.5, 0.15) # R G B
    glVertex2d(wo,192)
    glVertex2d(wo,0)
    glEnd()

    #pista1
    glColor3f(0.68, 0.68, 0.68) # R G B
    glBegin(GL_QUADS)
    glVertex2d(0,50)
    glVertex2d(0,110)
    glColor3f(0.4, 0.4, 0.4) # R G B
    glVertex2d(wo,110)
    glVertex2d(wo,50)
    glEnd()

    #faixa1
    glColor3f(0.8, 0.8, 0.8)
    glBegin(GL_LINE_STRIP)
    glVertex2d(0,80)    
    glVertex2d(wo,80)
    glEnd()

    #pista2
    glColor3f(0.68, 0.68, 0.68) # R G B
    glBegin(GL_QUADS)
    glVertex2d(0,120)
    glVertex2d(0,180)
    glColor3f(0.4, 0.4, 0.4) # R G B
    glVertex2d(wo,180)
    glVertex2d(wo,120)
    glEnd()

    #faixa2
    glColor3f(0.8, 0.8, 0.8)
    glBegin(GL_LINE_STRIP)
    glVertex2d(0,150)    
    glVertex2d(wo,150)
    glEnd()

    #lagoa
    glColor3f(0.4, 0.4, 1.0) # R G B
    glBegin(GL_QUADS)
    glVertex2d(0,192)
    glVertex2d(wo,192)
    glColor3f(0.3, 0.3, 0.4) # R G B
    glVertex2d(wo,224) 
    glVertex2d(0,224)
    glEnd()

def veiculo1():

    #carro
    glColor3f(0.0, 0.0, 1.0) # R G B
    glBegin(GL_QUADS)
    glVertex2d(vx1,vy1)
    glVertex2d(vx1,vy1 + 10*vprop)
    glColor3f(0.0, 0.0, 0.8) # R G B
    glVertex2d(vx1 + 24*vprop,vy1 + 10*vprop) 
    glVertex2d(vx1 + 24*vprop,vy1)
    glEnd()

    #teto e parabrisa
    glColor3f(0.7, 0.7, 0.8) # R G B
    glBegin(GL_QUADS)
    glVertex2d(vx1 + 8*vprop,vy1)
    glVertex2d(vx1 + 8*vprop, vy1 + 10*vprop)
    glColor3f(0.8, 0.8, 0.9) # R G B
    glVertex2d(vx1 + 10*vprop,vy1 + 10*vprop) 
    glVertex2d(vx1 + 10*vprop,vy1)
    glEnd()
    #parabrisa traseiro
    glColor3f(0.8, 0.8, 0.9) # R G B
    glBegin(GL_QUADS)
    glVertex2d(vx1 + 17*vprop,vy1)
    glVertex2d(vx1 + 17*vprop, vy1 + 10*vprop)
    glColor3f(0.7, 0.7, 0.8) # R G B
    glVertex2d(vx1 + 19*vprop,vy1 + 10*vprop) 
    glVertex2d(vx1 + 19*vprop,vy1)
    glEnd()

def veiculo2():

    #carro
    glColor3f(1.0, 0.0, 0.0) # R G B
    glBegin(GL_QUADS)
    glVertex2d(vx2,vy2)
    glVertex2d(vx2,vy2 + 10*vprop)
    glColor3f(0.8, 0.0, 0.0) # R G B
    glVertex2d(vx2 + 24*vprop,vy2 + 10*vprop) 
    glVertex2d(vx2 + 24*vprop,vy2)
    glEnd()

    #teto e parabrisa
    glColor3f(0.7, 0.7, 0.8) # R G B
    glBegin(GL_QUADS)
    glVertex2d(vx2 + 8*vprop,vy2)
    glVertex2d(vx2 + 8*vprop, vy2 + 10*vprop)
    glColor3f(0.8, 0.8, 0.9) # R G B
    glVertex2d(vx2 + 10*vprop,vy2 + 10*vprop) 
    glVertex2d(vx2 + 10*vprop,vy2)
    glEnd()
    #parabrisa traseiro
    glColor3f(0.8, 0.8, 0.9) # R G B
    glBegin(GL_QUADS)
    glVertex2d(vx2 + 17*vprop,vy2)
    glVertex2d(vx2 + 17*vprop, vy2 + 10*vprop)
    glColor3f(0.7, 0.7, 0.8) # R G B
    glVertex2d(vx2 + 19*vprop,vy2 + 10*vprop) 
    glVertex2d(vx2 + 19*vprop,vy2)
    glEnd()

def veiculo3():

    #carro
    glColor3f(0.9, 0.9, 0.9) # R G B
    glBegin(GL_QUADS)
    glVertex2d(vx3,vy3)
    glVertex2d(vx3,vy3 + 10*vprop)
    glColor3f(0.8, 0.8, 0.76) # R G B
    glVertex2d(vx3 + 24*vprop,vy3 + 10*vprop) 
    glVertex2d(vx3 + 24*vprop,vy3)
    glEnd()

    #teto e parabrisa
    glColor3f(0.7, 0.7, 0.8) # R G B
    glBegin(GL_QUADS)
    glVertex2d(vx3 + 8*vprop,vy3)
    glVertex2d(vx3 + 8*vprop, vy3 + 10*vprop)
    glColor3f(0.8, 0.8, 0.9) # R G B
    glVertex2d(vx3 + 10*vprop,vy3 + 10*vprop) 
    glVertex2d(vx3 + 10*vprop,vy3)
    glEnd()
    #parabrisa traseiro
    glColor3f(0.8, 0.8, 0.9) # R G B
    glBegin(GL_QUADS)
    glVertex2d(vx3 + 17*vprop,vy3)
    glVertex2d(vx3 + 17*vprop, vy3 + 10*vprop)
    glColor3f(0.7, 0.7, 0.8) # R G B
    glVertex2d(vx3 + 19*vprop,vy3 + 10*vprop) 
    glVertex2d(vx3 + 19*vprop,vy3)
    glEnd()
    
def veiculo4():

    #carro
    glColor3f(1.0, 0.93, 0.0) # R G B
    glBegin(GL_QUADS)
    glVertex2d(vx4,vy4)
    glVertex2d(vx4,vy4 + 10*vprop)
    glColor3f(0.93, 0.86, 0.0) # R G B
    glVertex2d(vx4 + 24*vprop,vy4 + 10*vprop) 
    glVertex2d(vx4 + 24*vprop,vy4)
    glEnd()

    #teto e parabrisa
    glColor3f(0.8, 0.76, 0.8) # R G B
    glBegin(GL_QUADS)
    glVertex2d(vx4 + 8*vprop,vy4)
    glVertex2d(vx4 + 8*vprop, vy4 + 10*vprop)
    glColor3f(0.8, 0.8, 0.9) # R G B
    glVertex2d(vx4 + 10*vprop,vy4 + 10*vprop) 
    glVertex2d(vx4 + 10*vprop,vy4)
    glEnd()
    #parabrisa traseiro
    glColor3f(0.8, 0.8, 0.9) # R G B
    glBegin(GL_QUADS)
    glVertex2d(vx4 + 17*vprop,vy4)
    glVertex2d(vx4 + 17*vprop, vy4 + 10*vprop)
    glColor3f(0.7, 0.7, 0.8) # R G B
    glVertex2d(vx4 + 19*vprop,vy4 + 10*vprop) 
    glVertex2d(vx4 + 19*vprop,vy4)
    glEnd()
    
def Desenha():#Função callback chamada para fazer o desenho
    global condicao,vivo,pause,chegada,contador,texto,xtexto,ytexto,vidas,windowWidth,windowHeight,sx,sy,xstep,ystep,wo,ho
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    # Limpa a janela de visualização com a cor de fundo especificada
    glClear(GL_COLOR_BUFFER_BIT)

    if(condicao == 'ANDAMENTO' and vidas > 0):
        cenario()
        if vivo: sapo()
        else: sapo_morto()
        if chegada: sapo_chegada()
        veiculo1()
        veiculo2()
        veiculo3()
        veiculo4()
        glColor3f(1.0,1.0,1.0)
        DesenhaTexto(texto)
    elif(condicao == 'INICIAR' and vidas > 0):
        pause = False
        cenario()
        xtexto = 15
        ytexto = 234
        texto = 'Vidas: {0:d}  Pontos: {1:d}'.format(vidas, int(contador*100))
        glColor3f(1.0,1.0,1.0)
        DesenhaTexto(texto)
        if vivo: sapo()
        else: sapo_morto()
        if chegada: sapo_chegada()
        veiculo1()
        veiculo2()
        veiculo3()
        veiculo4()
    elif(condicao == 'PAUSAR'):
        pause = True
        xtexto = windowWidth/2 - 15
        ytexto = windowHeight/2
        texto = 'Pause'
        glColor3f(1.0,1.0,1.0)        
        DesenhaTexto(texto)              
    elif(condicao == 'ENCERRAR'):
        pause = False
        vivo = True        
        chegada = False
        contador = 0
        vidas = 3
        sx=windowWidth/2
        sy=10
        xtexto = windowWidth/2 - 15
        ytexto = windowHeight/2
        texto = 'Encerrado'
        glColor3f(1.0,1.0,1.0)
        DesenhaTexto(texto)        
    else:
        vivo = False
        pause = False
        sx=sx
        sy=sy
        cenario()
        xtexto = windowWidth/4
        ytexto = windowHeight/2
        texto = 'Pontos: {0:d} - Fim de Jogo - Aperte "A" e jogue novamente'.format(int(contador*100))
        glColor3f(1.0,1.0,1.0)
        DesenhaTexto(texto)
        if vivo: sapo()
        else: sapo_morto()
        if chegada: sapo_chegada()
        veiculo1()
        veiculo2()
        veiculo3()
        veiculo4()
        glColor3f(1.0,1.0,1.0)
        DesenhaTexto(texto)   
    glutSwapBuffers()#Executa os comandos OpenGL
    
def DesenhaTexto(string):
    global texto,xtexto,ytexto,wo
    glPushMatrix()
    # Posição no universo onde o texto será colocado
    glRasterPos2f(xtexto,ytexto)
    # Exibe caracter a caracter
    for char in string:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18,ord(char))
    glPopMatrix()


# Inicializa parâmetros de rendering
def Inicializa():
    glClearColor(0.0, 0.0, 0.0, 1.0)# Define a cor de fundo da janela de visualização como preta

#Função callback chamada quando o tamanho da janela é alterado
def AlteraTamanhoJanela(w, h):
    global windowWidth,windowHeight,ho,wo
    # Evita a divisao por zero
    if(h == 0): h = 1
    if(w == 0): w = 1
    # Especifica as dimensões da Viewport
    glViewport(0, 0, w, h)
    wo=w
    ho=h
    # Inicializa o sistema de coordenadas
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # Estabelece a janela de seleção (left, right, bottom, top)
    if (w <= h):
        windowHeight = 250.0*h/w
        windowWidth = 250.0
    else:
        windowWidth = 250.0*w/h
        windowHeight = 250.0
    gluOrtho2D(0.0, windowWidth, 0.0, windowHeight)

# Função callback chamada para gerenciar eventos do teclado para teclas especiais, tais como F1, PgDn e Home
def TeclasEspeciais(key, x, y):
    global menu_vitoria,vivo,chegada,pause,contador,texto,salto
    global sx,sy,tsx,tsy,windowHeight,windowWidth,tvx,tvy,vx1,vy1

    if not vivo and vidas > 0:
        for i in range(1000000):
            i = i + 1
        vivo = True
        sx=windowWidth/2
        sy=10
           
    if(key == GLUT_KEY_UP and vivo and not pause and vidas > 0):
        sy=sy+ salto*tsy
        if (sy+tsy>windowHeight):
            sy=windowHeight-tsy          
    if(key == GLUT_KEY_DOWN and vivo and not pause and vidas > 0):
        sy=sy-salto*tsy
        if (sy<tsy):
            sy=0
    if(key == GLUT_KEY_LEFT and vivo and not pause and vidas > 0):
        sx=sx-salto*tsx
        if (sx<0):
            sx=0
    if(key == GLUT_KEY_RIGHT and vivo and not pause and vidas > 0):
        sx=sx+salto*tsx
        if (sx+tsx>windowWidth):
            sx=windowWidth-tsx

    if(sy+tsy > 198 and vivo and not pause and vidas > 0):
        chegada = True
        if(sy+2 < 196 and vivo and not pause and vidas > 0):
            chegada = False
        
    if(sy+tsy > 212 and vivo and not pause and vidas > 0):       
        chegada = False
        contador = contador + 1
        texto = 'Vidas: {0:d}  Pontos: {1:d}'.format(vidas, int(contador*100))
        sx=windowWidth/2
        sy=10
    glutPostRedisplay()

    #Função callback chamada pela GLUT a cada intervalo de tempo (a window não está sendo redimensionada ou movida)
def Timer(value) :
    global vivo,chegada,pause,contador,texto,vidas,contador
    global windowWidth,windowHeight,sx,sy,tsx,tsy
    global nivel1,nivel2,nivel3,nivel4,tvx,tvy,vx1,vy1,vx2,vy2,vx3,vy3,vx4,vy4,xstep1,xstep2,xstep3,xstep4

    #mudança de níveis veículo
    #níveis veículo 1
    if(vx1+tvx < 0 and nivel1 == 1 ):
        vx1 = windowWidth
        vy1 = 85
        nivel1 = 2
    if(vx1+tvx < 0 and nivel1 == 2):
        vx1 = windowWidth
        vy1 = 125
        nivel1 = 3
    if(vx1+tvx < 0 and nivel1 == 3):
        vx1 = windowWidth
        vy1 = 155
        nivel1 = 4
    if(vx1+tvx < 0 and nivel1 == 4):
        vx1 = windowWidth
        vy1 = 55
        nivel1 = 1
    #níveis veículo 2
    if(vx2+tvx < 0 and nivel2 == 1):
        vx2 = windowWidth
        vy2 = 85
        nivel2 = 2
    if(vx2+tvx < 0 and nivel2 == 2):
        vx2 = windowWidth
        vy2 = 125
        nivel2 = 3
    if(vx2+tvx < 0 and nivel2 == 3):
        vx2 = windowWidth
        vy2 = 155
        nivel2 = 4
    if(vx2+tvx < 0 and nivel2 == 4):
        vx2 = windowWidth
        vy2 = 55
        nivel2 = 1
    #níveis veículo 3
    if(vx3+tvx < 0 and nivel3 == 1):
        vx3 = windowWidth
        vy3 = 85
        nivel3 = 2
    if(vx3+tvx < 0 and nivel3 == 2):
        vx3 = windowWidth
        vy3 = 125
        nivel3 = 3
    if(vx3+tvx < 0 and nivel3 == 3):
        vx3 = windowWidth
        vy3 = 155
        nivel3 = 4
    if(vx3+tvx < 0 and nivel3 == 4):
        vx3 = windowWidth
        vy3 = 55
        nivel3 = 1
    #níveis veículo 4
    if(vx4+tvx < 0 and nivel4 == 1 ):
        vx4 = windowWidth
        vy4 = 85
        nivel4 = 2
    if(vx4+tvx < 0 and nivel4 == 2):
        vx4 = windowWidth
        vy4 = 125
        nivel4 = 3
    if(vx4+tvx < 0 and nivel4 == 3):
        vx4 = windowWidth
        vy4 = 155
        nivel4 = 4
    if(vx4+tvx < 0 and nivel4 == 4):
        vx4 = windowWidth
        vy4 = 55
        nivel4 = 1
        
    #velocidade dos veículos
    if (not pause and (nivel1 == 1 or nivel2 == 1 or nivel3 == 1 or nivel4 == 1)):
        if nivel1 == 1:
            vx1 -= (6 + 0.1*contador)*xstep1 
        if nivel2 == 1:
            vx2 -= (6 + 0.1*contador)*xstep1
        if nivel3 == 1:
            vx3 -= (6 + 0.1*contador)*xstep1
        if nivel4 == 1:
            vx4 -= (6 + 0.1*contador)*xstep1
    if (not pause and (nivel1 == 2 or nivel2 == 2 or nivel3 == 2 or nivel4 == 2)):
        if nivel1 == 2:
            vx1 -= (8 + 0.1*contador)*xstep1            
        if nivel2 == 2:
            vx2 -= (8 + 0.1*contador)*xstep1
        if nivel3 == 2:
            vx3 -= (8 + 0.1*contador)*xstep1
        if nivel4 == 2:
            vx4 -= (8 + 0.1*contador)*xstep1
    if (not pause and (nivel1 == 3 or nivel2 == 3 or nivel3 == 3 or nivel4 == 3)):
        if nivel1 == 3:
            vx1 -= (6 + 0.1*contador)*xstep1
        if nivel2 == 3:
            vx2 -= (6 + 0.1*contador)*xstep1
        if nivel3 == 3:
            vx3 -= (6 + 0.1*contador)*xstep1
        if nivel4 == 3:
            vx4 -= (6 + 0.1*contador)*xstep1
    if (not pause and (nivel1 == 4 or nivel2 == 4 or nivel3 == 4 or nivel4 == 4)):
        if nivel1 == 4:
            vx1 -= (8 + 0.1*contador)*xstep1
        if nivel2 == 4:
            vx2 -= (8 + 0.1*contador)*xstep1
        if nivel3 == 4:
            vx3 -= (8 + 0.1*contador)*xstep1
        if nivel4 == 4:
            vx4 -= (8 + 0.1*contador)*xstep1
    
    #atropelamento / colisão veículo1
    if((sy+tsy > vy1 and sy < vy1+tvy and sx+tsx > vx1 and sx < vx1+tvx) and vivo and not chegada):
        sy = sy
        sx = sx
        vidas = vidas - 1
        texto = 'Vidas: {0:d}  Pontos: {1:d}'.format(int(vidas), int(contador*100))
        vivo = False
    #atropelamento / colisão veículo2
    if((sy+tsy > vy2 and sy < vy2+tvy and sx+tsx > vx2 and sx < vx2+tvx) and vivo and not chegada):
        sy = sy
        sx = sx
        vidas = vidas - 1
        texto = 'Vidas: {0:d}  Pontos: {1:d}'.format(int(vidas), int(contador*100))
        vivo = False
    #atropelamento / colisão veículo3
    if((sy+tsy > vy3 and sy < vy3+tvy and sx+tsx > vx3 and sx < vx3+tvx) and vivo and not chegada):
        sy = sy
        sx = sx
        vidas = vidas - 1
        texto = 'Vidas: {0:d}  Pontos: {1:d}'.format(int(vidas), int(contador*100))
        vivo = False
    #atropelamento / colisão veículo4
    if((sy+tsy > vy4 and sy < vy4+tvy and sx+tsx > vx4 and sx < vx4+tvx) and vivo and not chegada):
        sy = sy
        sx = sx
        vidas = vidas - 1
        texto = 'Vidas: {0:d}  Pontos: {1:d}'.format(int(vidas), int(contador*100))
        vivo = False
            
    #/ Redesenha o objeto com as novas coordenadas
    glutPostRedisplay()
    glutTimerFunc(33,Timer, 1)

# Função callback chamada para gerenciar eventosde teclado
def GerenciaTeclado(key, x, y):
    global sx, sy, vivo
    global windowWidth,windowHeight,vx1,vx1,ho,wo,nivel1,condicao,vidas,contador,chegada
    global pause,texto,xtexto,ytexto
    if(key=='A' or key ==b'a'):
        condicao = 'ANDAMENTO'
        pause = False
        vivo = True        
        chegada = False
        contador = 0
        vidas = 3
        sx=windowWidth/2
        sy=10
        xtexto = 15
        ytexto = 234
        texto = 'Vidas: {0:d}  Pontos: {1:d}'.format(vidas, int(contador*100))
        glColor3f(1.0,1.0,1.0)
        DesenhaTexto(texto)
    
    glutPostRedisplay()

def GerenciaMouse(button, state, x, y):
    if (button == GLUT_RIGHT_BUTTON):
        if (state == GLUT_DOWN): CriaMenu()
        glutPostRedisplay()

def MenuPrincipal(op):
   
    global condicao
    if(op==0): condicao = 'INICIAR'
    elif(op==1): condicao = 'PAUSAR'
    elif(op==2): condicao = 'ENCERRAR'
    glutPostRedisplay();
    return 0;

def CriaMenu():
    # Criação do Menu
    menu = glutCreateMenu(MenuPrincipal);
    glutAddMenuEntry("INICIAR", 0);
    glutAddMenuEntry("PAUSAR", 1);
    glutAddMenuEntry("ENCERRAR", 2);
    glutAttachMenu(GLUT_RIGHT_BUTTON);
    return 0

#Programa Principal
def main():
    glutInit(sys.argv)
    #glutInitWindowPosition(100,100)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(400, 350)
    glutInitWindowPosition(10,10)    
    glutCreateWindow(b'Jogo Sapo 2D')
    glutReshapeFunc(AlteraTamanhoJanela)
    glutDisplayFunc(Desenha);
    glutTimerFunc(33, Timer, 1)
    glutKeyboardFunc(GerenciaTeclado)
    glutSpecialFunc(TeclasEspeciais)
    glutMouseFunc(GerenciaMouse)

    Inicializa()
    glutMainLoop()

#"Starta" o programa
main()









