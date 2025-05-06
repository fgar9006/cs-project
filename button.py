import pygame
pygame.init()

class Button:
    def __init__(self, text, pos,size):
        self.text=text
        self.position=pos
        self.size=size
        self.button=pygame.rect.Rect((self.position[0],self.position[1]),(self.size[0],self.size[1]))

    def drawbtn(self,surf):#blits button onto screen with text centred on it
        pygame.draw.rect(surf,'grey',self.button,0,5)
        textsurf=font.render(self.text,True,'black')
        textlen=textsurf.get_width()
        surf.blit(textsurf,(self.position[0]+int(self.size[0]/2)-int(textlen/2),self.position[1]+10))

    def check_click(self):
        if self.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return True #returns True if clicked
        else:
            return False

class hover_equ(Button):
    def __init__(self,text,pos,size):
        Button.__init__(self,text,pos,size)
        self.rect=pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.hover = False#if its being hovered over or not

    def show_equ(self, display):
        if self.hover:#if the mouse is on the button
            mouse_pos = pygame.mouse.get_pos()
            #display the equations above the mouse
            display.blit(eqs, (mouse_pos[0]-20, mouse_pos[1]-150))

    def hover_check(self, mpos):
        #checks position of mouse and if its clicked
        #updates hover attibute to True when mouse is on button
        self.hover = self.rect.collidepoint(mpos)
    

font=pygame.font.Font('freesansbold.ttf',22)
screen=pygame.display.set_mode([900,800])

eqs=pygame.image.load("project/equations.png")
eqs=pygame.transform.scale(eqs,(120,120))
eqs=eqs.convert_alpha()

#font = pygame.font.SysFont('arial',23) 
#try change drawbtn to take in a surface to draw the btn.... 
# impr:
#def drawbtn(self,surf):
    #pygame.draw.rect(surf,'grey',self.button,0,5)
    #text=font.render(self.text,True,'black')
    #surf.blit(text,(self.position[0]+(self.size[0]/3.5),self.position[1]+7))

#def drawbtn(self): BEFORE
    #pygame.draw.rect(screen,'grey',self.button,0,5)
    #text=font.render(self.text,True,'black')
    #screen.blit(text,(self.position[0]+(self.size[0]/3.5),self.position[1]+7))
