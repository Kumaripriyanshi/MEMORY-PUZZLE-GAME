import pygame
import sys
import time
import PuzzleSolutionModule
import welcomeWindowModule

class MainGame():
    def __init__(self,window,images,GameSounds):
        self.window=window
        self.images=images
        self.GameSounds=GameSounds
       
        

    def content(self):
        imageWidth=int(394/3)  #131
        imageHeight=int(410/3)   #136
       
        imageList=[self.images["piece6"],self.images["piece4"],self.images["piece8"],self.images["piece1"],self.images["piece2"],self.images["piece7"],self.images["piece3"],self.images["piece5"],self.images["piece9"]]
        desired_Position_Of_imageList=[self.images["piece1"],self.images["piece4"],self.images["piece7"],self.images["piece2"],self.images["piece5"],self.images["piece8"],self.images["piece3"],self.images["piece6"],self.images["piece9"]]
        mainl=[[self.images["piece6"],self.images["piece4"],self.images["piece8"]],[self.images["piece1"],self.images["piece2"],self.images["piece7"]],[self.images["piece3"],self.images["piece5"],self.images["piece9"]]]
        dimension_of_images={}
        position_of_images={}
        HintClicked=False

        #initializing the time __________
        initialTime=time.time()
      
        self.window.blit(pygame.transform.scale(self.images["newBg"], (550,700)),(-70,0)) 

        pygame.draw.rect(self.window,(255,255,255),[3,150,392,398])
      
        k=0
        tempy=0
        for i in range(0,3): 
            if i==0:tempy=150
            if i==1:tempy=147
            if i==2:tempy=144 
            for j in range(0,3):
                    img=imageList[k]
                    self.window.blit(img,(j*imageWidth+3,i*imageHeight+tempy)) 
                    pygame.display.update()
                    dimension_of_images[img]=(j*imageWidth+3,i*imageHeight+tempy)
                    position_of_images[img]=k
                    k+=1
  
        # print(position_of_images)
        while True:
            font=pygame.font.SysFont("Times New Roman",32)
            pygame.draw.rect(self.window,(0,0,0),[0,0,400,50])
                    
            Solution = font.render("Hint", True, (255,255,255))
            rect=pygame.draw.rect(self.window,(0,0,0,0),[2,6,Solution.get_width(),Solution.get_height()])
         
 
            Time = font.render("Time:", True, (255,255,255))
            Level = font.render("Level: 0", True, (0,0,0))
           
            self.window.blit(self.images["bulb"],(2,6))

            self.window.blit(Time,(280,6))
            self.window.blit(Level,(150,60))
          
           
            self.window.blit(self.images["solution"],(284,590))
            self.window.blit(self.images["restart"],(1,590))
            self.window.blit(self.images["levels"],(145,590))


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
                        # print(clicked)
                        clicked_image=self.findClickedImages(clicked,dimension_of_images,imageWidth,imageHeight)
                        posOfspace=self.findSpacePos(position_of_images)
                        self.ClickedImageCanSwap(clicked_image,posOfspace,position_of_images,dimension_of_images,desired_Position_Of_imageList)
                       
                        if HintClicked:
                            self.showNumbers(dimension_of_images,desired_Position_Of_imageList)
                        if (clicked[0] >=3 and clicked[0]<=110) and  (clicked[1]>=590 and clicked[1]<=643):
                            n=temppy=0
                            for i in range(0,3):  
                                    if i==0:temppy=150
                                    if i==1:temppy=147
                                    if i==2:temppy=144 
                                    for j in range(0,3):
                                        
                    
                                        img=imageList[n]
                                        self.window.blit(img,(j*imageWidth+3,i*imageHeight+temppy)) 
                                        pygame.display.update()

                                        dimension_of_images[img]=(j*imageWidth+3,i*imageHeight+temppy)
                                        position_of_images[img]=n
                                        n+=1
                          
                        elif (clicked[0] >=146 and clicked[0]<=254) and  (clicked[1]>=591 and clicked[1]<=644 ):
                            welcomeWindowModule.ShowLevelScreen(self,self.images,self.window,self.GameSounds,"mainGame",43)
                        
                        elif (clicked[0] >=284 and clicked[0]<=392) and  (clicked[1]>=592 and clicked[1]<=644 ):
                            n=temppy=0
                            for i in range(0,3):  
                                    if i==0:temppy=150
                                    if i==1:temppy=147
                                    if i==2:temppy=144 
                                    for j in range(0,3):
                                        img=imageList[n]
                                        self.window.blit(img,(j*imageWidth+3,i*imageHeight+temppy)) 
                                        pygame.display.update()

                                        dimension_of_images[img]=(j*imageWidth+3,i*imageHeight+temppy)
                                        position_of_images[img]=n
                                        n+=1
                                
                            self.solvePuzzle(mainl,dimension_of_images,imageList)
                            time.sleep(1)
                            self.GameOver()
     


                        if rect.collidepoint(clicked):
                                self.showNumbers(dimension_of_images,desired_Position_Of_imageList)
                                HintClicked=True
                     
     

                                

    def checkWinner(self,position_of_images,desired_Position_Of_imageList):
       
        count=0
        for i in range(9):
            if i==position_of_images[desired_Position_Of_imageList[i]]:
                count+=1

        data=""
        dt=0
        if count==9:
            with open("levels.txt","r") as r:
                data=r.read()
                data=data.split("\n")
                dt=int(data[len(data)-2])+1  
               
            with open("levels.txt","a") as w:
                w.write(str(dt)+"\n")

            while True:
                self.window.blit(self.images["winn"],(0,0)) 
                self.window.blit(self.images["next"],(70,550))   
                self.window.blit(self.images["homew"],(230,550))   
                pygame.display.flip()
                self.window.blit(self.images["coloredStarScale"],(170,100)) 
                self.window.blit(self.images["NormalcoloredStar"],(115,119)) 
                self.window.blit(self.images["NormalcoloredStar"],(240,119))

                pygame.display.update()
                for event in pygame.event.get():
                        if event.type==pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        elif event.type==pygame.KEYDOWN and event.key == pygame.K_SPACE:
                            self.content()
                        elif event.type==pygame.MOUSEBUTTONDOWN:
                            
                            clicked=event.pos
                            # print(clicked)
                            if (clicked[0] >=70 and clicked[0]<=169) and  (clicked[1]>=551 and clicked[1]<=610 ):
                                import P1
                            if (clicked[0] >=231 and clicked[0]<=578) and  (clicked[1]>=551 and clicked[1]<=610 ):
                                welcomeWindowModule.WelcomeScreen.StartwelcomeScreen(self)

                   
                
      
                  

    def GameOver(self):
        while True:
            font=pygame.font.SysFont("Times New Roman",100)

            self.window.fill((255,255,255))
            self.window.blit(self.images["over"],(0,0)) 

            self.window.blit(self.images["uncoloredStarScale"],(170,100)) 
            self.window.blit(self.images["uncoloredStar"],(115,119)) 
            self.window.blit(self.images["uncoloredStar"],(240,119))
           
            pygame.display.update()
            for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type==pygame.KEYDOWN and event.key == pygame.K_SPACE:
                       self.content()




    def findClickedImages(self,ClickedPos,dimension_of_images,imageWidth,imageHeight):
        for i in dimension_of_images.items():
            if (ClickedPos[0]>=i[1][0] and ClickedPos[0]<=i[1][0]+131) and(ClickedPos[1]>=i[1][1] and ClickedPos[1]<=i[1][1]+136):
                return i[0]



    def findSpacePos(self,position_of_images):
        for i in position_of_images.items():
            if i[0]==self.images["piece9"]:
                return i[1]


    
    def ClickedImageCanSwap(self,clicked_image,posOfspace,position_of_images,dimension_of_images,desired_Position_Of_imageList):
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
            # self.GameSounds["slide"].play()
            self.window.blit(clicked_image,dimension_of_images[clicked_image])
            self.window.blit(self.images["piece9"],dimension_of_images[self.images["piece9"]])

            temp=position_of_images[self.images["piece9"]]
            position_of_images[self.images["piece9"]]=position_of_images[clicked_image]
            position_of_images[clicked_image]=temp

            pygame.display.update()
            self.checkWinner(position_of_images,desired_Position_Of_imageList)

    

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
      
           


        
      
                            
       