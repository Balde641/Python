import pygame

naytto = pygame.display.set_mode((640, 400))
pygame.display.set_caption("Piirtäminen")


def piirraKuva(kuvatiedosto, x, y):
    naytto.blit(kuvatiedosto, (x, y))

def piirtaminen(naytto, hahmot):
    naytto.fill((0, 0, 0))
    for hahmo in hahmot:
        if hahmo[3] == True:
            kuva = pygame.image.load(hahmo[0]).convert()
            naytto.blit(kuva, (hahmo[1], hahmo[2]))
    pygame.display.flip()

def kontrolli(hahmot, tapahtuma, vihollinen): #Added line
    for vihollinen in viholliset:  #Added line
        if vihollinen = False #Added line
        
    if tapahtuma.type == pygame.KEYDOWN:
        if tapahtuma.key == pygame.K_SPACE:

            for hahmo in hahmot:
                hahmo[3] = True
        elif tapahtuma.key == pygame.K_RIGHT:
            päähahmo = hahmot[1]
            if päähahmo[1] < 570:
                päähahmo[1] += 10

            
        elif tapahtuma.key == pygame.K_LEFT:
            päähahmo = hahmot[1]
            if päähahmo[1] > 5:
                päähahmo[1] -= 10

        elif tapahtuma.key == pygame.K_UP:
            päähahmo = hahmot[1]
            if päähahmo[2] >= 5:
                päähahmo[2] -= 10 

        elif tapahtuma.key == pygame.K_DOWN:
            päähahmo = hahmot[1]
            if päähahmo[2] <= 320:
                päähahmo[2] += 10        

            hahmot[0][3] = True
            hahmot[1][3] = True


def main():
    kissahahmo = ["bear.jpg", 50, 50, False]
    kissahahmo1 = ["player.jpg", 500, 50, False]
    hahmot = [kissahahmo, kissahahmo1]

    while True:
        tapahtuma = pygame.event.poll()
        if tapahtuma.type == pygame.QUIT:
            break
        kontrolli(hahmot, tapahtuma, vihollinen) #Added line
        piirtaminen(naytto, hahmot)



main()