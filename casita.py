import sys
from pygame import *

init()
## Carregamento de recursos 
cachorro_imagem = image.load('cachorro.png')
cachorro_imagem = transform.scale(cachorro_imagem, (150,150))

cachorro_font = font.Font('Somelist.ttf', 50)

mixer.music.load('Fluffing-a-Duck(chosic.com).mp3')
mixer.music.play(-1)

window = display.set_mode((1280,720))
running = True
clock = time.Clock()


##Definição de variáveis
pos_x = 300
pos_y = 75
background_color = (152, 209, 250)
indo_direita = 0


while running:
    clock.tick(60)

    for ev in event.get():
        if ev.type == QUIT:
            running = False

        #AÇOES INSTANTANEAS
        if ev.type == KEYDOWN:
            key_pressed = ev.key
            if key_pressed == K_SPACE:
                background_color = (245,178,64)


    ##UPDATE
    dt = clock.get_time()/1000
    keys = key.get_pressed()

    # Nuvem não pode sair da tela
    if indo_direita == 0:
        pos_x = pos_x + 100 * dt
    else:
        pos_x = pos_x - 100 * dt
    
    if pos_x+120+40 > 1280:
       indo_direita = indo_direita+1
    if pos_x-40 < 0:
        indo_direita = 0
    

    #Pressionar teclas
    #ACOES CONTINUAS
    #if keys[K_d]:
    #    pos_x = pos_x + 100 * dt
    #if keys[K_a]:
    #    pos_x = pos_x - 100 * dt
    #if keys[K_w]:
    #    pos_y = pos_y - 100 * dt
    #if keys[K_s]:
    #    pos_y = pos_y + 100 * dt
    
    #Desenhar a partir daqui

    #Desenhar primitivas geometricas
    window.fill(background_color)

    #Casa
    draw.rect(window, (50, 168, 70), (0, 550, 1280, 300))
    draw.rect(window, (227, 195, 132), (200,350,300,200))
    draw.polygon(window, (196, 103, 49), ((200,350), (350,150), (500,350)))
    draw.rect(window, (148, 219, 227),(225,400,55,80) )
    draw.rect(window, (128, 85, 1), (350,400,90,150))
    draw.circle(window, (0,0,0), (360,470), 5)

    #Arvore
    draw.rect(window, (128, 85, 1), (900,400,30,150))
    draw.circle(window, (20, 107, 2), (915,350), 100)

    #Nuvem
    draw.circle(window, (255,255,255), (pos_x,75), 40)
    draw.circle(window, (255,255,255), (pos_x + 40,75), 40)
    draw.circle(window, (255,255,255), (pos_x + 80,75), 40)
    draw.circle(window, (255,255,255), (pos_x + 120,75), 40)

    #Nuvem não pode sair da tela

    #if pos_x>=1280 or pos_x<=0:
    #    pos_x=0
    
    #Sol
    draw.circle(window, (255,255,0), (70,70), 50)
    draw.line(window, (255,255,0),(70, 70),(150,70), 5)
    draw.line(window, (255,255,0),(70, 70),(70,150), 5)
    draw.line(window, (255,255,0),(70, 70),(140,140), 5)
    draw.line(window, (255,255,0),(70, 70),(140,30), 5)   
    
    
    #Desenhar imagens 
    window.blit(cachorro_imagem, (500,420))

    # Desenhar texto
    cachorro_text = cachorro_font.render('mais um dia calmo', True, (0, 0, 0))
    window.blit(cachorro_text, (400,100))

    display.update()