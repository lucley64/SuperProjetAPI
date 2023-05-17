import sys, pygame, time, os
from pygame.locals import *
import tkinter as tk
from tkinter.messagebox import *
pygame.init()
tailleFenetre=1366, 768
taille = largeur, hauteur =tailleFenetre
noir = 100, 100, 255

ecran = pygame.display.set_mode(taille)

aimant=pygame.image.load("aimant.png")
aimant=pygame.transform.scale(aimant,(70,70))
aimant2=pygame.image.load("aimant2.png")
aimant2=pygame.transform.scale(aimant2,(180,180))
fond=pygame.image.load("arrière plan.jpg")
fond=pygame.transform.scale(fond,(tailleFenetre))
fond_deux=pygame.image.load("arrière plan2.png")
fond_deux=pygame.transform.scale(fond_deux,(tailleFenetre))
fond_trois=pygame.image.load("arrière plan3.png")
fond_trois=pygame.transform.scale(fond_trois,(tailleFenetre))
fond_quatre=pygame.image.load("arrière plan4.png")
fond_quatre=pygame.transform.scale(fond_quatre,(tailleFenetre))
barreau=pygame.image.load("barreau.png")
barreau=pygame.transform.scale(barreau,(tailleFenetre))
barreau2=pygame.image.load("barreau2.png")
barreau2=pygame.transform.scale(barreau2,(70,70))
bougie=pygame.image.load("bougie.png")
bougie=pygame.transform.scale(bougie,(130,225))
bureau=pygame.image.load("bureau.png")
bureau=pygame.transform.scale(bureau,(600,400))
bureau2=pygame.image.load("bureau_ovrt.png")
bureau2=pygame.transform.scale(bureau2,(600,400))
casque=pygame.image.load("casque_audio.png")
casque=pygame.transform.scale(casque,(130,130))
casier=pygame.image.load("casier.png")
casier=pygame.transform.scale(casier,(450,600))
casier2=pygame.image.load("casier2.png")
casier2=pygame.transform.scale(casier2,(450,600))
chien=pygame.image.load("chien.png")
chien=pygame.transform.scale(chien,(800,450))
chien2=pygame.image.load("chien2.png")
chien2=pygame.transform.scale(chien2,(250,400))
cle=pygame.image.load("clé.png")
cle=pygame.transform.scale(cle,(70,70))
cle3=pygame.image.load("clé2.png")
cle3=pygame.transform.scale(cle3,(70,70))
coffre=pygame.image.load("coffre.png")
coffre=pygame.transform.scale(coffre,(300,200))
coffre_ouvert=pygame.image.load("coffre ouvert.png")
coffre_ouvert=pygame.transform.scale(coffre_ouvert,(390,260))
commode=pygame.image.load("commode.png")
commode=pygame.transform.scale(commode,(600,300))
commode2=pygame.image.load("commode_ovrt.png")
commode2=pygame.transform.scale(commode2,(600,300))
biscuits=pygame.image.load("dog_biscuits.png")
biscuits=pygame.transform.scale(biscuits,(80,110))
biscuits2=pygame.transform.scale(biscuits,(70,70))
enigme1=pygame.image.load("enigme1.png")
enigme1=pygame.transform.scale(enigme1,(70,70))
enigme2=pygame.image.load("enigme2.png")
enigme2=pygame.transform.scale(enigme2,(70,70))
enigme3=pygame.transform.scale(enigme2,(70,70))
etagere=pygame.image.load("etagere.png")
etagere=pygame.transform.scale(etagere,(400,200))
faux_mur=pygame.image.load("faux_mur.png")
faux_mur=pygame.transform.scale(faux_mur,(90,210))
fenetre1=pygame.image.load("fenetre.png")
fenetre1=pygame.transform.scale(fenetre1,(120,120))
fenetre2=pygame.image.load("fenetre2.png")
fenetre2=pygame.transform.scale(fenetre2,(120,120))
fleche_avant=pygame.image.load("fleche avant.png")
fleche_avant=pygame.transform.scale(fleche_avant,(300,150))
fleche_arriere=pygame.image.load("fleche derrière.png")
fleche_arriere=pygame.transform.scale(fleche_arriere,(300,150))
fleche_gauche=pygame.image.load("fleche de gauche.png")
fleche_gauche=pygame.transform.scale(fleche_gauche,(300,150))
fleche_droite=pygame.image.load("fleche droite.png")
fleche_droite=pygame.transform.scale(fleche_droite,(300,150))
gardien=pygame.image.load("gardien.png")
gardien=pygame.transform.scale(gardien,(950,600))
inventaire=pygame.image.load("inventaire.png")
inventaire=pygame.transform.scale(inventaire,(1366,100))
item_slot=pygame.image.load("item_slot.png")
item_slot=pygame.transform.scale(item_slot,(70,70))
lime=pygame.image.load("lime.png")
lime=pygame.transform.scale(lime,(70,70))
lime2=pygame.image.load("lime2.png")
lime2=pygame.transform.scale(lime2,(150,150))
lit=pygame.image.load("lit.png")
lit=pygame.transform.scale(lit,(600,425))
marteau=pygame.image.load("marteau2.png")
marteau=pygame.transform.scale(marteau,(65,150))
marteau2=pygame.image.load("marteau.png")
marteau2=pygame.transform.scale(marteau2,(70,70))
clé2=pygame.image.load("petiteclé.png")
clé2=pygame.transform.scale(clé2,(70,70))
pince=pygame.image.load("pince.png")
pince=pygame.transform.scale(pince,(80,200))
pince2=pygame.image.load("pince.png")
pince2=pygame.transform.scale(pince2,(70,70))
porte=pygame.image.load("porte barreau.png")
porte=pygame.transform.scale(porte,(tailleFenetre))
porte2=pygame.image.load("porte barreau ovrt.png")
porte2=pygame.transform.scale(porte2,(tailleFenetre))
porte_manteau=pygame.image.load("porte manteau.png")
porte_manteau=pygame.transform.scale(porte_manteau,(150,500))
serrure=pygame.image.load("serrure.png")
serrure=pygame.transform.scale(serrure,(tailleFenetre))
serrure2=pygame.image.load("serrure_ovrt.png")
serrure2=pygame.transform.scale(serrure2,(tailleFenetre))
tonneau=pygame.image.load("tonneau.png")
tonneau=pygame.transform.scale(tonneau,(225,300))
exterieur=pygame.image.load("vue exterieur.png")
exterieur=pygame.transform.scale(exterieur,(tailleFenetre))
win=pygame.image.load("win.png")
win=pygame.transform.scale(win,(tailleFenetre))
histoire=pygame.image.load("histoire.png")
histoire=pygame.transform.scale(histoire,(tailleFenetre))


pygame.mixer.music.load(b'ost.wav')
pygame.mixer.music.play()
pygame.mixer.music.play(loops=-1)
font = pygame.font.Font(None, 20)
ecran.fill(noir)
ecran.blit(histoire,(0,0))
pygame.display.flip()
mur = 'rien'

def mur_arrière(lim, barraux, item1):
    font = pygame.font.Font(None, 20)
    ecran.fill(noir)            
    ecran.blit(fond,(0,0))
    ecran.blit(fleche_arriere,(0,0))
    ecran.blit(lit,(-10,175))
    if barraux=='sciés':
        ecran.blit(fenetre2,(300,150))
    else : ecran.blit(fenetre1,(300,150))
    ecran.blit(etagere,(700,100))
    if item1==False: ecran.blit(coffre,(750,450))
    if item1==True: ecran.blit(coffre_ouvert,(670,387))
    ecran.blit(tonneau,(1100,425))
    if lim==True:
        ecran.blit(lime2,(1145,315))
    ecran.blit(bougie,(75,100))
    pygame.display.flip()
    

def mur_avant(cht, biscits, door):
    font = pygame.font.Font(None, 20)
    ecran.fill(noir)
    ecran.blit(fond_deux,(0,0))
    ecran.blit(bougie,(725,-40))
    ecran.blit(gardien,(300,-50))
    if cht:
        ecran.blit(chien,(-100,300))
    else: ecran.blit(chien2,(375,360))
    ecran.blit(casque,(535,160))
    if biscits:
        ecran.blit(biscuits,(1050,165))
    ecran.blit(barreau,(0,0))
    if door:
        ecran.blit(porte,(-35,10))
        ecran.blit(serrure,(400,90))
    else:
        ecran.blit(porte2,(-35,10))
        ecran.blit(serrure2,(400,90))
    ecran.blit(fleche_avant,(0,0))
    pygame.display.flip()
    

def mur_droit(csr, item7, item11):
    font = pygame.font.Font(None, 20)
    ecran.fill(noir)            
    ecran.blit(fond_quatre,(0,0))
    if not item11:
        ecran.blit(commode,(100,330))
    else:
        ecran.blit(commode2,(100,330))
    if csr:
        ecran.blit(casier,(825,30))
    else:
        ecran.blit(casier2,(825,30))
        if item7==False:
            ecran.blit(marteau,(945,440))
    ecran.blit(fleche_droite,(0,0))
    pygame.display.flip()
    

def mur_gauche(fxmur, item8, item10):
    font = pygame.font.Font(None, 20)
    ecran.fill(noir)            
    ecran.blit(fond_trois,(0,0))
    if fxmur:
        ecran.blit(faux_mur,(781,190))
    elif item8==False:
        print(item8)
        ecran.blit(pince,(785,195))
    if not item10:
        ecran.blit(bureau,(100,300))
    else: ecran.blit(bureau2,(100,300))
    ecran.blit(porte_manteau,(950,110))
    ecran.blit(fleche_gauche,(0,0))
    pygame.display.flip()
    

def vue_exterieur(item3):
    font = pygame.font.Font(None, 20)
    ecran.fill(noir)            
    ecran.blit(exterieur,(0,0))
    if not item3:
        ecran.blit(aimant2,(1150,208))
    pygame.display.flip()

def enigme_puzzel():
    font = pygame.font.Font(None, 20)
    ecran.fill(noir)            
    ecran.blit(puzzel,(0,0))
    ecran.blit(piece1,(10,10))
    ecran.blit(piece2,(10,10))
    ecran.blit(piece3,(10,10))
    ecran.blit(piece4,(10,10))
    ecran.blit(piece5,(10,10))
    ecran.blit(piece6,(10,10))
    ecran.blit(piece7,(10,10))
    ecran.blit(piece8,(10,10))
    ecran.blit(piece9,(10,10))
    ecran.blit(piece10,(10,10))
    ecran.blit(piece11,(10,10))
    ecran.blit(piece12,(10,10))
    pygame.display.flip()
    
    
def fenetre(question, title, rep1, rep2, ret1, ret2):
    root= tk.Tk()
    if rep1=='':
        showwarning(title,question)
        root.destroy()
        return 'rien'
    elif rep2=='code':
        def validation():
            if code.get()==rep1:
                tk.messagebox.showinfo(title, ret1)
                root.destroy()
            else :
                showwarning(title,ret2)
        root.title(title)
        codeLabel = tk.Label(root, text=question).grid(row=0, column=0)
        code = tk.StringVar()
        codeEntry = tk.Entry(root, textvariable=code).grid(row=0, column=1)
        valider = tk.Button(root, text="Valider", command=validation).grid(row=4, column=0)
        root.mainloop()
        return (code.get())
    else:
        Msgbox=tk.messagebox.askquestion(title,question)
        if Msgbox == 'yes':
            tk.messagebox.showinfo(title, ret1)
            root.destroy()
            return Msgbox
        else:
            tk.messagebox.showinfo(title, ret2)
            root.destroy()
            return Msgbox

	

def main(mur, item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12):
    montemps=time.time()
    y=time.time()-montemps
    cht=True 
    done=False
    impact=0
    lim = True
    barraux='non'
    biscits=True
    csr=True
    fxmur=True
    code=False
    door=True
    while not done:
        y=time.time()-montemps
        time.sleep(0.01)
        if time.localtime(y)[3]-1==1:
            done = True
        print (time.localtime(y)[3]-1,'h',time.localtime(y)[4],'min',time.localtime(y)[5],'s')
        if (time.localtime(y)[4]==5 or time.localtime(y)[4]==10 or time.localtime(y)[4]==15 or time.localtime(y)[4]==20 or time.localtime(y)[4]==25 or time.localtime(y)[4]==30 or time.localtime(y)[4]==35 or time.localtime(y)[4]== 40 or time.localtime(y)[4]==45 or time.localtime(y)[4]==50 or time.localtime(y)[4]==55) and time.localtime(y)[5]==0:    
            if not item1:
                fenetre('un indice?', 'indice', 'oui', 'non', 'il y a un coffre entre le tonneau et le lit','ok' )
            elif not item4:
                fenetre('un indice?', 'indice', 'oui', 'non', "il semble qu'une lime soit plantée dans le tonneau",'ok' )
            elif barraux!='sciés':
                fenetre('un indice?', 'indice', 'oui', 'non', "des barraux sont attachés a une fenêtre, ils pourraient être sciés",'ok' )
            elif not item10:
                fenetre('un indice?', 'indice', 'oui', 'non', "il y a peut-être quelque chose d'utile dans le burreau...",'ok' )
            elif not item11:
                fenetre('un indice?', 'indice', 'oui', 'non', "la clé pourraie peut-être ouvrir la commode",'ok' )
            elif not code:
                fenetre('un indice?', 'indice', 'oui', 'non', "des fois lire un papier peut débloquer des situations",'ok' )
            elif csr:
                fenetre('un indice?', 'indice', 'oui', 'non', "il y a un casier pouvant desormé être ouvert à droite",'ok' )
            elif not item7:
                fenetre('un indice?', 'indice', 'oui', 'non', "un marteau ce trouve dans ce casier",'ok' )
            elif fxmur:
                fenetre('un indice?', 'indice', 'oui', 'non', "des fois regarder de plus près un mur peut dévoiler des secrets",'ok' )
            elif not item8:
                fenetre('un indice?', 'indice', 'oui', 'non', "il y une pince dans le trou du mur",'ok' )
            elif not item3:
                fenetre('un indice?', 'indice', 'oui', 'non', "la pince pourrais attraper quelque chose qui était hors de portée",'ok' )
            elif not item9 and not item5:
                fenetre('un indice?', 'indice', 'oui', 'non', "l'aimant pourais atraper un objet métalique un peut loin",'ok' )
            elif not item5:
                fenetre('un indice?', 'indice', 'oui', 'non', "les biscuits pourraient être donnés à quelque chose mais quoi?",'ok' )
            elif door :
                fenetre('un indice?', 'indice', 'oui', 'non', "les clés pourraient peut-être ouvrir un porte",'ok' )
            elif not item12:
                fenetre('un indice?', 'indice', 'oui', 'non', "il reste un endroit qui n'a pas été fouillé",'ok' )
            else:
                fenetre('un indice?', 'indice', 'oui', 'non', "allez devinez il faut aller où?",'ok' )
        for event in pygame.event.get():
            if  event.type == pygame.QUIT :
                done= True
            if event.type == KEYDOWN:
                if event.key==K_ESCAPE:
                    done = True            
                if event.key == K_DOWN:
                    mur_arrière(lim, barraux, item1)
                    mur = 'arr'
                elif event.key == K_UP:
                    mur_avant(cht, biscits, door)
                    mur = 'avt'
                elif event.key == K_LEFT:
                    mur_gauche(fxmur, item8, item10)
                    mur = 'gch'
                elif event.key == K_RIGHT:
                    mur_droit(csr, item7, item11)
                    mur = 'drt'
                pygame.display.flip()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                if event.pos[0]>750 and event.pos[1]>450 and event.pos[0]<950 and event.pos[1]<600 and mur == 'arr' and item1==False:
                    if fenetre('ouvrir ?', 'coffre', 'oui', 'non', 'obtenu: papier froissé', 'ok')== 'yes' :
                        item1=True
                        son_coffre=pygame.mixer.Sound(b'coffre.wav')
                        son_coffre.play()
                        mur_arrière(lim, barraux, item1)
                if event.pos[0]>1100 and event.pos[1]>425 and event.pos[0]<1325 and event.pos[1]<725 and mur == 'arr':
                    if fenetre('une lime est plantée dans ce tonneau\n la prendre?', 'tonneau', 'oui', 'non', 'obtenu: lime', 'ok')== 'yes':
                        item4=True
                        son_lime=pygame.mixer.Sound(b'lime.wav')
                        son_lime.play()
                        lim = False
                        mur_arrière(lim, barraux, item1)
                if event.pos[0]>300 and event.pos[1]>150 and event.pos[0]<420 and event.pos[1]<270 and mur == 'arr':
                    if item4 and barraux != 'sciés':
                        if fenetre('des barraux sont attachés à cette fenêtre \n cela tombe bien, vous possedez une lime \n les scier ?', 'fenêtre', 'oui', 'non', 'vous pouvez maitenant passer votre tête par la fenêtre', 'ok')== 'yes' :
                            barraux='sciés'
                            son_limer=pygame.mixer.Sound(b'limer.wav')
                            son_limer.play()
                    elif barraux=='non': fenetre('des barraux sont attachés à cette fenêtre ', 'fenêtre', '', '', '', '')
                if event.pos[0]>300 and event.pos[1]>150 and event.pos[0]<420 and event.pos[1]<270 and mur == 'arr' and barraux=='sciés':
                    vue_exterieur(item3)
                    mur='ext'
                if event.pos[0]>1150 and event.pos[1]>208 and event.pos[0]<1330 and event.pos[1]<388 and mur == 'ext':
                    if item8:
                        if fenetre('un aimant est acroché au mur\n le prendre?', 'aimant', 'oui', 'non', 'obtenu: aimant', 'ok')== 'yes':
                            item3=True
                            son_objet=pygame.mixer.Sound(b'prendre_objet.wav')
                            son_objet.play()
                        vue_exterieur(item3)
                    else: fenetre("un aimant est acroché au mur\n mais il est trop loin \n vous ne pouvez pas l'atraper", 'aimant', '', '', '', '')
                if event.pos[0]>945 and event.pos[1]>440 and event.pos[0]<945+65 and event.pos[1]<440+150 and mur == 'drt' and csr==False and item7==False:
                    if fenetre("un mareau est dans ce casier\n le prendre?", 'mareau', 'oui', 'non', 'obtenu: marteau', 'ok')== 'yes':
                        item7=True
                        son_objet=pygame.mixer.Sound(b'prendre_objet.wav')
                        son_objet.play()
                        mur_droit(csr, item7, item11)
                if event.pos[0]>825 and event.pos[1]>30 and event.pos[0]<450+825 and event.pos[1]<600+30 and mur == 'drt' and csr:
                    if code:
                        if fenetre("ce casier est fermé\n l'ouvrir?", 'casier', '6174', 'code', 'le casier est ouvert', 'code mauvais')== '6174':
                            csr=False
                            son_casier=pygame.mixer.Sound(b'casier.wav')
                            son_casier.play()
                            mur_droit(csr, item7, item11)
                    else: fenetre("ce casier est fermé\n Il nessecite un code", 'casier', '', '', '', '')
                if event.pos[0]>100 and event.pos[1]>300 and event.pos[0]<100+600 and event.pos[1]<300+400 and mur == 'gch' and not item10:
                    if fenetre("ce burreau possede des tirroirs\n les fouiller?", 'bureau', 'oui', 'non', "dans l'un des tirroir, vous trouvez une clé", 'ok')== 'yes':
                        item10=True
                        son_tirroire=pygame.mixer.Sound(b'tirroire.wav')
                        son_tirroire.play()
                        son_objet=pygame.mixer.Sound(b'prendre_objet.wav')
                        son_objet.play()                   
                        mur_gauche(fxmur, item8, item10)
                if event.pos[0]>100 and event.pos[1]>300 and event.pos[0]<100+600 and event.pos[1]<300+400 and mur == 'drt' and not item11:
                    if item10:
                        if fenetre("cette commode possede des tirroirs\n les fouiller?", 'commode', 'oui', 'non', "vous trouvez un bout de papier avec plein de chiffres dessus", 'ok')== 'yes':
                            item11=True
                            son_tirroire=pygame.mixer.Sound(b'tirroire.wav')
                            son_tirroire.play()
                            mur_droit(csr, item7, item11)
                        else:fenetre("cette commode possede des tirroirs\n mais ils nessecitent une clé pour les ouvrirs", 'commode', '', '', "", '')
                if event.pos[0]>781 and event.pos[1]>190 and event.pos[0]<781+90 and event.pos[1]<190+210 and mur == 'gch' and fxmur==False and item8==False:
                    if fenetre("il y a une pince dans le trou\n la prendre ?", 'pince', 'oui', 'non', 'obtenu: pince', 'ok')== 'yes':
                        item8=True
                        son_objet=pygame.mixer.Sound(b'prendre_objet.wav')
                        son_objet.play()
                        mur_gauche(fxmur, item8, item10)
                if event.pos[0]>781 and event.pos[1]>190 and event.pos[0]<781+90 and event.pos[1]<190+210 and mur == 'gch' and item7 and fxmur:
                    if fenetre("il semble que cette partie du mur ressorte \n le casser avec le marteau?", 'faux mur', 'oui', 'non', 'faux mur cassé', 'ok')== 'yes':
                        fxmur=False
                        son_detruit=pygame.mixer.Sound(b'detruit.wav')
                        son_detruit.play()
                        mur_gauche(fxmur, item8, item10)
                if event.pos[0]>1050 and event.pos[1]>165 and event.pos[0]<1050+80 and event.pos[1]<165+110 and mur == 'avt' and item3:
                    if fenetre("il semble qu'une boîte de biscuits pour chien métalique soie posée sur le bureau du gardien\n utiliser l'aimant pour l'atraper", 'biscuits', 'oui', 'non', 'obtenu: boîte de biscuits pour chien', 'ok')== 'yes':
                        item9=True
                        son_objet=pygame.mixer.Sound(b'prendre_objet.wav')
                        son_objet.play()
                        biscits=False
                        mur_avant(cht, biscits, door)
                if event.pos[0]>800 and event.pos[1]>150 and event.pos[0]<1125 and event.pos[1]<800 and mur == 'avt' and item5 and door:
                    if fenetre("Vous avez les clés de la porte.\nL'ouvrir?", 'porte', 'oui', 'non', 'la porte est maitenant ouverte', 'ok')== 'yes':
                        door=False
                        son_porte=pygame.mixer.Sound(b'porte_cellule.wav')
                        son_porte.play()
                        mur_avant(cht, biscits, door)
                if event.pos[0]>-100 and event.pos[1]>300 and event.pos[0]<-100+800 and event.pos[1]<300+450 and mur == 'avt' and item9:
                    if fenetre("le chien semble avoir des clés attaché à son colié\n lui donner les buscuit?", 'chien', 'oui', 'non', 'obtenu: clés de la cellule', 'ok')== 'yes':
                        item5=True
                        cht=False
                        item9=False
                        son_objet=pygame.mixer.Sound(b'prendre_objet.wav')
                        son_objet.play()
                        son_chien=pygame.mixer.Sound(b'chien.wav')
                        son_chien.play()
                        mur_avant(cht, biscits, door)
                if event.pos[0]>15 and event.pos[1]>685 and event.pos[0]<85 and event.pos[1]<755 and item1:
                    son_papier=pygame.mixer.Sound(b'papier.wav')
                    son_papier.play()
                    fenetre("c'est un vieux papier\n il a l'air d'être là depuis longtemps \n le lire?", 'papier froissé', 'oui', 'non', "Vous lisez le papier:\na tous le monde qui passe après moi, sachez que j'écris avant de devenir fou, j'ai caché un aimant dehors hors de porté bonne chance si vous l'atrapez hahahah!", 'ok')
                if event.pos[0]>15+10*90 and event.pos[1]>685 and event.pos[0]<85+10*90 and event.pos[1]<755 and item11:
                    son_papier=pygame.mixer.Sound(b'papier.wav')
                    son_papier.play()
                    fenetre("ce papier est remplis de chiffres dont certains sont entourés\n vous les mettez bout-à-bout et cela forme un code 6174", 'papier plein de chiffres', '', '', "", '')
                    code=True
                if event.pos[0]>500 and event.pos[1]>250 and event.pos[0]<500+1000 and event.pos[1]<250+200 and not door and mur=='avt' and not item12:
                    if fenetre("Ce burreau est celui du gardien\nL'ouvrir?", 'burreau', 'oui', 'non', 'obtenu: clé rouillé', 'ok')== 'yes':
                        son_objet=pygame.mixer.Sound(b'prendre_objet.wav')
                        son_objet.play()
                        son_tirroire=pygame.mixer.Sound(b'tirroire.wav')
                        son_tirroire.play()
                        item12=True
                if event.pos[0]>175 and event.pos[1]>75 and event.pos[0]<175*2 and event.pos[1]<75+350 and not door and mur=='avt' and item12:
                    if fenetre("ceci est la porte de sortie\nL'ouvrir?", 'porte de sortie', 'oui', 'non', 'Félicitation vous vous êtes échapés', 'ok')== 'yes':
                        ecran.fill(noir)
                        ecran.blit(win,(0,0))
                        pygame.display.flip()
                        time.sleep(5)
                        done=True
        ecran.blit(inventaire,(0,665))
        j=15
        for i in range(0,15):
            ecran.blit(item_slot,(j,685))
            if j==15 and item1 :
                ecran.blit(enigme1,(j,685))
            if j==105 and item2:
                ecran.blit(enigme2,(j,685))
            if j==195 and item3:
                ecran.blit(aimant,(j,685))
            if j==285 and item4:
                ecran.blit(lime,(j,685))
                lim = False
            if j==375 and item5:
                ecran.blit(cle,(j,685))
            if j==465 and item6:
                ecran.blit(barreau2,(j,685))
            if j==465+90 and item7:
                ecran.blit(marteau2,(j,685))
            if j==465+(2*90) and item8:
                ecran.blit(pince2, (j,685))
            if j==465+(3*90) and item9:
                ecran.blit(biscuits2,(j,685))
            if j==465+(4*90) and item10:
                ecran.blit(clé2,(j,685))
            if j==465+5*90 and item11:
                ecran.blit(enigme1,(j,685))
            if j==465+6*90 and item12:
                ecran.blit(cle3,(j,685))
            j += 90
        pygame.display.flip()
    print('fin')
    pygame.quit()
    sys.exit()

item1= False
item2= False
item3= False
item4= False
item5= False
item6= False
item7= False
item8= False
item9= False
item10= False
item11= False
item12= False

main(mur, item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12)

ecran.fill(noir)            
ecran.blit(win,(0,0))
pygame.display.flip()
