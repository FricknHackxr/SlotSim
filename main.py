import random
from time import sleep

import pygame

geld = 50
wins = 0
einsatz = [1, 2, 3]
aktueller_einsatz = 0

choice1 = 0
choice2 = 0
choice3 = 0

white = (255, 255, 255)
yellow = (255, 255, 0)
orange = (255, 100, 0)

pygame.init()
screen = pygame.display.set_mode((600, 960))
background = pygame.image.load("textures/slot.png")
font = pygame.font.SysFont('timesnewroman', 250)
letters = [font.render("A", False, orange, yellow), font.render("B", False, orange, white),
           font.render("C", False, orange, white), font.render("D", False, orange, white),
           font.render("E", False, orange, white), font.render("F", False, orange, white),
           font.render("G", False, orange, white)]
font = pygame.font.SysFont('timesnewroman', 30)
letters_bets = font.render(str(einsatz[aktueller_einsatz]) + " €", False, orange, yellow)
letters_geld = font.render(str(geld) + " €", False, orange, yellow)
letters_wins = font.render(str(wins), False, orange, yellow)
pygame.display.set_caption("SlotSim")


class Symbol:
    def __init__(self, name, percentage, win, pic):
        self.name = name
        self.percentage = percentage
        self.win = win
        self.pic = pic

    def __str__(self):
        return self.name


symbols = [Symbol("A", 0.01, 200, ""), Symbol("B", 0.02, 100, ""),
           Symbol("C", 0.07, 50, ""), Symbol("D", 0.1, 20, ""),
           Symbol("E", 0.15, 10, ""), Symbol("F", 0.25, 5, ""),
           Symbol("G", 0.4, 1, "")]

weights = []
for symbol in symbols:
    weights.append(symbol.percentage)


def symbolChoice():
    choice = random.randint(0, 100)
    if (0 <= choice <= 40):
        return 6
    elif (41 <= choice <= 65):
        return 5
    elif (66 <= choice <= 80):
        return 4
    elif (81 <= choice <= 90):
        return 3
    elif (91 <= choice <= 97):
        return 2
    elif (98 <= choice <= 99):
        return 1
    else:
        return 0


# Eventloop, in der Tastatureingaben des Spielers abgefragt werden
'''
  Enter
'''
spiel_aktiv = True

while spiel_aktiv:

    font = pygame.font.SysFont('timesnewroman', 250)
    letters = [font.render("A", False, orange, yellow), font.render("B", False, orange, white),
               font.render("C", False, orange, white), font.render("D", False, orange, white),
               font.render("E", False, orange, white), font.render("F", False, orange, white),
               font.render("G", False, orange, white)]
    font = pygame.font.SysFont('timesnewroman', 30)
    letters_bets = font.render(str(einsatz[aktueller_einsatz]) + " €", False, orange, yellow)
    letters_geld = font.render(str(geld) + " €", False, orange, yellow)
    letters_wins = font.render(str(wins), False, orange, yellow)

    # draw frame
    screen.blit(background, (0, 0))
    screen.blit(letters[choice1], (30, 440))
    screen.blit(letters[choice2], (270, 440))
    screen.blit(letters[choice3], (450, 440))

    screen.blit(letters_bets, (150, 930))
    screen.blit(letters_geld, (380, 930))
    screen.blit(letters_wins, (650, 930))
    pygame.display.update()

    # Überprüfen, ob Nutzer eine Aktion durchgeführt hat
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            spielaktiv = False
        elif event.type == pygame.KEYDOWN:
            # Abfrage, welche Taste gedrückt wurde
            if event.key == pygame.K_UP:
                if aktueller_einsatz < 2:
                    aktueller_einsatz += 1
                    print("Einsatz erhöht")
            elif event.key == pygame.K_DOWN:
                if aktueller_einsatz > 0:
                    aktueller_einsatz -= 1
                    print("Einsatz gesenkt")
            elif event.key == pygame.K_e:
                print("Neue Runde")
                geld -= einsatz[aktueller_einsatz]
                choice1 = symbolChoice()
                print(symbols[choice1])
                choice2 = symbolChoice()
                print(symbols[choice2])
                choice3 = symbolChoice()
                print(symbols[choice3])
                if choice1 == choice2 == choice3:
                    print("You won " + str(symbols[choice1].win * einsatz[aktueller_einsatz]))
                    wins += 1
                    geld += symbols[choice1].win * einsatz[aktueller_einsatz]
            elif event.key == pygame.K_r:
                geld = 50
                aktueller_einsatz = 0
                wins = 0
                print("Neuanfang")
