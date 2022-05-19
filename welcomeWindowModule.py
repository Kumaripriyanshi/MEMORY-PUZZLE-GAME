import MainGameModule
import pygame
import sys
# from datetime import datetime
import time

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
        # step=5
       
        self=WelcomeScreen(self.window,self.images,self.GameSounds)
        image =self.images["pi"]
        imagen =self.images["Lev"]
        Exitimg=self.images["exit"]


        clock = pygame.time.Clock()

        DEFAULT_IMAGE_SIZE = (238,47)
        DEFAULT_IMAGE_POSITION = (80,390)
     
        coord=(238,47)
        posi=(80,465)

        Exitcoord=(238,47)
        Exitposi=(80,543)

        
        while True :
         
            font=pygame.font.SysFont("Trebuchet MS",32)       
        
            self.window.blit(self.images["league"],(0,0)) 
          

            pygame.draw.rect(self.window,(250,250,250),[1,1,399,699],2,3)   

         

            clock.tick(30)
            pygame.draw.rect(self.window,(250,250,250),[80,390,240,48],2,3)
            pygame.draw.rect(self.window,(250,250,250),[80,465,240,48],2,3)
            pygame.draw.rect(self.window,(250,250,250),[80,543,240,48],2,3)
            self.window.blit(pygame.transform.scale(image, DEFAULT_IMAGE_SIZE), DEFAULT_IMAGE_POSITION)
            self.window.blit(pygame.transform.scale(imagen, coord),posi)
            self.window.blit(pygame.transform.scale(Exitimg, Exitcoord),Exitposi)

            pygame.display.update()
            
            #handling the events here___________
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                elif event.type==pygame.MOUSEMOTION:
                    action=event.pos
                   
                    if (action[0]>85 and action[0]<321 ) and (action[1]>391 and action[1]<434):
                        DEFAULT_IMAGE_SIZE=self.scaleUp(DEFAULT_IMAGE_SIZE,image,248,DEFAULT_IMAGE_POSITION)
                    else :
                        DEFAULT_IMAGE_SIZE=self.scaleDown(DEFAULT_IMAGE_SIZE,image,238,DEFAULT_IMAGE_POSITION)

                        
                          
                    if  (action[0]>85 and action[0]<321 ) and (action[1]>468 and action[1]<512):
                        coord=self.scaleUp(coord,imagen,248,posi)
                    else :
                        coord=self.scaleDown(coord,imagen,238,posi)

                    
                    if  (action[0]>85 and action[0]<321 ) and (action[1]>547 and action[1]<587):
                        Exitcoord=self.scaleUp(Exitcoord,self.images["exit"],248,Exitposi)
                    else :
                        Exitcoord=self.scaleDown(Exitcoord,self.images["exit"],238,Exitposi)

                #mouse events_______________    
                elif event.type==pygame.MOUSEBUTTONDOWN:
                    clicked = event.pos
                    self.GameSounds["click"].play()
                    # print(clicked)
                  
                    if (action[0]>85 and action[0]<321 ) and (action[1]>391 and action[1]<434): 
                        self.mainGameScreen.content()
                    
                    elif (action[0]>85 and action[0]<321 ) and (action[1]>468 and action[1]<512):
                        Action=ShowLevelScreen(self,self.images,self.window,self.GameSounds,__name__,43)
                        # print("level")
                        # return
                        if Action=="back":
                            self.StartwelcomeScreen()
                    elif (action[0]>85 and action[0]<321 ) and (action[1]>547 and action[1]<587):
                        pygame.quit()
                        sys.exit()
            clock.tick(60)
           
        
    
    

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
            ShowLevelScreen(self,self.images,self.window,self.GameSounds,__name__,CarX)
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
            ShowLevelScreen(self,self.images,self.window,self.GameSounds,__name__,CarX)
            time.sleep(0.1)
            pygame.display.flip()
            if CarX>450: break
        return True
        
       

    

def ShowLevelScreen(self,images,window,GameSounds,call,CarX):
        """Responsible for dislaying levels on the window """
        # Level1Image
        carousel=[images["Level1Image"],images["Level2Image"]]
        mainGameScreen=MainGameModule.MainGame(window,images,GameSounds)

        clickIndx=0
        defSize=(318,302)
        global LevlClicked
        data=[]
        scoreList={0:3,1:6}
        score=0
        while True :
            window.fill((16,78,139)) 
       
            window.blit(images["nwL"],(0,0))

            with open("levels.txt","r") as r:
                data=r.read()
                data=data.split("\n")
               
            pygame.draw.rect(window,(250,250,250),[1,1,399,699],2,3)   
    
          
#star rectangle------------
            font=pygame.font.SysFont("Times New Roman",32)
            scoreText=font.render(str(score), True, (255, 255, 255))
            window.blit(scoreText,(356,8))

        
            if clickIndx<0 or clickIndx>len(carousel)-1: clickIndx=0
            window.blit(pygame.transform.scale(carousel[clickIndx], defSize), (CarX,250))

            
            window.blit(images["left"], (5,370))
            window.blit(images["right"], (355,370))

            
            if str(clickIndx) in data :
                 for k in scoreList:
                    if str(k) in data:
                        score=scoreList[k]
                 window.blit(images["coloredStarScale"],(170,170)) 
                 window.blit(images["NormalcoloredStar"],(115,189)) 
                 window.blit(images["NormalcoloredStar"],(240,189))
            else:
                window.blit(images["uncoloredStarScale"],(170,170)) 
                window.blit(images["uncoloredStar"],(115,189)) 
                window.blit(images["uncoloredStar"],(240,189))
            
            text = font.render(f"{clickIndx}", True, (255,255,255))
            window.blit(text, (250,75))
            if LevlClicked: return

             
            
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type==pygame.MOUSEMOTION:
                    action=event.pos
                    if (action[0]>51 and action[0]<349 ) and (action[1]>248 and action[1]<550):
                        defSize=WelcomeScreen.scaleUp(self,defSize,carousel[clickIndx],328,(CarX,250))
                    else :
                        defSize=WelcomeScreen.scaleDown(self,defSize,carousel[clickIndx],318,(CarX,250))
                elif event.type==pygame.MOUSEBUTTONDOWN:
                    GameSounds["click"].play()
                    clicked = event.pos
                    # print("cl",clicked)
                    if (clicked[0] >=0 and clicked[0]<=53) and  (clicked[1]>=0 and clicked[1]<=41 ):
                        if call=="__main__":return "back" 
                        else:
                            WelcomeScreen.StartwelcomeScreen(WelcomeScreen(window,images,GameSounds))
                    if (clicked[0] >=7 and clicked[0]<=41) and  (clicked[1]>=375 and clicked[1]<=411 ):
                        # print("<<")
                        LevlClicked=True
                        flag=WelcomeScreen.animateToLeft(self,clickIndx,carousel)
                        clickIndx-=1
                        if flag: LevlClicked=False
                   
                    if (clicked[0] >=368 and clicked[0]<=397) and  (clicked[1]>=378 and clicked[1]<=409 ):
                        # print(">>")
                        LevlClicked=True
                        flag=WelcomeScreen.animateToRight(self,clickIndx,carousel)
                        clickIndx+=1
                        if flag: LevlClicked=False
                    if (clicked[0] >=46 and clicked[0]<=363) and  (clicked[1]>=247 and clicked[1]<=553 ) and clickIndx==0:
                         mainGameScreen.content()
                     
                    if (clicked[0] >=46 and clicked[0]<=363) and  (clicked[1]>=247 and clicked[1]<=553 ) and clickIndx==1:
                       import P1
                       
          
            pygame.display.update()
       

