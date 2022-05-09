import pygame
import sys
from welcomeWindowModule import *
from pygame import mixer
# import ImageClass

windoWidth=400
windoHeight=700

window=pygame.display.set_mode((windoWidth,windoHeight))

SetOfimages={"bgimage":pygame.image.load("PROJECT_SEM_4/IMAGES/background.png").convert_alpha(),
        "bgmage":pygame.image.load("PROJECT_SEM_4/IMAGES/bg.png").convert_alpha(),
        "bgtop": pygame.image.load("PROJECT_SEM_4/IMAGES/bgtop.jpg").convert_alpha(),
        "character":pygame.image.load("PROJECT_SEM_4/IMAGES/character.jpg").convert_alpha(),
       "one": pygame.image.load("PROJECT_SEM_4/IMAGES/1.png").convert_alpha(),
        "image2":pygame.image.load("PROJECT_SEM_4/IMAGES/right.png").convert_alpha(),
        "image3": pygame.image.load("PROJECT_SEM_4/IMAGES/bottom.png").convert_alpha(),
        "image4": pygame.image.load("PROJECT_SEM_4/IMAGES/space.png").convert_alpha(),
        "puzzle": pygame.image.load("PROJECT_SEM_4/IMAGES/puzzle.png").convert_alpha(),
        "puzzle1": pygame.image.load("PROJECT_SEM_4/IMAGES/puzzle1.png").convert_alpha(),
       "image5U": pygame.transform.rotate(pygame.image.load("PROJECT_SEM_4/IMAGES/arrow.png").convert_alpha(),90),
        "image5L":pygame.transform.rotate(pygame.image.load("PROJECT_SEM_4/IMAGES/arrow.png").convert_alpha(),180),
        "image5D":pygame.transform.rotate(pygame.image.load("PROJECT_SEM_4/IMAGES/arrow.png").convert_alpha(),270),
        "image5R":pygame.image.load("PROJECT_SEM_4/IMAGES/arrow.png").convert_alpha(),
        "brain":pygame.image.load("PROJECT_SEM_4/IMAGES/brain.png").convert_alpha(),
        "piece1":pygame.image.load("PROJECT_SEM_4/IMAGES/piece1.png").convert_alpha(),
        "piece2":pygame.image.load("PROJECT_SEM_4/IMAGES/piece2.png").convert_alpha(),
        "piece3":pygame.image.load("PROJECT_SEM_4/IMAGES/piece3.png").convert_alpha(),
        "piece4":pygame.image.load("PROJECT_SEM_4/IMAGES/piece4.png").convert_alpha(),
        "piece6":pygame.image.load("PROJECT_SEM_4/IMAGES/piece6.png").convert_alpha(),
        "piece5":pygame.image.load("PROJECT_SEM_4/IMAGES/piece5.png").convert_alpha(),
        "piece7":pygame.image.load("PROJECT_SEM_4/IMAGES/piece7.png").convert_alpha(),
        "piece8":pygame.image.load("PROJECT_SEM_4/IMAGES/piece8.png").convert_alpha(),
        "piece9":pygame.image.load("PROJECT_SEM_4/IMAGES/piece9.png").convert_alpha(),
        "user":pygame.image.load("PROJECT_SEM_4/IMAGES/user.png").convert_alpha(),
        "Level1Image":pygame.image.load("PROJECT_SEM_4/IMAGES/Level1Img.png").convert_alpha(),
        "Lock":pygame.image.load("PROJECT_SEM_4/IMAGES/lock.png").convert_alpha(),
        "bluebg":pygame.image.load("PROJECT_SEM_4/IMAGES/bluebg.jpg").convert_alpha(),
        "challenge":pygame.image.load("PROJECT_SEM_4/IMAGES/challenge.png").convert_alpha(),
        "pi":pygame.image.load("PROJECT_SEM_4/IMAGES/pi.png").convert_alpha(),
        "Lev":pygame.image.load("PROJECT_SEM_4/IMAGES/Lev.png").convert_alpha(),
        "right":pygame.image.load("PROJECT_SEM_4/IMAGES/rightLeft.png").convert_alpha(),
        "left":pygame.transform.rotate(pygame.image.load("PROJECT_SEM_4/IMAGES/rightLeft.png").convert_alpha(),180),
        "home":pygame.transform.scale(pygame.image.load("PROJECT_SEM_4/IMAGES/home.png").convert_alpha(),(44,44)),
        "coloredStar":pygame.transform.scale(pygame.image.load("PROJECT_SEM_4/IMAGES/coloredStar.png").convert_alpha(),(24,24)),
        "NormalcoloredStar":pygame.image.load("PROJECT_SEM_4/IMAGES/coloredStar.png").convert_alpha(),
        "coloredStarScale":pygame.transform.scale(pygame.image.load("PROJECT_SEM_4/IMAGES/coloredStar.png").convert_alpha(),(64,64)),
        "bulb":pygame.transform.scale(pygame.image.load("PROJECT_SEM_4/IMAGES/bulb.png").convert_alpha(),(30,30)),
        "uncoloredStar":pygame.image.load("PROJECT_SEM_4/IMAGES/uncoloredStar.png").convert_alpha(),
        "uncoloredStarScale":pygame.transform.scale(pygame.image.load("PROJECT_SEM_4/IMAGES/uncoloredStar.png").convert_alpha(),(64,64))
   }
pygame.mixer.init()
GameSounds={'click': pygame.mixer.Sound('PROJECT_SEM_4/SOUNDS/click.wav')}
screen=WelcomeScreen(window,SetOfimages,GameSounds)
if __name__=="__main__":
    pygame.init()
    # clock=pygame.time.Clock()
    pygame.display.set_caption("checking game")
    while True:
        screen.StartwelcomeScreen()
        pygame.quit()
        sys.exit()
    