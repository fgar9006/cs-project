import pygame,sys
from button import Button
pygame.init()
        
class dropmenu():#creates a class for mode menu
    def __init__(self, colour_menu, colour_opt, x, y, w, h, font, main, options):
        self.colour_menu = colour_menu
        self.colour_opt = colour_opt
        self.rect = pygame.Rect(x, y, w, h)#sets the coordinates and size of menu
        self.font = font
        self.main = main#displayed current text of menu
        self.options = options#sets the options in the menu
        #starts off inactive as nothing is pressed yet
        self.draw_menu = False
        self.menu_active = False
        self.sel_opt = -1 #tells you which option is selected

    def draw(self, surf):#draws the menu on a surface
        pygame.draw.rect(surf, self.colour_menu[self.menu_active], self.rect, 0,5)
        #if the menu is active, the active colour is used and vice versa
        msg = self.font.render(self.main, True, 'black')#adds text to main button
        surf.blit(msg, msg.get_rect(center = self.rect.center))#blits text to the center of rectangle

        if self.draw_menu:#if options are shown
            for i, text in enumerate(self.options):#options listed with a number (0,S),(1,U) etc.
                rect = self.rect.copy() #each option uses the same x,y,w,h
                rect.y += (i+1) * self.rect.height #changes y to draw rects beneath each other
                pygame.draw.rect(surf, self.colour_opt[1 if i == self.sel_opt else 0], rect, 0,2)
                #two colour options are given. It highlights the option/rect its hovering over
                msg = self.font.render(text, True, 'black')
                surf.blit(msg, msg.get_rect(center = rect.center))#blits text to center

    def update(self, events):#checks events
        #if the mouse is on the menu, menu is active
        mousepos = pygame.mouse.get_pos()
        self.menu_active = self.rect.collidepoint(mousepos)
        #none of the options have been selected yet
        self.sel_opt = -1
        for i in range(len(self.options)): #0 to how many options there are
            rect = self.rect.copy() #uses the same x,y,w,h
            rect.y += (i+1) * self.rect.height #changes y to draw rects beneath each other
            if rect.collidepoint(mousepos): #if one of the options are pressed
                self.sel_opt = i #set the active option to the one that was pressed
                break

        #if menu is inactive and no option has been selected
        if not self.menu_active and self.sel_opt == -1:
            self.draw_menu = False #do not blit the options

        for event in events:#checks events
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.menu_active:#display options if clicked
                    self.draw_menu = not self.draw_menu
                elif self.draw_menu and self.sel_opt >= 0:
                    self.draw_menu = False #hide options if an option is selected
                    return self.sel_opt #returns selected option
        return -1 #if no option is selected

#functions for screens
def draw_home():
    font=pygame.font.SysFont('arialblack',30)
    tfont=pygame.font.SysFont('arialblack',23)
    screen.fill('white')
    text=font.render(f'Welcome to                         !',True,'black')
    name=font.render(f'solving.SUVAT',True,'#0044cc')
    screen.blit(text,(200,240))
    screen.blit(name,(400,240))
    command=0

    #adds a cloud to the screen
    cloud1=pygame.image.load("project/cloud.png")
    cloud1=pygame.transform.scale(cloud1,(200,100))
    cloud1=cloud1.convert_alpha()
    cloud2=pygame.image.load("project/cloud.png")
    cloud2=pygame.transform.scale(cloud2,(250,120))
    cloud2=cloud2.convert_alpha()
    cloud3=pygame.image.load("project/cloud.png")
    cloud3=pygame.transform.scale(cloud3,(170,90))
    cloud3=cloud3.convert_alpha()
    screen.blit(cloud1,(600,40))
    screen.blit(cloud2,(30,20))
    screen.blit(cloud3,(350,70))

    #creates a ground on the screen
    ground=pygame.image.load("project/ground.png")
    ground=pygame.transform.scale(ground,(900,50))
    ground=ground.convert_alpha()
    screen.blit(ground,(0,750))
    
    #draws buttons on screen
    #logsign_btn=Button('Login/Sign up',(300,400),(260,40))
    #logsign_btn.drawbtn(screen)
    start_btn=Button('Start!',(300,350),(260,40))
    start_btn.drawbtn(screen)

    mode.draw(screen)
    logsign.draw(screen)

    #checks if login or signup was selected 
    selected_opt = logsign.update(events)
    if selected_opt == 0:#if login is selected
        #changes the current displayed option on the menu to the selected one
        #logsign.main = logsign.options[selected_opt]
        command=1#should blit to login screen
    elif selected_opt == 1:#if sign up is selected
        command=3#should blit to sign up screen

    if start_btn.check_click() and mode.main!='Select Mode':
        command=2#show info screen then main gameplay
    elif start_btn.check_click():
        command=5#reminder to select a mode
    return command

def loggedin(lirun):#run when logged in
   font = pygame.font.SysFont('arial',20) 
   while lirun:
      screen.fill('white')

      #adds a cloud to the screen
      cloud1=pygame.image.load("project/cloud.png")
      cloud1=pygame.transform.scale(cloud1,(200,100))
      cloud1=cloud1.convert_alpha()
      cloud2=pygame.image.load("project/cloud.png")
      cloud2=pygame.transform.scale(cloud2,(230,110))
      cloud2=cloud2.convert_alpha()
      cloud3=pygame.image.load("project/cloud.png")
      cloud3=pygame.transform.scale(cloud3,(170,90))
      cloud3=cloud3.convert_alpha()
      screen.blit(cloud1,(600,20))
      screen.blit(cloud2,(350,70))
      screen.blit(cloud3,(150,50))

      #creates a ground on the screen
      ground=pygame.image.load("project/ground.png")
      ground=pygame.transform.scale(ground,(900,50))
      ground=ground.convert_alpha()
      screen.blit(ground,(0,750))

      txtsurf=font.render(f'Logged in! Return to main menu by pressing the Back button!',True,'black')
      screen.blit(txtsurf,(190,300))

      backbtn=Button("Back",(50,50),(100,40))
      backbtn.drawbtn(screen)

      for events in pygame.event.get():
         if events.type==pygame.QUIT: #lets user exit the window
            pygame.quit()
            sys.exit()
         if events.type==pygame.MOUSEBUTTONDOWN:
            if backbtn.check_click()==True:#returns to main menu
               lirun=False
               return True#so then home=True, draws home
               
      pygame.display.flip()

def logscreen(lsrun):#run when user wants to log in
   from db_alg import login
   #setting up variables
   clock = pygame.time.Clock() 
   tfont=pygame.font.SysFont('arial',30)
   usn= ''
   pasw=''
   us_rect = pygame.Rect(380,300,600,30)#(x,y,width,height)
   pas_rect = pygame.Rect(380,350,600,30)#(x,y,width,height)
   color_active=pygame.Color('blue')
   color_inactive=pygame.Color('black')
   color=color_inactive #initially the box is inactive so it starts black
   uactive=False
   pactive=False
   font = pygame.font.SysFont('arial',20) 

   while lsrun:
      for events in pygame.event.get():
         if events.type==pygame.QUIT: #lets user exit the window
            pygame.quit()
            sys.exit()
         
         if events.type==pygame.MOUSEBUTTONDOWN:
            if us_rect.collidepoint(events.pos):
               uactive = True #if the box is pressed, it becomes active/blue
               pactive=False
            elif pas_rect.collidepoint(events.pos):
               pactive=True
               uactive=False
            else:
               uactive=False#if the user click outside the box, it deactivates
               pactive=False
            if backbtn.check_click()==True:
                return False,'',0

         if events.type == pygame.KEYDOWN and uactive==True:
            if events.key==pygame.K_RETURN:#enter is pressed when the user wants to stop typing
               uactive=False#also deactivates when enter is pressed
               print(usn)
            elif events.key == pygame.K_BACKSPACE:
               usn = usn[:-1] #removes the last letter
            else:
               usn+=events.unicode #adds letter to screen
            
         if events.type == pygame.KEYDOWN and pactive==True:
            if events.key==pygame.K_RETURN:#enter is pressed when the user wants to stop typing
               pactive=False#also deactivates when enter is pressed
               print(pasw)
            elif events.key == pygame.K_BACKSPACE:
               pasw = pasw[:-1] #removes the last letter
            else:
               pasw+=events.unicode #adds letter to screen
   
          
      screen.fill('white')
      #adds a cloud to the screen
      cloud1=pygame.image.load("project/cloud.png")
      cloud1=pygame.transform.scale(cloud1,(200,100))
      cloud1=cloud1.convert_alpha()
      cloud2=pygame.image.load("project/cloud.png")
      cloud2=pygame.transform.scale(cloud2,(230,110))
      cloud2=cloud2.convert_alpha()
      cloud3=pygame.image.load("project/cloud.png")
      cloud3=pygame.transform.scale(cloud3,(170,90))
      cloud3=cloud3.convert_alpha()
      screen.blit(cloud1,(600,20))
      screen.blit(cloud2,(350,70))
      screen.blit(cloud3,(150,50))

      #creates a ground on the screen
      ground=pygame.image.load("project/ground.png")
      ground=pygame.transform.scale(ground,(900,50))
      ground=ground.convert_alpha()
      screen.blit(ground,(0,750))

      if uactive==True or pactive==True:#can remove this later. it just shows if the text box is active or not
         color=color_active
      else:
         color=color_inactive
      
      #displays on screen,with colour,with rectangle and outline of width 2
      pygame.draw.rect(screen,color,us_rect,2)
      us=font.render(f'Username:',True,'black')
      screen.blit(us,(280,302)) #displays a title

      pygame.draw.rect(screen,color,pas_rect,2)
      pst=font.render(f'Password:',True,'black')
      screen.blit(pst,(280,352))
   
      entbtn=Button("Enter",(340,450),(180,40))
      entbtn.drawbtn(screen)

      if entbtn.check_click()==True and (usn=='' or pasw==''):
         rem=font.render(f'Empty field!',True,'black')
         screen.blit(rem,(380,500))
      elif entbtn.check_click()==True:
         lres=login(usn,pasw)
         if lres[0]==3:#if their details have been found
            return True,usn,lres[1]
         elif lres[0]==2:#if their password is incorrect
            err=font.render(f'Password incorrect',True,'black')
            screen.blit(err,(320,500))
         elif lres[0]==1:#if their username is not in db
            err=font.render(f'Username unrecognised',True,'black')
            screen.blit(err,(320,500))

      backbtn=Button("Back",(50,50),(100,40))
      backbtn.drawbtn(screen)

      title=tfont.render(f'Log into account!',True,'black')
      screen.blit(title,(300,200))

      usn_surface = font.render(usn,True,(0,0,0))
      screen.blit(usn_surface,(us_rect.x + 5, us_rect.y +5)) #only updates the box
      us_rect.w=max(100,usn_surface.get_width() + 10)

      pas_surface = font.render(pasw,True,(0,0,0))
      screen.blit(pas_surface,(pas_rect.x + 5, pas_rect.y +5)) #only updates the box
      pas_rect.w=max(100,pas_surface.get_width() + 10)

      pygame.display.flip() #updates the screen
      clock.tick(60)

def accountmade(sirun):#run when signed in
   while sirun:
         screen.fill('white')
         #adds a cloud to the screen
         cloud1=pygame.image.load("project/cloud.png")
         cloud1=pygame.transform.scale(cloud1,(200,100))
         cloud1=cloud1.convert_alpha()
         cloud2=pygame.image.load("project/cloud.png")
         cloud2=pygame.transform.scale(cloud2,(230,110))
         cloud2=cloud2.convert_alpha()
         cloud3=pygame.image.load("project/cloud.png")
         cloud3=pygame.transform.scale(cloud3,(170,90))
         cloud3=cloud3.convert_alpha()
         screen.blit(cloud1,(600,20))
         screen.blit(cloud2,(350,70))
         screen.blit(cloud3,(150,50))

         #creates a ground on the screen
         ground=pygame.image.load("project/ground.png")
         ground=pygame.transform.scale(ground,(900,50))
         ground=ground.convert_alpha()
         screen.blit(ground,(0,750))

         font = pygame.font.SysFont('arial',20) 
         txtsurf=font.render(f'Account made! Return to main menu by pressing the Back button!',True,'black')
         screen.blit(txtsurf,(190,300))

         backbtn=Button("Back",(50,50),(100,40))
         backbtn.drawbtn(screen)

         for events in pygame.event.get():
            if events.type==pygame.QUIT: #lets user exit the window
               pygame.quit()
               sys.exit()
            if events.type==pygame.MOUSEBUTTONDOWN:
               if backbtn.check_click()==True:#returns to home
                  sirun=False
                  return True
         pygame.display.flip()

def signupscreen(ssrun):#run when user wants to sign up
   from db_alg import signup
   clock = pygame.time.Clock()
   tfont=pygame.font.SysFont('arial',30)
   font = pygame.font.SysFont('arial',20) 
   usn= ''
   pasw=''
   rpasw=''
   us_rect = pygame.Rect(380,300,600,30)#(x,y,width,height)
   pas_rect = pygame.Rect(380,350,600,30)#(x,y,width,height)
   rpas_rect = pygame.Rect(380,400,600,30)#(x,y,width,height)
   color_active=pygame.Color('blue')
   color_inactive=pygame.Color('black')
   color=color_inactive #initially the box is inactive so it starts black
   uactive=False
   pactive=False
   rpactive=False

   while ssrun:    
      for events in pygame.event.get():
         if events.type==pygame.QUIT: #lets user exit the window
            pygame.quit()
            sys.exit()
               
         if events.type==pygame.MOUSEBUTTONDOWN:
            if us_rect.collidepoint(events.pos):
               uactive = True #if the box is pressed, it becomes active/blue
               pactive=False
               rpactive=False
            elif pas_rect.collidepoint(events.pos):
               pactive=True
               uactive=False
               rpactive=False
            elif rpas_rect.collidepoint(events.pos):
               rpactive=True
               pactive=False
               uactive=False
            else:
               uactive=False#if the user click outside the box, it deactivates
               pactive=False
               rpactive=False
            if backbtn.check_click()==True:
                return False,'',0

         if events.type == pygame.KEYDOWN and uactive==True:
            if events.key==pygame.K_RETURN:#enter is pressed when the user wants to stop typing
               uactive=False#also deactivates when enter is pressed
               print(usn)
            elif events.key == pygame.K_BACKSPACE:
               usn = usn[:-1] #removes the last letter
            else:
               usn+=events.unicode #adds letter to screen
               
         if events.type == pygame.KEYDOWN and pactive==True:
            if events.key==pygame.K_RETURN:#enter is pressed when the user wants to stop typing
               pactive=False#also deactivates when enter is pressed
               print(pasw)
            elif events.key == pygame.K_BACKSPACE:
               pasw = pasw[:-1] #removes the last letter
            else:
               pasw+=events.unicode #adds letter to screen

         if events.type == pygame.KEYDOWN and rpactive==True:
            if events.key==pygame.K_RETURN:#enter is pressed when the user wants to stop typing
               rpactive=False#also deactivates when enter is pressed
               print(rpasw)
            elif events.key == pygame.K_BACKSPACE:
               rpasw = rpasw[:-1] #removes the last letter
            else:
               rpasw+=events.unicode #adds letter to screen
      
            
      screen.fill('white')
      #adds a cloud to the screen
      cloud1=pygame.image.load("project/cloud.png")
      cloud1=pygame.transform.scale(cloud1,(200,100))
      cloud1=cloud1.convert_alpha()
      cloud2=pygame.image.load("project/cloud.png")
      cloud2=pygame.transform.scale(cloud2,(230,110))
      cloud2=cloud2.convert_alpha()
      cloud3=pygame.image.load("project/cloud.png")
      cloud3=pygame.transform.scale(cloud3,(170,90))
      cloud3=cloud3.convert_alpha()
      screen.blit(cloud1,(600,20))
      screen.blit(cloud2,(350,70))
      screen.blit(cloud3,(150,50))

      #creates a ground on the screen
      ground=pygame.image.load("project/ground.png")
      ground=pygame.transform.scale(ground,(900,50))
      ground=ground.convert_alpha()
      screen.blit(ground,(0,750))

      if uactive==True or pactive==True or rpactive==True:#shows if the text box is active or not
         color=color_active
      else:
         color=color_inactive
         
      #for each displays on screen, with colour, with rectangle and outline of width 2
      pygame.draw.rect(screen,color,us_rect,2)
      us=font.render(f'Username:',True,'black')
      screen.blit(us,(280,302)) #adds title next to box

      pygame.draw.rect(screen,color,pas_rect,2)
      pst=font.render(f'Password:',True,'black')
      screen.blit(pst,(280,352))

      pygame.draw.rect(screen,color,rpas_rect,2)
      rpst=font.render(f'Re-enter password:',True,'black')
      screen.blit(rpst,(200,402))
      
      entbtn=Button("Enter",(340,450),(180,40))
      entbtn.drawbtn(screen)

      if entbtn.check_click()==True and (usn=='' or pasw=='' or rpasw==''):
         rem=font.render(f'Empty field!',True,'black')
         screen.blit(rem,(380,500))
         pygame.time.delay(50)
      
      elif entbtn.check_click()==True and (len(usn)>20 or len(pasw)>20 or len(rpasw)>20):
         err=font.render(f'Username and password cannot be more than 20 characters long!',True,'black')
         screen.blit(err,(150,500))
         pygame.time.delay(50)

      elif entbtn.check_click()==True and (usn!='' and pasw!='' and rpasw!=''):
         scomm=signup(usn,pasw,rpasw)
         if scomm[0]==3:
            return True,usn,scomm[1]
         elif scomm[0]==2:
            perror=font.render(f'Passwords do not match',True,'black')
            screen.blit(perror,(330,500))
         elif scomm[0]==1:
            uerror=font.render(f'Username taken. Enter different username.',True,'black')
            screen.blit(uerror,(240,500))

      backbtn=Button("Back",(30,50),(90,40))
      backbtn.drawbtn(screen)

      title=tfont.render(f'Create an account',True,'black')
      screen.blit(title,(300,200))

      usn_surface = font.render(usn,True,(0,0,0))
      screen.blit(usn_surface,(us_rect.x + 5, us_rect.y +5)) #only updates the box
      us_rect.w=max(100,usn_surface.get_width() + 10)

      pas_surface = font.render(pasw,True,(0,0,0))
      screen.blit(pas_surface,(pas_rect.x + 5, pas_rect.y +5)) #only updates the box
      pas_rect.w=max(100,pas_surface.get_width() + 10)

      rpas_surface = font.render(rpasw,True,(0,0,0))
      screen.blit(rpas_surface,(rpas_rect.x + 5, rpas_rect.y +5)) #only updates the box
      rpas_rect.w=max(100,rpas_surface.get_width() + 10)

      pygame.display.flip() #updates the screen
      clock.tick(60)

def pause_screen(prun):
    #setting up
    screen.fill('white')
    fps=60
    timer=pygame.time.Clock()
    tfont = pygame.font.SysFont('arialblack', 30) 
    #font = pygame.font.SysFont('arial', 20)
    timer.tick(fps)

    title=tfont.render(f'Game paused',True,'black')
    screen.blit(title,(330,300))
    resumebtn=Button("Resume",(300,400),(260,40))
    resumebtn.drawbtn(screen)
    homebtn=Button("Home",(300,450),(260,40))
    homebtn.drawbtn(screen)

    #adds a cloud to the screen
    cloud1=pygame.image.load("project/cloud.png")
    cloud1=pygame.transform.scale(cloud1,(200,100))
    cloud1=cloud1.convert_alpha()
    cloud2=pygame.image.load("project/cloud.png")
    cloud2=pygame.transform.scale(cloud2,(250,120))
    cloud2=cloud2.convert_alpha()
    cloud3=pygame.image.load("project/cloud.png")
    cloud3=pygame.transform.scale(cloud3,(170,90))
    cloud3=cloud3.convert_alpha()
    screen.blit(cloud1,(600,40))
    screen.blit(cloud2,(30,20))
    screen.blit(cloud3,(350,70))

    #creates a ground on the screen
    ground=pygame.image.load("project/ground.png")
    ground=pygame.transform.scale(ground,(900,50))
    ground=ground.convert_alpha()
    screen.blit(ground,(0,750))

    while prun:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                prun=False
                pygame.quit()
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if resumebtn.check_click()==True:
                    #should return to gameplay screen
                    return 2
                if homebtn.check_click()==True:
                    #should return to home screen
                    return 0
        
        pygame.display.flip()
    pygame.quit()

def info(irun):#run before main gameplay
    screen.fill('white')
    tfont = pygame.font.SysFont('arialblack', 30) 
    font=pygame.font.SysFont('arial', 23) 
    title=tfont.render(f'Before you start...',True,'black')
    screen.blit(title,(300,240))
    note=font.render(f'Please note:',True,'black')
    p1=font.render(f'- The trajectory of the object is not a realistic simulation to the question!',True,'black')
    p2=font.render(f'- Upwards should be taken as positive',True,'black')
    p3=font.render(f'- The value for gravity will always be -9.8',True,'black')
    p4=tfont.render(f'Have fun playing!',True,'#0044cc')
    screen.blit(note,(100,300))
    screen.blit(p1,(100,330))
    screen.blit(p2,(100,360))
    screen.blit(p3,(100,390))
    screen.blit(p4,(300,430))

    start_btn=Button('Got it!',(320,500),(260,40))
    start_btn.drawbtn(screen)
    tut_btn=Button('How to Play',(320,550),(260,40))
    tut_btn.drawbtn(screen)

    #adds a cloud to the screen
    cloud1=pygame.image.load("project/cloud.png")
    cloud1=pygame.transform.scale(cloud1,(200,100))
    cloud1=cloud1.convert_alpha()
    cloud2=pygame.image.load("project/cloud.png")
    cloud2=pygame.transform.scale(cloud2,(250,120))
    cloud2=cloud2.convert_alpha()
    cloud3=pygame.image.load("project/cloud.png")
    cloud3=pygame.transform.scale(cloud3,(170,90))
    cloud3=cloud3.convert_alpha()
    screen.blit(cloud1,(600,40))
    screen.blit(cloud2,(30,20))
    screen.blit(cloud3,(350,70))

    #creates a ground on the screen
    ground=pygame.image.load("project/ground.png")
    ground=pygame.transform.scale(ground,(900,50))
    ground=ground.convert_alpha()
    screen.blit(ground,(0,750))

    while irun:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                irun=False
                pygame.quit()
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if start_btn.check_click():
                    return 2#load main gameplay
                if tut_btn.check_click():
                    return 6#load tutorial screen
        
        pygame.display.flip()
    pygame.quit()

def tut(trun):#tutorial screen
    screen.fill('white')
    tfont = pygame.font.SysFont('arialblack',30) 
    font=pygame.font.SysFont('arial', 22) 
    title=tfont.render(f'How to play!',True,'black')
    screen.blit(title,(340,240))

    l1=font.render(f'- You will be asked to solve a SUVAT question that will be displayed',True,'black')
    l2=font.render(f'   in a box on the right hand side of the screen.',True,'black')
    l3=font.render(f'- Use the                  on the bottom left of the screen if you need help.',True,'black')
    w3=font.render(f'Equations',True,'#0044cc')
    l4=font.render(f'- Enter your answer in the box below it and press',True,'black')
    w4=font.render(f'Start!',True,'#0044cc')
    l5=font.render(f'- If your answer is correct, the object will land at the target and a new',True,'black')
    l6=font.render(f'   question will be displayed.',True,'black')
    l7=font.render(f'- If your answer is incorrect, the object will not land at the target and',True,'black')
    l8=font.render(f'   you can attempt the question again.',True,'black')
    l9=font.render(f'- You can also press         to change the question.',True,'black')
    w9=font.render(f'Skip',True,'#0044cc')

    screen.blit(l1,(100,300))
    screen.blit(l2,(100,330))
    screen.blit(l3,(100,360))
    screen.blit(w3,(195,360))
    screen.blit(l4,(100,390))
    screen.blit(w4,(575,390))
    screen.blit(l5,(100,420))
    screen.blit(l6,(100,450))
    screen.blit(l7,(100,480))
    screen.blit(l8,(100,510))
    screen.blit(l9,(100,540))
    screen.blit(w9,(300,540))

    start_btn=Button('Got it!',(320,600),(260,40))
    start_btn.drawbtn(screen)

    #adds a cloud to the screen
    cloud1=pygame.image.load("project/cloud.png")
    cloud1=pygame.transform.scale(cloud1,(200,100))
    cloud1=cloud1.convert_alpha()
    cloud2=pygame.image.load("project/cloud.png")
    cloud2=pygame.transform.scale(cloud2,(250,120))
    cloud2=cloud2.convert_alpha()
    cloud3=pygame.image.load("project/cloud.png")
    cloud3=pygame.transform.scale(cloud3,(170,90))
    cloud3=cloud3.convert_alpha()
    screen.blit(cloud1,(600,40))
    screen.blit(cloud2,(30,20))
    screen.blit(cloud3,(350,70))

    #creates a ground on the screen
    ground=pygame.image.load("project/ground.png")
    ground=pygame.transform.scale(ground,(900,50))
    ground=ground.convert_alpha()
    screen.blit(ground,(0,750))

    while trun:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                trun=False
                pygame.quit()
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if start_btn.check_click():
                    return 2#load main gameplay
        pygame.display.flip()
    pygame.quit()

#functions for main gameplay
def obj_pos(): #function to generate a random starting position
    import random
    x=round(random.uniform(160,300))
    y=round(random.uniform(400,710)) 
    return x,y #returns starting coordinate

def target_pos(): #generate a random target position
    import random
    x=round(random.uniform(330,500))
    y=715 #the target will always be on the ground
    return x,y #returns target coordinate

def calc_u(dx,dy,correct,diff):#x+30 just so the object lands in the center of the target
    import math
    u=math.sqrt((-4.9*((dx+30)**2)/(((math.cos(math.radians(60)))**2)*(-dy-(dx+30)*math.tan(math.radians(60))))))
    if correct==True:
        return u
    elif diff!=0:#if answer is not correct, the object will not land at the target
        u=u+diff
        return u

def cloud(correct,background):
    #adds a cloud to the screen
    cloudp=pygame.image.load("project/cloud.png")
    cloudp=pygame.transform.scale(cloudp,(200,100))
    cloudp=cloudp.convert_alpha()
    font = pygame.font.Font('freesansbold.ttf',27)
    if correct==True:#displays if its correct or not
        background.blit(cloudp,(380,120))
        txt=font.render('Correct!',True,'black')
        background.blit(txt,(425,165))
    else:
        background.blit(cloudp,(380,120))
        txt=font.render('Incorrect',True,'black')
        background.blit(txt,(425,165))

def main_gameplay(mode,username,curscore):
    import math, textwrap
    from q_ans import gen_qa
    from button import hover_equ
    from db_alg import scoring
    pygame.init()
    #setting up variables
    font = pygame.font.SysFont('arial', 17)
    color=pygame.Color('black')
    event= pygame.event.Event
    projectile= pygame.Surface
    opos=obj_pos()
    initial_x=opos[0]#x-coordinate of starting pos
    initial_y=opos[1]#y-coordinate of starting pos
    x1=initial_x#another copy of x for the trajectory
    y1=initial_y#another copy of y for the trajectory
    x=initial_x #copy of x
    y=initial_y#copy of y
    time=0
    project=False #at the start projection hasnt started
    angle=60
    ans=''
    clock=pygame.time.Clock()
    user_quit=False
    tpos=target_pos()
    tx=tpos[0]
    ty=tpos[1]
    tpoints=[]
    errmess=''#no error has occurred yet at the start
    if username=='':
        score=0#score starts from 0 if the user is not logged in
    else:
        score=curscore
    points=5

    #creates a pygame background surface
    background=pygame.Surface((900,800))

    #adds an object to the screen to project
    projectile=pygame.image.load("project/glass-ball-png-image.png")
    projectile=pygame.transform.scale(projectile,(30,30))
    projectile=projectile.convert_alpha()

    #creates a ground on the screen
    ground=pygame.image.load("project/ground.png")
    ground=pygame.transform.scale(ground,(900,50))
    ground=ground.convert_alpha()

    #adds a target on screen
    target=pygame.image.load("project/hole.png")
    target=pygame.transform.scale(target,(90,40))
    target=target.convert_alpha()

    #makes a box on the RHS of screen where user can enter values
    sidebox=pygame.Surface((200,300))
    ans_rect=pygame.Rect(115,240,30,25)

    #makes all the buttons needed on the screen
    startbtn=Button("Start!",(780,650),(100,40))
    pausebtn=Button("Pause",(780,60),(100,40))
    skipbtn=Button("Skip",(780,700),(100,40))
    equbtn=hover_equ('Equations',(15,690),(130,40))

    mlogsign = dropmenu(
    [inact_colour,act_colour],
    [inact_optcolour,act_optcolour],
    700, 10, 180, 40, tfont, 
    "Login/Sign up", ["Login","Sign up"])
    
    #displays score box on LHS of screen
    pygame.draw.rect(background,'light grey', pygame.Rect(10, 10, 200, 30))
    scoretxt=font.render('Score:',True,(0,0,0))

    qa=gen_qa(mode)#only calls it once
    print(qa[0])#prints question in terminal
    print(qa[1])#print answer in terminal

    #adds a cloud to the screen
    cloud1=pygame.image.load("project/cloud.png")
    cloud1=pygame.transform.scale(cloud1,(200,100))
    cloud1=cloud1.convert_alpha()
    cloud2=pygame.image.load("project/cloud.png")
    cloud2=pygame.transform.scale(cloud2,(230,110))
    cloud2=cloud2.convert_alpha()

    while not user_quit:
        clock.tick(30)

        background.fill('white')#white background 

        #blits buttons on top of the background
        startbtn.drawbtn(background)
        pausebtn.drawbtn(background)
        skipbtn.drawbtn(background)
        equbtn.drawbtn(background)
        mlogsign.draw(background)

        #draws clouds on background
        background.blit(cloud1,(600,90))
        background.blit(cloud2,(100,60))

        #displays score box on LHS of screen
        pygame.draw.rect(background,'light grey', pygame.Rect(10, 10, 200, 30))
        scoretxt=font.render('Score:',True,(0,0,0))
        background.blit(scoretxt,(14,14))
        disp_score=font.render(str(score),True,'black')
        background.blit(disp_score,(70,15))

        #sets colour of sidebox
        sidebox.fill('light grey')

        events=pygame.event.get()
        #checks if login or signup was selected 
        selected_opt = mlogsign.update(events)
        if selected_opt == 0:#if login is selected
            #changes the current displayed option on the menu to the selected one
            command=1#should blit to login screen
            return command
        elif selected_opt == 1:#if sign up is selected
            command=3#should blit to sign up screen
            return command

        for event in events:
            if event.type==pygame.QUIT: #lets user exit window
                user_quit=True
                pygame.quit()
                sys.exit()
            
            if event.type==pygame.MOUSEBUTTONDOWN:
                if ans_rect.collidepoint(event.pos):
                    uactive=True #if the box is pressed, it becomes active
                else:
                    uactive=False#if the user click outside the box, it deactivates
                if startbtn.check_click()==True and ans=='':#blits an error message if nothing is entered
                    errmess=font.render(f'Enter an answer!',True,'black')
                elif startbtn.check_click()==True:
                    try:
                        numb=float(ans)#turns the user's answer into a float
                        err=False
                        project=True
                        errmess=''#there's no error message
                    except ValueError:
                        #if it cannot turn into a float, a letter/unexpected character has been entered
                        err=True
                        project=False
                        errmess=font.render('Enter a number!',True,'black')
                        #reminds the user to enter a number
                if skipbtn.check_click()==True:
                    qa=gen_qa(mode)
                    print(qa[0])#checking if it reaches this point
                    print(qa[1])
                    #makes the question into a para then blits on side box
                    sidebox.fill('light grey')
                    pquest=textwrap.wrap(qa[0],width=250//10)
                    ofsy=20
                    for line in pquest:
                        question=font.render(line,True,(0,0,0))
                        sidebox.blit(question,(5,ofsy))
                        ofsy+=question.get_height()+5
                if pausebtn.check_click()==True:
                    return 4

            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:#enter is pressed when the user wants to stop typing
                    uactive=False#also deactivates when enter is pressed
                    print(ans)
                elif event.key==pygame.K_BACKSPACE:
                    ans=ans[:-1] #removes the last character
                else:
                    ans+=event.unicode #adds character to screen
        
        if errmess:#if there is an error message
            sidebox.blit(errmess,(3,210))#display the message onto the screen

        if project and err==False:#occurs when user enters in a value and presses start
            #checks if answer is correct.
            if round(float(ans),2)==qa[1]:
                correct=True
                diff=0
            elif round(float(ans),2)>qa[1]:
                correct=False
                diff=15
            else:
                correct=False
                diff=-15
            #pass in the target's x distance and y distance, if ans is correct and a set difference
            u=calc_u(tx-x1,715-y1,correct,diff)
            time=time+(1/10) #time increments
            speed=float(u)
            #calculates x and y values of the object when it projects
            x=(initial_x+math.cos(math.radians(angle))*speed*time)
            y=(initial_y-(math.sin(math.radians(angle))*speed*time)+0.5*9.8*time**2)
            #displays if its correct or not
            cloud(correct,background)

            #check if it hits the ground
            if y+projectile.get_height()>=748:
                time=0
                project=False
                a=tpoints[-1]#gets the last coordinate of the object/where it lands
                for point in tpoints:#removes the last trajectory from screen
                    pygame.draw.circle(background,'white',point,2)
                tpoints.clear()
                if (tx<=a[0] and a[0]<=tx+45) and (ty-20<=a[1] and a[1]<=ty+20):#if it lands at target (there's a range)
                    #resets ball position
                    opos=obj_pos()
                    initial_x=opos[0]
                    initial_y=opos[1]
                    x1=initial_x
                    y1=initial_y
                    x=initial_x
                    y=initial_y
                    #changes target position
                    tpos=target_pos()
                    tx=tpos[0]
                    ty=tpos[1]
                    #generates new question
                    qa=gen_qa(mode)
                    print(qa[0])#checking if it reaches this point
                    print(qa[1])
                    #makes the question into a para then blits on side box
                    sidebox.fill('light grey')
                    pquest=textwrap.wrap(qa[0],width=250//10)
                    ofsy=20
                    for line in pquest:
                        question=font.render(line,True,(0,0,0))
                        sidebox.blit(question,(5,ofsy))
                        ofsy+=question.get_height()+5
                    #updates score
                    if username=='':
                        score=score+points
                    else:
                        score=scoring(username,points)
                    disp_score=font.render(str(score),True,'black')
                    background.blit(disp_score,(70,15))
                else:
                    x=initial_x 
                    y=initial_y

        #adds ans box where user enters their values
        ans_surf = font.render(ans,True,(0,0,0))
        sidebox.blit(ans_surf,(ans_rect.x+ 5, ans_rect.y+5)) #only updates the box
        ans_rect.w=max(60,ans_surf.get_width() + 10)

        #displays the ans box on the sidebox
        pygame.draw.rect(sidebox,color,ans_rect,2)
        title_ans=font.render(f'Enter answer:',True,color) #adds a label for the box
        sidebox.blit(title_ans,(3,240))

        #makes the question into a para then blits on side box
        pquest=textwrap.wrap(qa[0],width=250//10)
        ofsy=20
        for line in pquest:
            question=font.render(line,True,(0,0,0))
            sidebox.blit(question,(5,ofsy))
            ofsy+=question.get_height()+5

        #draws a line of motion
        if time>0:
            tpoints.append((int(x),int(y)))
        for point in tpoints:
            pygame.draw.circle(background,'#0044cc',point,2)

        #checks if the mouse it over the button
        mouse_pos = pygame.mouse.get_pos()
        equbtn.hover_check(mouse_pos)
        equbtn.show_equ(background)#displays equations when hovered over

        #updates everything on screen
        screen.blit(background,(0,0))
        screen.blit(target,(tx,ty))
        screen.blit(projectile,(x,y))
        screen.blit(ground,(0,750))
        screen.blit(sidebox,(650,300))
        pygame.display.update()

    pygame.quit()

#setting up
fps=60
timer=pygame.time.Clock()
font=pygame.font.Font('freesansbold.ttf',24)
tfont=pygame.font.Font('freesansbold.ttf',22)
screen=pygame.display.set_mode([900,800])
pygame.display.set_caption('solving.SUVAT')
home=True
home_command=0
inact_colour='grey'
act_colour='light grey'
inact_optcolour='grey'
act_optcolour='light grey'

#creating a mode menu with options SUVT
mode = dropmenu(
[inact_colour,act_colour],
[inact_optcolour,act_optcolour],
300, 450, 260, 40, tfont, 
"Select Mode", ["S", "U","V","T"])

#creating a login/signup menu 
logsign = dropmenu(
[inact_colour,act_colour],
[inact_optcolour,act_optcolour],
300, 400, 260, 40, tfont, 
"Login/Sign up", ["Login","Sign up"])

#main game loop
hrun=True
lsrun=False
lirun=False
prun=False
irun=False
trun=False
username=''
current_score=0
while hrun:
    screen.fill('white')
    timer.tick(fps)

    #to stop the loop
    events = pygame.event.get()
    for event in events:
        if event.type==pygame.QUIT:
            hrun=False
        
    if home: #runs when home is True
        command=draw_home()

        #checks if a mode was selected 
        selected_opt = mode.update(events)
        if selected_opt >= 0:#if an option is selected
            #changes the current displayed option on the menu to the selected one
            mode.main = mode.options[selected_opt]
            print(mode.main)

        if command>0:
            home=False
        elif command==0:
            home=True

    else:
        if command>0:
            if command==1:#login is pressed
                lsrun=True
                #logscreen runs
                logg,username,current_score=logscreen(lsrun)
                if logg==True:#if they logged in
                    print(username,current_score)
                    lsrun=False
                    lirun=True#call the logged in screen
                    home=loggedin(lirun)#shows loggedin screen
                    command=0
                elif logg==False:#if they didnt login/pressed back
                    lsrun=False
                    command=0
                    home=True
            elif command==3:#if sign up was selected
                ssrun=True
                #logscreen runs
                signed,username,current_score=signupscreen(ssrun)
                if signed==True:#if they signed in
                    print(username,current_score)
                    ssrun=False
                    sirun=True#call the logged in screen
                    home=accountmade(sirun)#shows loggedin screen
                    command=0
                elif signed==False:#if they didnt login/pressed back
                    ssrun=False
                    command=0
                    home=True
            elif command==2: #if start is selected
                #show info screen
                irun=True
                icom=info(irun)
                if icom==2:#if [Got it!] is pressed
                    #load gameplay screen after
                    command=main_gameplay(mode.main,username,current_score)
                elif icom==6:#if [How to Play] is pressed
                    trun=True
                    command=tut(trun)#show tutorial screen
            elif command==5:#if they press start but do not select a mode
                modebackbtn=Button('Back',(50,50),(100,40))
                modebackbtn.drawbtn(screen)
                text=font.render(f'Go back and select a mode!',True,'black')
                screen.blit(text,(280,240))
                #adds a cloud to the screen
                cloud1=pygame.image.load("project/cloud.png")
                cloud1=pygame.transform.scale(cloud1,(200,100))
                cloud1=cloud1.convert_alpha()
                cloud2=pygame.image.load("project/cloud.png")
                cloud2=pygame.transform.scale(cloud2,(230,110))
                cloud2=cloud2.convert_alpha()
                cloud3=pygame.image.load("project/cloud.png")
                cloud3=pygame.transform.scale(cloud3,(170,90))
                cloud3=cloud3.convert_alpha()
                screen.blit(cloud1,(600,20))
                screen.blit(cloud2,(350,70))
                screen.blit(cloud3,(150,50))
                #creates a ground on the screen
                ground=pygame.image.load("project/ground.png")
                ground=pygame.transform.scale(ground,(900,50))
                ground=ground.convert_alpha()
                screen.blit(ground,(0,750))
                if modebackbtn.check_click()==True:
                    home=True
            elif command==4:#if pause is pressed
                prun=True
                pcomm=pause_screen(prun)
                if pcomm==0:#if home is pressed
                    prun=False
                    command=0
                    home=True
                elif pcomm==2:#if resume is pressed
                    prun=False
                    command=2
    pygame.display.flip()
pygame.quit()