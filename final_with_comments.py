import pygame
import time
import random

pygame.init()

display_width = 800        # it's the console width, using variable let use modify or access that futher in the programme easily
display_height =600        # it's the console height

black = (0,0,0)            # we are defining color here
white = (255,255,255)
red = (255,0,0)

random_color = (45,34,134)

car_width = 73

gameDisplay = pygame.display.set_mode((display_width,display_height))   
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

carImg = pygame.image.load('F:\car_2nd.png')     # we have loaded our image by this code

# dodged score function
def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text, (0,0))

def things(thingx, thingy, thingw, thingh, color):    # things is here box
    # thingx and thingy is x and y coordinate of block
    # thingw and thingh are height and width of block
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

    # finally this function draw the block to our screen


def car(x,y):    # to display the image on the console
    gameDisplay.blit(carImg,(x,y))    # we are displaying our car image at postion (x,y) 

def text_objects(text,font):
    textSurface = font.render(text, True, red)    # to create the surface for the text 
    return textSurface, textSurface.get_rect()     # .get_rect() it rectangles our text 

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',100)     # parameter are (font_type) and (font_size)
    TextSurf, TextRect = text_objects(text, largeText)    # calling text_objects function
    TextRect.center = ((display_width/2),(display_height/2))     # to center the text on screen
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)    # wait for 2 second

    game_loop()      # if crashed start the game_loop further

def crash():    
    message_display('You Crashed')
     
def game_loop():      # This is our main game loop
    x = (display_width * 0.45)          # these two line defines car location 
    y = (display_height * 0.8)

    x_change = 0
  
    thing_startx = random.randrange(0, display_width)    # randomly selects the x coordinate b/w (0 and 800) of block
    thing_starty = -600    # we will start the block from 600 pixels of the sreen
    thing_speed = 4        # 
    thing_width = 100     # block is (100 by 100) width and height
    thing_height = 100
    
    dodged = 0
    
    gameExit = False            # change the crashed to gameExit

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:    # if user want to quit, this code runs
                pygame.quit()      # this quits the game
                quit()

            if event.type == pygame.KEYDOWN:      # KEYDOWN here means we are pressing the keys
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:        # KEYUP means when we stop pressing the key i.e. 
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
            

                
        x += x_change            
        gameDisplay.fill(white)     # it fills the console to white from black(default)

        # things(thingx, thingy, thingw, thingh, color)
        things(thing_startx, thing_starty, thing_width, thing_height, random_color)
        thing_starty += thing_speed        # we are changing the y coordinate by 4(thing_speed) every time
        car(x,y)  # calling car function that draws car image
        things_dodged(dodged)
        
        if x > display_width - car_width or x < 0:    # code for boundry of the game
            # before it was gameExit = True but now crash function is called so if we crash game not exit
            crash( )

        if thing_starty > display_height:   # if block is of the screen it will come back again with this code
            thing_starty = 0-thing_height   # everytime changing the y coordinate to -100(means 100 pixels above the screen se block aaega)
            thing_startx = random.randrange(0,display_width)
            dodged += 1
            # speed increases by 1 by every dodged
            thing_speed +=1

        # box crash code with car
        if y < thing_starty + thing_height:
            print()

            if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx + thing_width:
                crash()

        
        pygame.display.update()     # or pygame.display.flip()
        clock.tick(60)

game_loop()
pygame.quit()
quit()

