import time
from tkinter import *
from tkinter.messagebox import *
import os
import sys
import pygame as pg 
CAPTION = "Drag the Red Square"
SCREEN_SIZE = (1000, 600)
class Character(object):
    SIZE = (150, 150)
    def __init__(self, pos):
        self.rect = pg.Rect((0,0), Character.SIZE)
        self.rect.center = pos
        self.text, self.text_rect = self.setup_font("black")
        self.click = False
    def setup_font(self,color):
        font = pg.font.SysFont('timesnewroman', 30)
        message = "prout"
        label = font.render(message, True, pg.Color(color))
        label_rect = label.get_rect()
        return label, label_rect

    def check_click(self, pos):
        if self.rect.collidepoint(pos):
            self.click = True
            self.text, self.text_rect = self.setup_font("white")
            pg.mouse.get_rel()
        else: self.text, self.text_rect = self.setup_font("black")

    def update(self, screen_rect):
        if self.click:
            self.rect.move_ip(pg.mouse.get_rel())
            self.rect.clamp_ip(screen_rect)
        self.text_rect.center = (self.rect.centerx, self.rect.centery+90)

    def draw(self, surface):
        surface.fill(pg.Color("red"), self.rect)
        surface.blit(self.text, self.text_rect)
        
class App(object):
    def __init__(self):
        self.screen = pg.display.get_surface()
        self.screen_rect = self.screen.get_rect()
        self.clock = pg.time.Clock()
        self.fps = 60
        self.done = False
        self.keys = pg.key.get_pressed()
        self.player = Character(self.screen_rect.center)

    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or self.keys[pg.K_ESCAPE]:
                self.done = True
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                self.player.check_click(event.pos)
            elif event.type == pg.MOUSEBUTTONUP and event.button == 1:
                self.player.click = False
            elif event.type in (pg.KEYUP, pg.KEYDOWN):
                self.keys = pg.key.get_pressed() 

    def render(self):
        self.screen.fill(pg.Color("black"))
        self.player.draw(self.screen)
        pg.display.update()

    def main_loop(self):
        while not self.done:
            self.event_loop()
            self.player.update(self.screen_rect)
            self.render()
            self.clock.tick(self.fps)


def main():
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pg.init()
    pg.display.set_caption(CAPTION)
    pg.display.set_mode(SCREEN_SIZE)
    App().main_loop()
    pg.quit()
    sys.exit()
 
def fenetre(question, title, rep1, rep2, ret1, ret2):
	def Verif():
		if rep.get()==rep1:
			showinfo(title, ret1)
			Mafenetre.destroy()
		elif rep.get()==rep2:
			showinfo(title, ret2)
			Mafenetre.destroy()
		else:
			showwarning('attention','error')
			rep.set('')
	Mafenetre=Tk()
	Mafenetre.title(title)
	Label1=Label(Mafenetre, text= question)
	Label1.pack(side=LEFT, padx=5,pady=5)
	rep=StringVar()
	Champ=Entry(Mafenetre, textvariable=rep, bg='bisque', fg='maroon')
	Champ.focus_set()
	Champ.pack(side=LEFT, padx=5, pady=5)
	Bouton=Button(Mafenetre, text='valider',command=Verif)
	Bouton.pack(side=LEFT, padx=5, pady=5)
	Mafenetre.mainloop()

montemps=time.time()
y=time.time()-montemps
while time.localtime(y)[3]-1<1:
    y=time.time()-montemps
    time.sleep(1)
    print (time.localtime(y)[3]-1,'h',time.localtime(y)[4],'min',time.localtime(y)[5],'s')
    main()
    if time.localtime(y)[5]==5 or time.localtime(y)[4]==10 or time.localtime(y)[4]==15 or time.localtime(y)[4]==20 or time.localtime(y)[4]==25 or time.localtime(y)[4]==30 or time.localtime(y)[4]==35 or time.localtime(y)[4]== 40 or time.localtime(y)[4]==45 or time.localtime(y)[4]==50 or time.localtime(y)[4]==55:
    	fenetre('un indice?', 'indice', 'oui', 'non', 'des friandises pour le chien sont\n posées dans une boite métalique sur \n le bureau','ok' )
print('fin')