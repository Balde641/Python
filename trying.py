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

def kontrolli(hahmot, tapahtuma, viholliset): #added here and below till .KEYDOWN
    for vihollinen in viholliset:
        if viholliset == hahmot:
            break
            # elif tapahtuma.type == pygame.QUIT:
            #     break
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
    kissahahmo = ["marioo.png", 50, 50, False]
    ase = ["gun.png", 500, 50, False]
    hahmot = [kissahahmo, ase]

    while True:
        tapahtuma = pygame.event.poll()
        if tapahtuma.type == pygame.QUIT:
            break
        kontrolli(hahmot, tapahtuma, viholliset)
        piirtaminen(naytto, hahmot)



main()