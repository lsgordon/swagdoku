"""

Plan:

sudoku generator

Step 1), generate 9x9 sudoku board with algorithm from https://www.geeksforgeeks.org/program-sudoku-generator/
build top-left,middle,bottom right 3x3 sqaures
Step 2) solve sudoku
Step 3) verify





Time Spent:
12:00-12:57
Working on understand what my algorithms need, planning just ASCII representation
Built random list generator
Almost built base board
1:50-2:30
Finished intial generator:
working on step 2
writing plan
11/27/22 2:00-2:30
Changing tactics and instead using a different way of doing step 1:
shuffle board so that it is solvable but different each time
this strat no work
11/28/22 10:00-11:15
Implementing the shuffle algorithm, testing, tweaking
11/29 or 30
Spent like 30-60 on graphics
12/1/22
12:30-1:00
Worked more on graphics, infrastructure for shuffling the board, and Querying for difficulty
Need to work on the sudoku cell class, and do all of the maths,
Build a board solver
8:00-9:00
More GUI garb
12/2/22
3:00-3:30
candidate_map_builder(),
    incell -> remove from individual cell
    inrow 
    incoll
Complex Solving Functions ()
Buiding a board solver

    Starting with the 3 BNSF incell, inrow, incoll simplified to 1(cand)
    Building off those three methods to make everything else
12/4/22
created sudokuboard.py
12/8-9
11:00-1:00
Worked on making a working sudoku_candidate_map function, made it all the way to the part where I have to implement for big cells, and then promptly gave up, since I have to go to bed because of a track meet in the morning
This project is so much work and simultaneously the most fun programming challenge I have ever embarked on
12/14/22 9:00-12:00, 
Finished my last exam
It is time to code

Did a lot of scaling back/scrapping since the code was getting really messy really fast, (1 million steps to calculate the board) so every board is the same level of difficulty
Solver algorithm is greatly scaled back
So is colors
And solving algorithms
1:50-4:00 (12/15/22)

HIT MINIMUM VIABLE PROJECT!@!!!!!!

Implemented a graphics interface
WASD key control
Writing into memory

EVERYTHING ELSE IS ARBITRARY AND DO NOT FEEL RESPONSIBLE FOR THE TIME I SPENT ON THIS PART...

Made a Help tool
Difficulty levels
Candidates in the grid as well
Recorded the video

"""



import numpy as np
import random
import sudokuboard
arr = np.array([[8,2,7,1,5,4,3,9,6]
,[9,6,5,3,2,7,1,4,8]
,[3,4,1,6,8,9,7,5,2]
,[5,9,3,4,6,8,2,7,1]
,[4,7,2,5,1,3,6,8,9]
,[6,1,8,9,7,2,4,3,5]
,[7,8,6,2,3,5,9,1,4]
,[1,5,4,7,9,6,8,2,3]
,[2,3,9,8,4,1,5,6,7]])

def selectrand(arr): #this really makes a difference just trust
    for i in range(1,len(arr)**2):
        a = random.randint(1,len(arr))
        b = random.randint(1,len(arr))
        a,b=b,a
    return(arr)
class cell():
    candidates = []
    def __init__(self,rep) -> None: #value = rep
        self.rep = rep
def boardshuffle(arr): #shuffles the board
    for i in range(1,100):
        for i in range(0,2):
            for j in range(1,random.randint(1,3)):
                arr[[0+(i*3),1+(i*3)]] = arr[[1+(i*3),0+(i*3)]]
                arr[[1+(i*3),2+(i*3)]] = arr[[2+(i*3),1+(i*3)]]
            for j in range(1,random.randint(1,3)):
                arr[[2+(i*3),0+(i*3)]] = arr[[0+(i*3),2+(i*3)]]
                arr[[2+(i*3),1+(i*3)]] = arr[[1+(i*3),2+(i*3)]]
        for i in range(0,2): #shuffle cols
            for j in range(1,random.randint(1,3)):
                arr[:,[0+(i*3),1+(i*3)]] = arr[:,[1+(i*3),0+(i*3)]]
                arr[:,[1+(i*3),2+(i*3)]] = arr[:,[2+(i*3),1+(i*3)]]
            for j in range(1,random.randint(1,3)):
                arr[:,[2+(i*3),0+(i*3)]] = arr[:,[0+(i*3),2+(i*3)]]
                arr[:,[2+(i*3),1+(i*3)]] = arr[:,[1+(i*3),2+(i*3)]]
        #shuffle big rows
        a = arr[[0]] 
        a= np.concatenate((a,arr[[1]]))
        a= np.concatenate((a,arr[[2]]))
        b = arr[[3]] 
        b= np.concatenate((b,arr[[4]]))
        b= np.concatenate((b,arr[[5]]))
        c = arr[[6]]
        c = np.concatenate((c,arr[[7]]))
        c = np.concatenate((c,arr[[8]]))
        randy = selectrand([a,b,c])
        a = randy[0]
        b = randy[1]
        c = randy[2]
        a = np.concatenate((a,b))
        a = np.concatenate((a,c))
        #shuffle big cols
        a = arr[:,[0]] 
        a= np.concatenate((a,arr[:,[1]]),1)
        a= np.concatenate((a,arr[:,[2]]),1)
        b = arr[:,[3]] 
        b= np.concatenate((b,arr[:,[4]]),1)
        b= np.concatenate((b,arr[:,[5]]),1)
        c = arr[:,[6]]
        c = np.concatenate((c,arr[:,[7]]),1)
        c = np.concatenate((c,arr[:,[8]]),1)
        randy = selectrand([a,b,c])
        a = randy[0]
        b = randy[1]
        c = randy[2]
        a = np.concatenate((a,b),1)
        a = np.concatenate((a,c),1)
        for j in range(1,random.randint(1,4)):
            arr=np.rot90(arr)
    for i in arr:
        i = cell(i)
    return(arr)

# import the pygame module, so you can use it
import pygame
# define a main function
def main():
    # initialize the pygame module
    pygame.init()
    #background
    background_colour = (255,255,255)
    # load and set the logo
    logo = pygame.image.load("sudokuicon.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Swagdoku")
    
    # create a surface on screen that has the size of 1000 x 800
    screen = pygame.display.set_mode((1000,800))
    screen.fill(background_colour)
    # define a variable to control the main loop
    running = True
    diff = 0
    flagg = 0
    xpos = 0
    ypos = 0
    helpmenuflag = 0
    helpmenuframes = 0
    frame_counter_up = 0
    frame_counter_down = 0
    frame_counter_left = 0
    frame_counter_right = 0
    BLACK = (0, 0, 0) 
    WHITE = (255, 255, 255)
    BLUE =  (225,225,255)
    RED = (255,0,0) #color values





    # main loop, just graphics
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.draw.rect(screen, WHITE, pygame.Rect((0, 0), (1000, 1000)))
        mouse = pygame.mouse.get_pos() 
        myfont = pygame.font.SysFont("arial", 23)
        #PUT RENDERING BELOW TO THIS
        if flagg == 1: #flagg is used for rendering alternative things to the sprite other than the header and sidebar
            pygame.draw.rect(screen, WHITE, pygame.Rect((0, 0), (1000, 1000)))
            label = myfont.render("What difficulty do you want?", 1, BLACK)
            screen.blit(label, (300,300))
            label = myfont.render("Easy", 1, BLACK)
            screen.blit(label, (350,350))
            label = myfont.render("Medium", 1, BLACK)
            screen.blit(label, (450,350))
            label = myfont.render("Hard", 1, BLACK)
            screen.blit(label, (350,400))
            label = myfont.render("Impossible",1, RED)
            screen.blit(label, (450,400))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 350 <= mouse[0] <= 410 and 350 <= mouse[1] <= 384: #normal
                    flagg = 2
                    diff=1
                if 440 <= mouse[0] <= 540 and 350 <= mouse[1] <= 384: #normal
                    flagg = 2
                    diff=2
                if 350 <= mouse[0] <= 410 and 400 <= mouse[1] <= 444: #normal
                    flagg = 2
                    diff=3
                if 410 <= mouse[0] <= 600 and 400 <= mouse[1] <= 444: #normal
                    flagg = 2
                    diff=4

        if flagg == 2: #this is for when undoing the last screen step, means to rerender white box
            pygame.draw.rect(screen, WHITE, pygame.Rect((300, 300), (420, 385)))
            boardshuffle(arr)
            for i in range(0,8):
                for j in range(0,8):
                    arr[i,j] = int(arr[i,j])
            s = sudokuboard.sudokuboard(arr,diff) #sudokuboarding
            s.reduce()
            flagg = 3 #state is now sudoku board
        if flagg == 3:
            keys = pygame.key.get_pressed()
            #arrow key movement // every x frames change x pos
            if keys[pygame.K_UP]:
                frame_counter_up = frame_counter_up + 1
            if keys[pygame.K_DOWN]:
                frame_counter_down = frame_counter_down + 1
            if keys[pygame.K_LEFT]:
                frame_counter_left = frame_counter_left + 1
            if keys[pygame.K_RIGHT]:
                frame_counter_right = frame_counter_right + 1
            #sensitivity of the algorithm
            speed = 8
            if frame_counter_right >= speed:
                frame_counter_left = 0
                frame_counter_right = 0
                frame_counter_up = 0
                frame_counter_down = 0
                if xpos < 8:
                    xpos = xpos + 1
            if frame_counter_left >= speed:
                frame_counter_left = 0
                frame_counter_right = 0
                frame_counter_up = 0
                frame_counter_down = 0
                if xpos > 0:
                    xpos = xpos - 1
            if frame_counter_down >= speed:
                frame_counter_left = 0
                frame_counter_right = 0
                frame_counter_up = 0
                frame_counter_down = 0
                if ypos < 8:
                    ypos = ypos + 1
            if frame_counter_up >= speed:
                frame_counter_left = 0
                frame_counter_right = 0
                frame_counter_up = 0
                frame_counter_down = 0
                if ypos > 0:
                    ypos = ypos - 1
            #there was no easy alternative to this I could find so instead enjoy the utter nonsense remaining
            if keys[pygame.K_1]:
                s.rep[xpos,ypos].rep = 1
            if keys[pygame.K_2]:
                s.rep[xpos,ypos].rep = 2
            if keys[pygame.K_3]:
                s.rep[xpos,ypos].rep = 3
            if keys[pygame.K_4]:
                s.rep[xpos,ypos].rep = 4
            if keys[pygame.K_5]:
                s.rep[xpos,ypos].rep = 5
            if keys[pygame.K_6]:
                s.rep[xpos,ypos].rep = 6
            if keys[pygame.K_7]:
                s.rep[xpos,ypos].rep = 7
            if keys[pygame.K_8]:
                s.rep[xpos,ypos].rep = 8
            if keys[pygame.K_9]:
                s.rep[xpos,ypos].rep = 9
            if keys[pygame.K_BACKSPACE]:
                s.rep[xpos,ypos].rep = None
            #big lines
            pygame.draw.rect(screen, BLACK, pygame.Rect((395, 20), (10, 720)))
            pygame.draw.rect(screen, BLACK, pygame.Rect((635, 20), (10, 720)))
            pygame.draw.rect(screen, BLACK, pygame.Rect((160, 255), (720, 10)))
            pygame.draw.rect(screen, BLACK, pygame.Rect((160, 495), (720, 10)))
            for i in range(0,10): #board setup
                pygame.draw.line(screen,BLACK, (160+(i*80), 20), (160+(i*80), 740))
                pygame.draw.line(screen,BLACK,(160,100+(i*80)),(880,100+(i*80)))
            pygame.draw.rect(screen, BLUE, pygame.Rect((165+(xpos*80), 25+(ypos*80)), (70, 70)))
            for i in range(0,9): #numbers on board
                for j in range(0,9):
                    p = (s.rep[i,j].rep)
                    p = str(p)
                    if p == "None":
                        p = " "
                    myfont2 = pygame.font.SysFont("arial", 40) #second font for the cells since they have to be bigger
                    label = myfont2.render(p, 1, BLACK)
                    screen.blit(label, ((80*i)+190,(j*80)+40))
            endflag = 0
            for i in range(0,9): #checking if any cells are still empty, if the puzzle is over
                for j in range(0,9):
                    p = (s.rep[i,j].rep)
                    if s.rep[i,j].rep == None:
                        endflag = 1
            if endflag == 0:
                flagg = 5
        if flagg == 5:
            pygame.draw.rect(screen, WHITE, pygame.Rect((0, 0), (1000, 1000)))
            label = myfont2.render("Congrats! You did it!", 1, BLACK)
            screen.blit(label,(500,500))
        if helpmenuflag == 1:
            print("Press the arrow keys to move around. Your position is denoted by the light blue square. For more help, refer to the README.TXT file.")
            helpmenuflag = 2
        if helpmenuflag == 2:
            helpmenuframes =+ 1
            label = myfont.render("check your terminal!", 1, BLACK)
            screen.blit(label,(0,700))
            if helpmenuframes >= 30:
                helpmenuflag = 0
        label = myfont.render("Swagdoku", 1, BLACK)
        screen.blit(label, (30, 0))
        label = myfont.render("New Game", 1, BLACK)
        screen.blit(label, (0, 350))
        label = myfont.render("Exit", 1, BLACK)
        screen.blit(label, (0, 400))
        label = myfont.render("Help",1,BLACK)
        screen.blit(label, (0,450))
        if event.type == pygame.MOUSEBUTTONDOWN:
            #Exit game button
            if 0 <= mouse[0] <= 113 and 405 <= mouse[1] <= 425:
                pygame.quit()
            if 0 <= mouse[0] <= 113 and 345 <= mouse[1] <= 380:
                flagg = 1
            if 0 <= mouse[0] <= 113 and 445 <= mouse[1] <= 490:
                helpmenuflag = 1
        print(mouse[0],mouse[1])#debug func
        pygame.display.update() #don't put anything after this



        
    
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
    

