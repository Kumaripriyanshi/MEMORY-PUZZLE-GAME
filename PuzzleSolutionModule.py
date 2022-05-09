from copy import deepcopy
# from glob import glob
# from colorama import Fore, Back, Style
import pygame
import time

#direction matrix
DIRECTIONS = {"U": [-1, 0], "D": [1, 0], "L": [0, -1], "R": [0, 1]}
#target matrix
END = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
# game=MainGame()
desired_Position_Of_imageList=[]
imageList=[]
dimension_of_images=[]
window=None
mainl=[]

# unicode for draw puzzle in command promt or terminal
# left_down_angle = '\u2514'
# right_down_angle = '\u2518'
# right_up_angle = '\u2510'
# left_up_angle = '\u250C'

# middle_junction = '\u253C'
# top_junction = '\u252C'
# bottom_junction = '\u2534'
# right_junction = '\u2524'
# left_junction = '\u251C'

#bar color
# bar = Style.BRIGHT + Fore.CYAN + '\u2502' + Fore.RESET + Style.RESET_ALL
# dash = '\u2500'

# #Line draw code
# first_line = Style.BRIGHT + Fore.CYAN + left_up_angle + dash + dash + dash + top_junction + dash + dash + dash + top_junction + dash + dash + dash + right_up_angle + Fore.RESET + Style.RESET_ALL
# middle_line = Style.BRIGHT + Fore.CYAN + left_junction + dash + dash + dash + middle_junction + dash + dash + dash + middle_junction + dash + dash + dash + right_junction + Fore.RESET + Style.RESET_ALL
# last_line = Style.BRIGHT + Fore.CYAN + left_down_angle + dash + dash + dash + bottom_junction + dash + dash + dash + bottom_junction + dash + dash + dash + right_down_angle + Fore.RESET + Style.RESET_ALL
ListUpd=imageList  

listOfPastARrryas=[]
def updateList(array,mlm):
    global dimension_of_images
    global mainl
    mm=mlm[len(mlm)-1]
    if len(mlm)-2>=0:
        mm=mlm[len(mlm)-2]
    # mm=[[8, 2, 6],
    #            [1, 4, 3],
    #            [7, 5, 0]]
    
    doneSwap=[]
    for a in range(len(array)):
        for b in range(len(array)):
            # print("doneswap loop",doneSwap)
            if array[a][b]!=mm[a][b] and ((mm[a][b],array[a][b]) not in doneSwap):
                l=(a,b)
                doneSwap.append(l)
   
    if len(doneSwap)>0:
        a,b=doneSwap[0][0],doneSwap[0][1]
        x,y=doneSwap[1][0],doneSwap[1][1]
        temp1=dimension_of_images[mainl[a][b]]
        dimension_of_images[mainl[a][b]]=dimension_of_images[mainl[x][y]]
        dimension_of_images[mainl[x][y]]=temp1

        temp1=mainl[a][b]
        mainl[a][b]=mainl[x][y]
        mainl[x][y]=temp1

        # window.blit(mainl[a][b],(10,80)) 
        # window.blit(mainl[b][a],(150,80)) 
    #1,2   2,2
        # print(dimension_of_images[mainl[a][b]])

        pygame.display.update()
        time.sleep(0.3)            

        

#puzzle print function
def print_puzzle(array):
    # print(first_line)
    global listOfPastARrryas
    listOfPastARrryas.append(array)
    # print("before",imageList)
    updateList(array,listOfPastARrryas)
    # print(imageList)

   

    # pygame.draw.rect(window,(0,0,0),[0.4,150,400,398])
    for a in range(len(array)):
        for i in range(len(array)):
            # print(i)
            
            img=mainl[a][i]
            # print()
            window.blit(img,(dimension_of_images[img])) 
            # print(dimension_of_images[img])
            pygame.display.update()
            # time.sleep(2)
           

            # dimension_of_images[img]=(j*imageWidth+1+tempx,i*imageHeight+temp)
            # position_of_images[img]=k
            # k+=1

#it is the node which store each state of puzzle
class Node:
    def __init__(self, current_node, previous_node, g, h, dir):
        self.current_node = current_node
        self.previous_node = previous_node
        self.g = g
        self.h = h
        self.dir = dir

    def f(self):
        return self.g + self.h


def get_pos(current_state, element):
    for row in range(len(current_state)):
        if element in current_state[row]:
            return (row, current_state[row].index(element))

#it is a distance calculation algo
def euclidianCost(current_state):
    cost = 0
    for row in range(len(current_state)):
        for col in range(len(current_state[0])):
            pos = get_pos(END, current_state[row][col])
            cost += abs(row - pos[0]) + abs(col - pos[1])
    return cost

#get adjucent Nodes
def getAdjNode(node):
    listNode = []
    emptyPos = get_pos(node.current_node, 0)

    for dir in DIRECTIONS.keys():
        newPos = (emptyPos[0] + DIRECTIONS[dir][0], emptyPos[1] + DIRECTIONS[dir][1])
        if 0 <= newPos[0] < len(node.current_node) and 0 <= newPos[1] < len(node.current_node[0]):
            newState = deepcopy(node.current_node)
            newState[emptyPos[0]][emptyPos[1]] = node.current_node[newPos[0]][newPos[1]]
            newState[newPos[0]][newPos[1]] = 0
            # listNode += [Node(newState, node.current_node, node.g + 1, euclidianCost(newState), dir)]
            listNode.append(Node(newState, node.current_node, node.g + 1, euclidianCost(newState), dir))

    return listNode

#get the best node available among nodes
def getBestNode(openSet):
    firstIter = True

    for node in openSet.values():
        if firstIter or node.f() < bestF:
            firstIter = False
            bestNode = node
            bestF = bestNode.f()
    return bestNode

#this functionn create the smallest path
def buildPath(closedSet):
    node = closedSet[str(END)]
    branch = list()

    while node.dir:
        branch.append({
            'dir': node.dir,
            'node': node.current_node
        })
        node = closedSet[str(node.previous_node)]
    branch.append({
        'dir': '',
        'node': node.current_node
    })
    branch.reverse()

    return branch

#main function of node
def main(puzzle):
    open_set = {str(puzzle): Node(puzzle, puzzle, 0, euclidianCost(puzzle), "")}
    closed_set = {}

    while True:
        test_node = getBestNode(open_set)
        closed_set[str(test_node.current_node)] = test_node

        if test_node.current_node == END:
            return buildPath(closed_set)

        adj_node = getAdjNode(test_node)
        for node in adj_node:
            if str(node.current_node) in closed_set.keys() or str(node.current_node) in open_set.keys() and open_set[
                str(node.current_node)].f() < node.f():
                continue
            open_set[str(node.current_node)] = node

        del open_set[str(test_node.current_node)]


def start(mail,dime,wind,List):
    #it is start matrix
    global mainl
    mainl=mail
    global dimension_of_images
    dimension_of_images=dime
    global window
    window=wind
    
    global imageList
    imageList=List
    # print(mainl)
    br = main([[8, 2, 6],
               [1, 4, 3],
               [7, 5, 0]])
    

    print('total steps : ', len(br) - 1)
    # print()
    # print(dash + dash + right_junction, "INPUT", left_junction + dash + dash)
    for b in br:
        if b['dir'] != '':
            letter = ''
            if b['dir'] == 'U':
                letter = 'UP'
            elif b['dir'] == 'R':
                letter = "RIGHT"
            elif b['dir'] == 'L':
                letter = 'LEFT'
            elif b['dir'] == 'D':
                letter = 'DOWN'
            # print(dash + dash + right_junction, letter, left_junction + dash + dash)
        print_puzzle(b['node'])
        # print()

    # print(dash + dash + right_junction, 'ABOVE IS THE OUTPUT', left_junction + dash + dash)
