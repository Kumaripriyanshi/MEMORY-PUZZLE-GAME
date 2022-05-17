import pygame
import sys
from welcomeWindowModule import *
from pygame import mixer
# import ImageClass

windoWidth=400
windoHeight=700

window=pygame.display.set_mode((windoWidth,windoHeight))

SetOfimages={
  
        "piece1":pygame.transform.scale(pygame.image.load("PROJECT_SEM_4/IMAGES/piece1.png").convert_alpha(),(130,132)),
        "piece2":pygame.transform.scale(pygame.image.load("PROJECT_SEM_4/IMAGES/piece2.png").convert_alpha(),(130,132)),
        "piece3":pygame.transform.scale(pygame.image.load("PROJECT_SEM_4/IMAGES/piece3.png").convert_alpha(),(130,132)),
        "piece4":pygame.transform.scale(pygame.image.load("PROJECT_SEM_4/IMAGES/piece4.png").convert_alpha(),(130,132)),
        "piece5":pygame.transform.scale(pygame.image.load("PROJECT_SEM_4/IMAGES/piece5.png").convert_alpha(),(130,132)),
        "piece6":pygame.transform.scale(pygame.image.load("PROJECT_SEM_4/IMAGES/piece6.png").convert_alpha(),(130,132)),
        "piece7":pygame.transform.scale(pygame.image.load("PROJECT_SEM_4/IMAGES/piece7.png").convert_alpha(),(130,132)),
        "piece8":pygame.transform.scale(pygame.image.load("PROJECT_SEM_4/IMAGES/piece8.png").convert_alpha(),(130,132)),
        "piece9":pygame.transform.scale(pygame.image.load("PROJECT_SEM_4/IMAGES/piece9.png").convert_alpha(),(130,132)),
    
        "Level1Image":pygame.image.load("PROJECT_SEM_4/IMAGES/Level1Img.png").convert_alpha(),
     
        "pi":pygame.image.load("PROJECT_SEM_4/IMAGES/play.png").convert_alpha(),
        "Lev":pygame.image.load("PROJECT_SEM_4/IMAGES/Lev.png").convert_alpha(),
        "right":pygame.image.load("PROJECT_SEM_4/IMAGES/rightLeft.png").convert_alpha(),
        "left":pygame.transform.rotate(pygame.image.load("PROJECT_SEM_4/IMAGES/rightLeft.png").convert_alpha(),180),
        "home":pygame.transform.scale(pygame.image.load("PROJECT_SEM_4/IMAGES/home.png").convert_alpha(),(44,44)),
        "coloredStar":pygame.transform.scale(pygame.image.load("PROJECT_SEM_4/IMAGES/coloredStar.png").convert_alpha(),(24,24)),
        "NormalcoloredStar":pygame.image.load("PROJECT_SEM_4/IMAGES/coloredStar.png").convert_alpha(),
        "coloredStarScale":pygame.transform.scale(pygame.image.load("PROJECT_SEM_4/IMAGES/coloredStar.png").convert_alpha(),(64,64)),
        "bulb":pygame.transform.scale(pygame.image.load("PROJECT_SEM_4/IMAGES/bulb.png").convert_alpha(),(30,30)),
        "uncoloredStar":pygame.image.load("PROJECT_SEM_4/IMAGES/uncoloredStar.png").convert_alpha(),
        "uncoloredStarScale":pygame.transform.scale(pygame.image.load("PROJECT_SEM_4/IMAGES/uncoloredStar.png").convert_alpha(),(64,64)),
       
        "over":pygame.transform.scale(pygame.image.load("PROJECT_SEM_4/IMAGES/over.png").convert_alpha(),(400,700)),
        "winn":pygame.transform.scale(pygame.image.load("PROJECT_SEM_4/IMAGES/WINN.png").convert_alpha(),(400,700)),
        "next":pygame.transform.scale(pygame.image.load("PROJECT_SEM_4/IMAGES/next.png").convert_alpha(),(100,60)),
        "homew":pygame.transform.scale(pygame.image.load("PROJECT_SEM_4/IMAGES/homeW.png").convert_alpha(),(100,60)),
        "exit":pygame.image.load("PROJECT_SEM_4/IMAGES/exit.png").convert_alpha(),
        "restart":pygame.transform.scale(pygame.image.load("PROJECT_SEM_4/IMAGES/restart.png").convert_alpha(),(110,55)),
        "solution":pygame.transform.scale(pygame.image.load("PROJECT_SEM_4/IMAGES/solution.png").convert_alpha(),(110,55)),
        "levels":pygame.transform.scale(pygame.image.load("PROJECT_SEM_4/IMAGES/levels.png").convert_alpha(),(110,55)),

        "league":pygame.transform.scale(pygame.image.load("PROJECT_SEM_4/IMAGES/lt.png").convert_alpha(),(400,700)),
        "nwL":pygame.transform.scale(pygame.image.load("PROJECT_SEM_4/IMAGES/nwL.png").convert_alpha(),(400,700)),
        
        "newBg":pygame.transform.scale(pygame.image.load("PROJECT_SEM_4/IMAGES/newBg.png").convert_alpha(),(400,700))

   }
pygame.mixer.init()
GameSounds={'click': pygame.mixer.Sound('PROJECT_SEM_4/SOUNDS/click.wav')}
screen=WelcomeScreen(window,SetOfimages,GameSounds)
if __name__=="__main__":
    pygame.init()
    # clock=pygame.time.Clock()
    pygame.display.set_caption("MEMORY PUZZLE GAME")
    while True:
        screen.StartwelcomeScreen()
        # pygame.quit()
        # sys.exit()
    