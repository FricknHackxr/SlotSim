import random
import pygame

geld = 50
einsatz = [1, 2, 3, 4, 5]
aktueller_einsatz = 0

choice1 = 0
choice2 = 0
choice3 = 0

white = (255, 255, 255)
yellow = (255, 255, 0)
orange = (255, 100, 0)

pygame.init()
screen = pygame.display.set_mode((800, 1200))
background = pygame.image.load("textures/slot.png")
font = pygame.font.SysFont('timesnewroman', 250)
letters = [font.render("7", False, orange, yellow), font.render("A", False, orange, white),
           font.render("B", False, orange, white), font.render("C", False, orange, white),
           font.render("D", False, orange, white)]
pygame.display.set_caption("SlotSim")


class Symbol:
    def __init__(self, name, percentage, pic):
        self.name = name
        self.percentage = percentage
        self.pic = pic

    def __str__(self):
        return self.name


symbols = [Symbol("Johnny Sins als Mechaniker", 0.02, ""), Symbol("Johnny Sins als Babysitter", 0.08, ""),
           Symbol("Johnny Sins als Koch", 0.2, ""), Symbol("Johnny Sins als Feuerwehrmann", 0.3, ""),
           Symbol("Johnny Sins als Arzt", 0.4, "")]


# Eventloop, in der Tastatureingaben des Spielers abgefragt werden
'''
   Enter
'''
spiel_aktiv = True

while spiel_aktiv:

    # draw frame
    screen.blit(background, (0, 0))
    screen.blit(letters[choice1], (120, 590))
    screen.blit(letters[choice2], (360, 590))
    screen.blit(letters[choice3], (580, 590))
    pygame.display.update()

    # Überprüfen, ob Nutzer eine Aktion durchgeführt hat
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            spielaktiv = False
        elif event.type == pygame.KEYDOWN:
            # Abfrage, welche Taste gedrückt wurde
            if event.key == pygame.K_UP:
                print("Einsatz erhöht")
                aktueller_einsatz += 1
            elif event.key == pygame.K_DOWN:
                print("Einsatz gesenkt")
                aktueller_einsatz -= 1
            elif event.key == pygame.K_e:
                print("Neue Runde")
                choice1 = random.randint(0, 4)
                print(symbols[choice1])
                choice2 = random.randint(0, 4)
                print(symbols[choice2])
                choice3 = random.randint(0, 4)
                print(symbols[choice3])
            elif event.key == pygame.K_r:
                print("Neuanfang")
