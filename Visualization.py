#Imports
import pygame
from random import randint as rn
#Constants
ScreenWidth = 1920
ScreenHeight = 1080
GAP = 2
SCREEN = pygame.display.set_mode((ScreenWidth,ScreenHeight))
CLOCK = pygame.time.Clock()
LINES = []
Search = True
#Classes
class line:
    def __init__(self,x,y) -> None:
        self.x = x
        self.height = y
        self.color = 'white'

    def Draw(self):
        start_pos = pygame.Vector2(self.x,ScreenHeight)
        end_pos = pygame.Vector2(self.x,self.height)
        pygame.draw.line(SCREEN,self.color,start_pos,end_pos)
#Functions
def FindLine(x):
    for line in LINES:
        if line.x == x:
            return line
    raise Exception(f"Could not find line with x:{x}")
def DrawLines():
    for line in LINES:
        line.Draw()
def SearchLine(idx):
    global Search
    line = FindLine(idx)
    if line.color != 'purple': line.color = 'blue'
    else: 
        line.color = 'red'
        Search = False
def mainloop():
    global LINES,Search
    RUNNING = True
    LINES = [line(x,rn(1,ScreenHeight)) for x in range(1,ScreenWidth,GAP)]
    SpecialLine = LINES[rn(1,len(LINES) - 1)]
    SpecialLine.color = "purple"
    idx = 1 - GAP
    Search = True
    while RUNNING:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
        SCREEN.fill('black')

        idx += GAP
        if Search:SearchLine(idx)
        DrawLines()

        pygame.display.flip()
        CLOCK.tick(60)
def Run():
    pygame.init()
    mainloop()
    pygame.quit()
#main
Run()