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
choice4 = 0
choice5 = 0
choice6 = 0
choice7 = 0
choice8 = 0
choice9 = 0

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
diagonal_line1 = pygame.image.load("textures/Untitled-1.png")
diagonal_line2 = pygame.image.load("textures/diagonal2.png")
horizontal_line1 = pygame.image.load("textures/Untitled-2.png")
horizontal_line2 = pygame.image.load("textures/Untitled-2.png")
horizontal_line3 = pygame.image.load("textures/Untitled-2.png")
font = pygame.font.SysFont('arial', 25)
pygame.display.set_caption("SlotSim")

pics[0] = pygame.transform.scale(pics[0], (50, 50))
pics[1] = pygame.transform.scale(pics[1], (50, 50))
pics[2] = pygame.transform.scale(pics[2], (50, 50))
pics[3] = pygame.transform.scale(pics[3], (50, 50))
pics[4] = pygame.transform.scale(pics[4], (50, 50))
pics[5] = pygame.transform.scale(pics[5], (50, 50))
pics[6] = pygame.transform.scale(pics[6], (50, 50))

horizontal_line1 = pygame.transform.scale(horizontal_line1, (400, 5))
horizontal_line2 = pygame.transform.scale(horizontal_line2, (400, 5))
horizontal_line3 = pygame.transform.scale(horizontal_line3, (400, 5))
diagonal_line1 = pygame.transform.scale(diagonal_line1, (400, 400))
diagonal_line2 = pygame.transform.scale(diagonal_line2, (400, 400))





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



# 0,064 0,078125 0,03375 0,02 0,01715 0,0008 0,0002 == 0,214025 -1€ == -0,785975

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

    #background = pygame.image.load("textures/slot.png")
    screen.blit(background, (0, 0))
    screen.blit(pics[choice1], (110, 450))
    screen.blit(pics[choice2], (285, 450))
    screen.blit(pics[choice3], (460, 450))
    screen.blit(pics[choice4], (110, 525))
    screen.blit(pics[choice5], (285, 525))
    screen.blit(pics[choice6], (460, 525))
    screen.blit(pics[choice7], (110, 600))
    screen.blit(pics[choice8], (285, 600))
    screen.blit(pics[choice9], (460, 600))

    screen.blit(letters_bets, (90, 695))
    screen.blit(letters_geld, (215, 695))
    screen.blit(letters_wins, (430, 695))

    if show_win and (int(time.time() * 1000) - show_start < 1000) and (gewinn >= 0):
        screen.blit(font.render(str(gewinn) + "€ gewonnen!", False, white), (240, 850))

        if choice1 == choice2 == choice3:
            screen.blit(horizontal_line1, (110, 470))
        if choice4 == choice5 == choice6:
            screen.blit(horizontal_line2, (110, 545))
        if choice7 == choice8 == choice9: 
            screen.blit(horizontal_line3, (110, 625))
        if choice1 == choice5 == choice9:    
            screen.blit(diagonal_line1, (110, 350))
        if choice3 == choice5 == choice7:
            screen.blit(diagonal_line2, (110, 350))

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
                    screen.blit(letters_reset, (150, 450))
                    pygame.display.update()
                    pygame.time.delay(2000)
                    screen.fill(black)
                    letters_reset = font.render("Du wachst in der Sparkasse auf!", False, white)
                    screen.blit(letters_reset, (130, 450))
                    pygame.display.update()
                    pygame.time.delay(2000)
                geld -= einsatz[aktueller_einsatz]
                gewinn = -einsatz[aktueller_einsatz]

                choice1 = symbol_choice()
                choice2 = symbol_choice()
                choice3 = symbol_choice()
                choice4 = symbol_choice()
                choice5 = symbol_choice()
                choice6 = symbol_choice()
                choice7 = symbol_choice()
                choice8 = symbol_choice()
                choice9 = symbol_choice()

                if choice1 == choice2 == choice3:
                    gewinn += symbols[choice1].win * einsatz[aktueller_einsatz]
                    show_start = time.time() * 1000
                    show_win = True
                    wins += 1
                    geld += gewinn

                if choice4 == choice5 == choice6:
                    gewinn += symbols[choice4].win * einsatz[aktueller_einsatz]
                    show_start = time.time() * 1000
                    show_win = True
                    wins += 1
                    geld += gewinn

                if choice7 == choice8 == choice9:
                 
                    gewinn += symbols[choice7].win * einsatz[aktueller_einsatz]
                    show_start = time.time() * 1000
                    show_win = True
                    wins += 1
                    geld += gewinn

                if choice1 == choice5 == choice9:
                   
                    gewinn += symbols[choice1].win * einsatz[aktueller_einsatz]
                    show_start = time.time() * 1000
                    show_win = True
                    wins += 1
                    geld += gewinn

                if choice3 == choice5 == choice7:
                    
                    gewinn += symbols[choice3].win * einsatz[aktueller_einsatz]
                    show_start = time.time() * 1000
                    show_win = True
                    wins += 1
                    geld += gewinn

                print("Du hast gewonnen: " + str(gewinn) + "€")

            elif event.key == pygame.K_r:
                geld = 50
                aktueller_einsatz = 0
                wins = 0
                print("Neuanfang")

            pygame.display.update()
