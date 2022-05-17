from copy import deepcopy
import pygame
import time

DIRECTIONS = {"U": [-1, 0], "D": [1, 0], "L": [0, -1], "R": [0, 1]}

END = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

desired_Position_Of_imageList=[]
imageList=[]
dimension_of_images=[]
window=None
mainl=[]

ListUpd=imageList  

listOfPastARrryas=[]
def updateList(array,mlm):
    global dimension_of_images
    global mainl
    mm=mlm[len(mlm)-1]
    if len(mlm)-2>=0:
        mm=mlm[len(mlm)-2]
 
    doneSwap=[]
    for a in range(len(array)):
        for b in range(len(array)):
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
        pygame.display.update()
        time.sleep(0.3)            

        

def printPuzzle(array):
   
    global listOfPastARrryas
    listOfPastARrryas.append(array)
    updateList(array,listOfPastARrryas)
  
    for a in range(len(array)):
        for i in range(len(array)):
           
            
            img=mainl[a][i]
         
            window.blit(img,(dimension_of_images[img])) 
            # print(dimension_of_images[img])
            pygame.display.update()
            # time.sleep(2)
           

           
class Node:
    def __init__(self, currentNode, previousNode, g, h, dir):
        self.currentNode = currentNode
        self.previousNode = previousNode
        self.g = g
        self.h = h
        self.dir = dir

    def f(self):
        return self.g + self.h


def get_pos(currentState, element):
    for row in range(len(currentState)):
        if element in currentState[row]:
            return (row, currentState[row].index(element))


def euclidianDist(currentState):
    cost = 0
    for row in range(len(currentState)):
        for col in range(len(currentState[0])):
            pos = get_pos(END, currentState[row][col])
            cost += abs(row - pos[0]) + abs(col - pos[1])
    return cost


def getAdjNode(node):
    listNode = []
    emptyPos = get_pos(node.currentNode, 0)

    for dir in DIRECTIONS.keys():
        newPos = (emptyPos[0] + DIRECTIONS[dir][0], emptyPos[1] + DIRECTIONS[dir][1])
        if 0 <= newPos[0] < len(node.currentNode) and 0 <= newPos[1] < len(node.currentNode[0]):
            newState = deepcopy(node.currentNode)
            newState[emptyPos[0]][emptyPos[1]] = node.currentNode[newPos[0]][newPos[1]]
            newState[newPos[0]][newPos[1]] = 0
            listNode.append(Node(newState, node.currentNode, node.g + 1, euclidianDist(newState), dir))

    return listNode

def getBestNode(openSet):
    firstIter = True

    for node in openSet.values():
        if firstIter or node.f() < bestF:
            firstIter = False
            bestNode = node
            bestF = bestNode.f()
    return bestNode


def SmallestPath(closedSet):
    node = closedSet[str(END)]
    branch = list()

    while node.dir:
        branch.append({
            'dir': node.dir,
            'node': node.currentNode
        })
        node = closedSet[str(node.previousNode)]
    branch.append({
        'dir': '',
        'node': node.currentNode
    })
    branch.reverse()

    return branch

def main(puzzle):
    open_set = {str(puzzle): Node(puzzle, puzzle, 0, euclidianDist(puzzle), "")}
    closed_set = {}

    while True:
        test_node = getBestNode(open_set)
        closed_set[str(test_node.currentNode)] = test_node

        if test_node.currentNode == END:
            return SmallestPath(closed_set)

        adj_node = getAdjNode(test_node)
        for node in adj_node:
            if str(node.currentNode) in closed_set.keys() or str(node.currentNode) in open_set.keys() and open_set[
                str(node.currentNode)].f() < node.f():
                continue
            open_set[str(node.currentNode)] = node

        del open_set[str(test_node.currentNode)]


def start(mail,dime,wind,List):
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
        printPuzzle(b['node'])
    