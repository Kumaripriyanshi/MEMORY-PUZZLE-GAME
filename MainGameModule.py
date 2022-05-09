import pygame
import sys
import time
from  tkinter import * 
import PuzzleSolutionModule 
from copy import deepcopy
from colorama import Fore, Back, Style


class MainGame():
    def __init__(self,window,images,GameSounds):
        self.window=window
        self.images=images
        self.GameSounds=GameSounds

    def content(self):
        imageWidth=int(394/3)
        imageHeight=int(410/3)
        print(imageHeight,imageWidth)
        Goal=[[self.images["piece1"],self.images["piece4"],self.images["piece7"]],[self.images["piece2"],self.images["piece5"],self.images["piece8"]],[self.images["piece3"],self.images["piece6"],self.images["piece9"]]]
        imageList=[self.images["piece6"],self.images["piece4"],self.images["piece8"],self.images["piece1"],self.images["piece2"],self.images["piece7"],self.images["piece3"],self.images["piece5"],self.images["piece9"]]
        
        desired_Position_Of_imageList=[self.images["piece1"],self.images["piece4"],self.images["piece7"],self.images["piece2"],self.images["piece5"],self.images["piece8"],self.images["piece3"],self.images["piece6"],self.images["piece9"]]
        HintReferencePosition={self.images["piece1"]:1,self.images["piece4"]:2,self.images["piece7"]:3,self.images["piece2"]:4,self.images["piece5"]:5,self.images["piece8"]:6,self.images["piece3"]:7,self.images["piece6"]:8}
        # imageList=[self.images["piece6"],self.images["piece4"],self.images["piece8"],self.images["piece1"],self.images["piece2"],self.images["piece7"],self.images["piece3"],self.images["piece5"],self.images["piece9"]]
        mainl=[[self.images["piece6"],self.images["piece4"],self.images["piece8"]],[self.images["piece1"],self.images["piece2"],self.images["piece7"]],[self.images["piece3"],self.images["piece5"],self.images["piece9"]]]
        dimension_of_images={}
        position_of_images={}
        HintClicked=False

        #initializing the time __________
        initialTime=time.time()
        self.window.fill((255,255,255))
        pygame.draw.rect(self.window,(0,0,0),[0.4,150,400,398])
        solveRectCoor=[280,560,90,40]
        k=0
        for i in range(0,3):  
                for j in range(0,3):
                    if i==0:temp=150
                    else: temp=147

                    if j==0:tempx=0
                    else:tempx=6

                    if j==2:tempx=11
                    if i==2:temp=144
 
                    img=imageList[k]
                    self.window.blit(img,(j*imageWidth+1+tempx,i*imageHeight+temp)) 
                    pygame.display.update()

                    dimension_of_images[img]=(j*imageWidth+1+tempx,i*imageHeight+temp)
                    position_of_images[img]=k
                    self.checkWinner(position_of_images,desired_Position_Of_imageList)
                    k+=1
        
        while True:
            font=pygame.font.SysFont("Times New Roman",32)
            pygame.draw.rect(self.window,(0,0,0),[0,0,400,50])
                    
            Solution = font.render("Hint", True, (255,255,255))
            rect=pygame.draw.rect(self.window,(0,0,0,0),[2,6,Solution.get_width(),Solution.get_height()])
            Score = font.render("Point :20", True, (255,19,0))
            self.window.blit(Score,(2,60))
 
            Time = font.render("Time:", True, (255,255,255))
            Level = font.render("Level: 1", True, (0,0,0))
            Solve = font.render("Solve", True, (255,255,255))
            # self.window.blit(Solution,(2,6))
            self.window.blit(self.images["bulb"],(2,6))

            self.window.blit(Time,(280,6))
            self.window.blit(Level,(150,60))
          
            solveRect=pygame.draw.rect(self.window,(0,0,0),solveRectCoor)
            self.window.blit(Solve,(287,561))

            x=int(time.time()-initialTime)
            Time_text = font.render(f'{60-x}', True, (255,255,255))
            self.window.blit(Time_text,(358,7))
            pygame.display.update()
            if 60-x ==0:
                self.GameOver()
             

        #    -----------------Listening events here----------------
            for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        self.GameSounds["click"].play()
                        clicked=event.pos
                        clicked_image=self.findClickedImages(clicked,dimension_of_images,imageWidth,imageHeight)
                        posOfspace=self.findSpacePos(position_of_images)
                        self.ClickedImageCanSwap(clicked_image,posOfspace,position_of_images,dimension_of_images)
                        if HintClicked:
                            self.showNumbers(dimension_of_images,desired_Position_Of_imageList)

                        if rect.collidepoint(clicked):
                                self.showNumbers(dimension_of_images,desired_Position_Of_imageList)
                                HintClicked=True
                        if solveRect.collidepoint(clicked):
                            k=0
                            for i in range(0,3):  
                                    for j in range(0,3):
                                        if i==0:temp=150
                                        else: temp=147

                                        if j==0:tempx=0
                                        else:tempx=6

                                        if j==2:tempx=11
                                        if i==2:temp=144
                    
                                        img=imageList[k]
                                        self.window.blit(img,(j*imageWidth+1+tempx,i*imageHeight+temp)) 
                                        pygame.display.update()

                                        dimension_of_images[img]=(j*imageWidth+1+tempx,i*imageHeight+temp)
                                        position_of_images[img]=k
                                        k+=1
                                
                            self.solvePuzzle(mainl,dimension_of_images,imageList)
                            time.sleep(2)
                            self.GameOver()
     

                                

    def checkWinner(self,position_of_images,desired_Position_Of_imageList):
        flagpost=0
        for index,item in enumerate(position_of_images):
            if item==desired_Position_Of_imageList[index]:
                flagpost=1
                print("winner!! winner!!")
            else:
                flagpost=0
                break
        data=""
        dt=0
        if flagpost==1:
            with open("levels.txt","r") as r:
                data=r.read()
                data=data.split("\n")
                dt=int(data[len(data)-2])+1  
               
            with open("levels.txt","a") as w:
                w.write(str(dt)+"\n")

            while True:
                font=pygame.font.SysFont("Times New Roman",100)
                self.window.fill((255,255,255))
                self.window.blit(self.images["uncoloredStarScale"],(170,100)) 
                self.window.blit(self.images["uncoloredStar"],(115,119)) 
                self.window.blit(self.images["uncoloredStar"],(240,119))
                Game = font.render("Game", True, (255,19,0))
                over = font.render("Over", True, (255,19,0))
                self.window.blit(Game,(90,175))
                self.window.blit(over,(102,270))
                font=pygame.font.SysFont("Times New Roman",24)
                restart = font.render(" Press Space To Restart The Game ", True, (255,19,0))
                self.window.blit(restart,(30,380))
                pygame.display.update()
                for event in pygame.event.get():
                        if event.type==pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        elif event.type==pygame.KEYDOWN and event.key == pygame.K_SPACE:
                            self.content()

                   
                
      
                  

    def GameOver(self):
        while True:
            font=pygame.font.SysFont("Times New Roman",100)

            self.window.fill((255,255,255))
            self.window.blit(self.images["uncoloredStarScale"],(170,100)) 
            self.window.blit(self.images["uncoloredStar"],(115,119)) 
            self.window.blit(self.images["uncoloredStar"],(240,119))
            Game = font.render("Game", True, (255,19,0))
            over = font.render("Over", True, (255,19,0))

            self.window.blit(Game,(90,175))
            self.window.blit(over,(102,270))
            font=pygame.font.SysFont("Times New Roman",24)
            restart = font.render(" Press Space To Restart The Game ", True, (255,19,0))
            self.window.blit(restart,(30,380))
            pygame.display.update()
            for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type==pygame.KEYDOWN and event.key == pygame.K_SPACE:
                       self.content()




    def findClickedImages(self,ClickedPos,dimension_of_images,imageWidth,imageHeight):
        for i in dimension_of_images.items():
            if (ClickedPos[0]>=i[1][0] and ClickedPos[0]<=i[1][0]+imageWidth) and(ClickedPos[1]>=i[1][1] and ClickedPos[1]<=i[1][1]+imageHeight):
                return i[0]



    def findSpacePos(self,position_of_images):
        for i in position_of_images.items():
            if i[0]==self.images["piece9"]:
                return i[1]


    
    def ClickedImageCanSwap(self,clicked_image,posOfspace,position_of_images,dimension_of_images):
        pos_ofClickedImg=None
        for i in position_of_images.items():
            if i[0]==clicked_image:
                pos_ofClickedImg=i[1]
       
        up=down=right=left=None
        if pos_ofClickedImg!=None:
            up=pos_ofClickedImg-3
            down=pos_ofClickedImg+3
            left=pos_ofClickedImg-1
            right=pos_ofClickedImg+1
        
        if right==posOfspace or down==posOfspace or left==posOfspace or up==posOfspace:
            temp=dimension_of_images[self.images["piece9"]]
            dimension_of_images[self.images["piece9"]]=dimension_of_images[clicked_image]
            dimension_of_images[clicked_image]=temp
            self.window.blit(clicked_image,dimension_of_images[clicked_image])
            self.window.blit(self.images["piece9"],dimension_of_images[self.images["piece9"]])

            temp=position_of_images[self.images["piece9"]]
            position_of_images[self.images["piece9"]]=position_of_images[clicked_image]
            position_of_images[clicked_image]=temp

            pygame.display.update()
    

    def showNumbers(self,dimension_of_images,desired_Position_Of_imageList):
        font=pygame.font.SysFont("Times New Roman",32)
        k=0
        for i in range(0,len(desired_Position_Of_imageList)):  
                if i==8: break
                image=desired_Position_Of_imageList[i]
                m = font.render(str(i+1), True, (255,255,255))
                self.window.blit(m,(dimension_of_images[image][0]+50,dimension_of_images[image][1]+50) )
               
                pygame.display.update()
       
                                    
    def solvePuzzle(self,mainl,dimension_of_images,imageList):
      PuzzleSolutionModule.start(mainl,dimension_of_images,self.window,imageList)
      
           


        
      
                            
       