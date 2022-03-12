import random
import time

import pygame

geld = 50
wins = 0
gewinn = 0
einsatz = [1, 2, 3]
aktueller_einsatz = 0

choice1 = 0
choice2 = 0
choice3 = 0

red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)

pygame.init()
screen = pygame.display.set_mode((600, 960))
background = pygame.image.load("textures/slot.png")
pics = [pygame.image.load("textures/diamant.png"), pygame.image.load("textures/sieben.png"),
        pygame.image.load("textures/bar.png"), pygame.image.load("textures/hufeisen.png"),
        pygame.image.load("textures/geld.png"), pygame.image.load("textures/glocke.png"),
        pygame.image.load("textures/cherry.png")]
font = pygame.font.SysFont('arial', 25)
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


def symbol_choice():
    choice = random.randint(0, 100)
    if 0 <= choice <= 40:
        return 6
    elif 41 <= choice <= 65:
        return 5
    elif 66 <= choice <= 80:
        return 4
    elif 81 <= choice <= 90:
        return 3
    elif 91 <= choice <= 97:
        return 2
    elif 98 <= choice <= 99:
        return 1
    else:
        return 0


# Eventloop, in der Tastatureingaben des Spielers abgefragt werden
'''
  e - neue Runde
  r - Reset auf Anfangswerte
  Pfeil hoch - Einsatz erhöhen
  Pfeil runter - Einsatz senken
'''
spiel_aktiv = True
show_win = False
show_start = 0

input_block = False

while spiel_aktiv:

    font = pygame.font.SysFont('arial', 28)
    letters_bets = font.render(str(einsatz[aktueller_einsatz]) + "€", False, red)
    letters_geld = font.render(str(geld) + "€ (" + str(gewinn) + "€)", False, red)
    letters_wins = font.render(str(wins), False, red)

    # draw frame
    screen.blit(background, (0, 0))
    screen.blit(pics[choice1], (90, 500))
    screen.blit(pics[choice2], (265, 500))
    screen.blit(pics[choice3], (440, 500))

    screen.blit(letters_bets, (90, 695))
    screen.blit(letters_geld, (215, 695))
    screen.blit(letters_wins, (430, 695))

    if show_win and (int(time.time() * 1000) - show_start < 1000) and (gewinn > 0):
        screen.blit(font.render(str(gewinn) + "€ gewonnen!", False, white), (200, 800))
        input_block = True
    elif show_win and (int(time.time() * 1000) - show_start > 1000):
        show_win = False
        show_start = 0
        input_block = False

    pygame.display.update()

    # Überprüfen, ob Nutzer eine Aktion durchgeführt hat
    for event in pygame.event.get():

        if input_block:
            break

        if event.type == pygame.QUIT:
            spiel_aktiv = False

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
                if geld - einsatz[aktueller_einsatz] < 0:
                    geld = 50
                    aktueller_einsatz = 0
                    wins = 0
                    print("Neuanfang")
                    screen.fill(black)
                    letters_reset = font.render("Dir wird schwarz vor Augen!", False, red)
                    screen.blit(letters_reset, (130, 450))
                    pygame.display.update()
                    pygame.time.delay(2000)
                    screen.fill(black)
                    letters_reset = font.render("Du wachst in einem Poke-Center auf!", False, white)
                    screen.blit(letters_reset, (60, 450))
                    pygame.display.update()
                    pygame.time.delay(2000)
                geld -= einsatz[aktueller_einsatz]
                gewinn = -einsatz[aktueller_einsatz]
                choice1 = symbol_choice()
                choice2 = symbol_choice()
                choice3 = symbol_choice()
                if choice1 == choice2 == choice3:
                    gewinn = symbols[choice1].win * einsatz[aktueller_einsatz]
                    print("Du hast gewonnen: " + str(gewinn) + "€")
                    show_start = time.time() * 1000
                    show_win = True
                    wins += 1
                    geld += gewinn

            elif event.key == pygame.K_r:
                geld = 50
                aktueller_einsatz = 0
                wins = 0
                print("Neuanfang")

            pygame.display.update()
