import pygame

naytto = pygame.display.set_mode((740, 500))
pygame.display.set_caption("Piirtäminen")

x = 100
y = 300

def main():
    while True:
        tapahtuma = pygame.event.poll()
        if tapahtuma.type == pygame.QUIT:
            break

        naytto.fill((0, 0, 0))
        pygame.draw.line(naytto, (0, 0, 255), (0, 0), (640, 400))
        #pygame.display.flip()

        #naytto.fill((0, 0, 0))
        pygame.draw.line(naytto, (0, 255, 0), (640, 0), (0, 400))
        #pygame.display.flip()

        #naytto.fill((0, 0, 0))
        pygame.draw.rect(naytto, (255, 0, 0), (100, 50, 150, 200))
        #pygame.display.flip()

        #naytto.fill((0, 0, 0))
        pygame.draw.circle(naytto, (255, 255, 0), (350, 150), 40)

        #naytto.fill((0, 0, 0))
        kuva = pygame.image.load("mycat.png").convert()
        naytto.blit(kuva, (x, y))
        pygame.display.flip()
        #pygame.display.flip()
        # oli osa2
 

main()