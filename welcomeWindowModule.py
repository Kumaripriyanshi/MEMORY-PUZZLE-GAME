import MainGameModule
import pygame
import random
import sys
from datetime import datetime
import time
from pygame import mixer
# import ImageClass

green = (0, 255, 0)
blue = (0, 0, 128)
aqua=(0,104,139)

LevlClicked=False
class WelcomeScreen():
    def __init__(self,window,images,GameSounds):
        self.window=window
        self.images=images
        self.GameSounds=GameSounds
        self.mainGameScreen=MainGameModule.MainGame(self.window,self.images,self.GameSounds)

        
        
    def StartwelcomeScreen(self):
        """This method will show the welcome screen i.e starting window of the game"""
        # texty=160
        # textx=10
        step=5
        user_text=""
        with open("PROJECT_SEM_4/Name.txt","r") as f:
                     user_text=f.readline()

        rectangle=[3,52,1,25]   #user rectangle coor
        # imageWidth=191
        # imageHeight=137
        playHover=False
        imageWidth=100     #temporary
        imageHeight=100    #temporary
        rectCoordinates=[]      #for motion of  rectangles
        clock=pygame.time.Clock()         #FPS
        inx=rectCoordinates
        li=[]
        # image =self.images["piece5"]
        image =self.images["pi"]
        imagen =self.images["Lev"]


        clock = pygame.time.Clock()

        DEFAULT_IMAGE_SIZE = (235,39)
        DEFAULT_IMAGE_POSITION = (90,350)
        imagex=pygame.Surface((235,41))
        coord=(235,41)
        posi=(90,410)

        
        while True :
            self.window.fill((0,0,0))        #black filling
            font=pygame.font.SysFont("Times New Roman",32)       
          # rendering the text____________
            welcometext = font.render("Welcome To", True, blue)
            Braintext = font.render("Brainly", True, blue)
            clciktext = font.render("Press Space to start Game", True, blue)
            Highscore = font.render("HighScore", True, (255,255,255))
            levels = font.render("Level", True, (255,255,255))
            play = font.render("Play", True, (255,255,255))
            Level = font.render("Levels", True, (255,255,255))
            Music = font.render("Music", True, (255,255,255))

            self.window.blit(self.images["bluebg"],(0,0)) 
            pygame.draw.rect(self.window,(250,250,250),[1,1,399,699],2,3)   

         

            clock.tick(30)
    
  
  
            #blitting the images____
            # self.window.blit(self.images["bgmage"],(0,50)) 
            # self.window.blit(self.images["puzzle"],(68,490)) 
            # self.window.blit(self.images["puzzle"],(290,590))
            # self.window.blit(self.images["user"],(18,4)) 

            # self.window.blit(textt, (10,160))
            # window.blit(puzzle1,(270,50)) 
            # rectangle=[230,100,130,40]  



            # userInput function here___________
            # rectangle=self.UserInput(rectangle,user_text)


            #animating the rectangles here__________
            # pygame.draw.rect(self.window,(0,0,0),[50,50,32,44])
            # inx=self.animateRectangle(rectCoordinates,imageWidth,imageHeight,step,font,inx)

            # blitting the texts____________
            # self.window.blit(welcometext, (textx,texty))
            # self.window.blit(clciktext, (20,350))
            # self.window.blit(Braintext, (144,200))
            # self.window.blit(Highscore,(259,6))
            # self.window.blit(levels,(119,6)) 
            tempWi=Level.get_width()+152
            # print("s",tempWi,Level.get_height()+5)
            # print(tempWi,play.get_height())
            pygame.draw.rect(self.window,(250,250,250),[90,350,tempWi,play.get_height()+5],2,3)
            pygame.draw.rect(self.window,(250,250,250),[90,410,tempWi,Level.get_height()+7],2,3)
            self.window.blit(pygame.transform.scale(image, DEFAULT_IMAGE_SIZE), DEFAULT_IMAGE_POSITION)
            self.window.blit(pygame.transform.scale(imagen, coord),posi)
            pygame.draw.rect(self.window,(250,250,250),[90,470,tempWi,Music.get_height()+5],2,3)

            # self.window.blit(play,(179,350)) 
            # self.window.blit(self.images["bluebg"],(90,350)) 

            # self.window.blit(Level,(179,410)) 
            self.window.blit(Music,(179,470)) 
            self.window.blit(self.images["challenge"],(10,20)) 
           




            pygame.display.update()
            
            #handling the events here___________
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                #keyboard events_______________
                # elif event.type==pygame.KEYDOWN :
                #     if event.key == pygame.K_BACKSPACE:
                #       user_text = user_text[:-1]
                #     else:
                #           user_text += event.unicode
                #           with open("PROJECT_SEM_4/Name.txt","w") as f:
                #             f.write(f"{user_text}")
                elif event.type==pygame.MOUSEMOTION:
                    action=event.pos
                   
                    if (action[0]>90 and action[0]<321 ) and (action[1]>350 and action[1]<386):
                      
                        DEFAULT_IMAGE_SIZE=self.scaleUp(DEFAULT_IMAGE_SIZE,image,245,DEFAULT_IMAGE_POSITION)
                      
                    else :
                        DEFAULT_IMAGE_SIZE=self.scaleDown(DEFAULT_IMAGE_SIZE,image,235,DEFAULT_IMAGE_POSITION)

                        
                          
                    if  (action[0]>90 and action[0]<321 ) and (action[1]>410 and action[1]<452):
                        coord=self.scaleUp(coord,imagen,245,(90,410))

                    else :
                        coord=self.scaleDown(coord,imagen,235,(90,410))

                #mouse events_______________    
                elif event.type==pygame.MOUSEBUTTONDOWN:
                    clicked = event.pos
                    self.GameSounds["click"].play()
                    # print(clicked)
                    # if rectangle.collidepoint(clicked):
                    #     user_text=""
                    if (action[0]>90 and action[0]<321 ) and (action[1]>350 and action[1]<386): 
                        self.mainGameScreen.content()
                        return   
                
                    # if (clicked[0] >=263 and clicked[0]<=391) and  (clicked[1]>=6 and clicked[1]<=39 ):
                    #     Action=self.ShowHighScore()
                    #     if Action=="back":
                    #         self.StartwelcomeScreen()
                    #     print("Highscore")
                        
                    
                    elif  (action[0]>90 and action[0]<321 ) and (action[1]>410 and action[1]<452):
                        Action=self.ShowLevelScreen(43)
                        if Action=="back":
                            self.StartwelcomeScreen()
                        print("level")
            clock.tick(60)
           
        
    
    def ShowLevelScreen(self,CarX):
        """Responsible for dislaying levels on the window """
        # Level1Image
        carousel=[self.images["Level1Image"],self.images["Level1Image"]]
        clickIndx=0
        defSize=(318,302)
        global LevlClicked
        data=[]
        scoreList={0:3,1:6}
        score=0
        while True :
            self.window.fill((16,78,139)) 
            with open("levels.txt","r") as r:
                data=r.read()
                data=data.split("\n")
               
            pygame.draw.rect(self.window,(250,250,250),[1,1,399,699],2,3)   
            pygame.draw.rect(self.window,(0,0,0),[1,1,399,50],2,3)   
            self.window.blit(self.images["home"],(0,0)) 

          
#star rectangle------------
            font=pygame.font.SysFont("Times New Roman",32)
            pygame.draw.rect(self.window,(250,250,250),[300,11,80,30],2,10)   
            self.window.blit(self.images["coloredStar"],(300,12)) 
            scoreText=font.render(": "+str(score), True, (255, 255, 255))
            self.window.blit(scoreText,(324,7))

        
            if clickIndx<0 or clickIndx>len(carousel)-1: clickIndx=0
            self.window.blit(pygame.transform.scale(carousel[clickIndx], defSize), (CarX,250))

            
            self.window.blit(self.images["left"], (5,370))
            self.window.blit(self.images["right"], (355,370))

            
            if str(clickIndx) in data :
                 for k in scoreList:
                    if str(k) in data:
                        score=scoreList[k]
                 self.window.blit(self.images["coloredStarScale"],(170,170)) 
                 self.window.blit(self.images["NormalcoloredStar"],(115,189)) 
                 self.window.blit(self.images["NormalcoloredStar"],(240,189))
            else:
                self.window.blit(self.images["uncoloredStarScale"],(170,170)) 
                self.window.blit(self.images["uncoloredStar"],(115,189)) 
                self.window.blit(self.images["uncoloredStar"],(240,189))

            text = font.render(f"Level : {clickIndx}", True, (255,255,255))
            self.window.blit(text, (148,70))
            if LevlClicked: return

             
            
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type==pygame.MOUSEMOTION:
                    action=event.pos
                    if (action[0]>51 and action[0]<349 ) and (action[1]>248 and action[1]<550):
                        defSize=self.scaleUp(defSize,carousel[clickIndx],328,(CarX,250))
                    else :
                        defSize=self.scaleDown(defSize,carousel[clickIndx],318,(CarX,250))
                elif event.type==pygame.MOUSEBUTTONDOWN:
                    self.GameSounds["click"].play()
                    clicked = event.pos
                    print("cl",clicked)
                    if (clicked[0] >=0 and clicked[0]<=53) and  (clicked[1]>=0 and clicked[1]<=41 ):
                        return "back"
                    if (clicked[0] >=7 and clicked[0]<=41) and  (clicked[1]>=375 and clicked[1]<=411 ):
                        # print("<<")
                      
                        LevlClicked=True
                        flag=self.animateToLeft(clickIndx,carousel)
                        clickIndx-=1
                        if flag: LevlClicked=False
                   
                    if (clicked[0] >=368 and clicked[0]<=397) and  (clicked[1]>=378 and clicked[1]<=409 ):
                        # print(">>")
                        LevlClicked=True
                        flag=self.animateToRight(clickIndx,carousel)
                        clickIndx+=1
                        if flag: LevlClicked=False
                    if (clicked[0] >=46 and clicked[0]<=363) and  (clicked[1]>=247 and clicked[1]<=553 ) and clickIndx==0:
                       self.mainGameScreen.content()
                       return   

          
            pygame.display.update()

    def scaleUp(self,defSize,image,size,pos):
        l=list(defSize)
        step=5
        while l[0]!=size:
            self.window.blit(pygame.transform.scale(image, defSize), pos)
            pygame.display.flip()
            l[0]+=step
            l[1]+=step
            defSize=tuple(l)
            time.sleep(0.1)
        return defSize
        
    def scaleDown(self,defSize,image,size,pos):
        l=list(defSize)
        step=-5
        while l[0]!=size:
            self.window.blit(pygame.transform.scale(image, defSize), pos)
            pygame.display.flip()
            l[0]+=step
            l[1]+=step
            defSize=tuple(l)
            time.sleep(0.1)
        return defSize
    
     

    
    def animateToLeft(self,clickIndx,carousel):
        CarX=47
        img=carousel[clickIndx]
        while True:
            CarX-=60
            self.ShowLevelScreen(CarX)
            # if clickIndx!=0:
            #      self.window.blit(self.images["Lock"], (CarX-20,250))
            time.sleep(0.1)
            pygame.display.flip()
            if CarX<-400: break
        return True

            
    def animateToRight(self,clickIndx,carousel):
        # print("right")
        CarX=50
        img=carousel[clickIndx]
        while True:
            CarX+=60
            self.ShowLevelScreen(CarX)
            # if clickIndx!=0:
            #   self.window.blit(self.images["Lock"], (CarX+90,390))
            time.sleep(0.1)
            pygame.display.flip()
            if CarX>450: break
        return True
        
       

    def UserInput(self,rectangle,user_text):
            """Responsible for taking input from the user """
            rectangle=pygame.draw.rect(self.window,(0,0,0),rectangle)
            font=pygame.font.SysFont("Times New Roman",22)
            user_textt=font.render(user_text, True, (255, 255, 255))
            self.window.blit(user_textt,(rectangle.x+5,rectangle.y-1))
            self.window.blit(self.images["brain"],(264,170))
            rectangle.w = max(30, user_textt.get_width()+10)
            return rectangle
       