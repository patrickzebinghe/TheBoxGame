from Tkinter import *
import webbrowser
import time
import winsound
times=0
current_turn = False
turns=0
root = Tk()
game_menu = Frame(root)
game_menu.grid(row=1,column=2,sticky=NW)

playing_field = Canvas(game_menu, height=500,width=500)
playing_field.grid(row=1,column=1,sticky=NW)
def write(content):
    output.configure(state='normal')
    output.delete('1.0',END)
    output.insert('1.0',content)
    output.configure(state='disabled')
def turn():
    global current_turn
    if lets_battle(player1,player2) == player1.name:
        write('Player 1 has won! Make a choice')
        current_turn=player1
    elif lets_battle(player1,player2) == player2.name:
        write('Player 2 has won! Make a choice')
        current_turn=player2
    elif lets_battle(player1,player2) == False:
        write('Tie! Try again')
        current_turn = False
select = 0



class player:
    def __init__(self,name,building_spots):
        self.name = name
        self.building_spots = building_spots
    def attackarino(self,player,place):
        global select
        self.opponent.lives -= select.attack
        select.aud(select.audio)
        if self.opponent.lives < 1:
            write('GGGGGG!!!!!' + player.name + 'wins')
        place.destroy()
        damage(self.opponent)
        current_turn = False
    def sel(self, player,yolo):
        opposition = Button(yolo, text=current_turn.opponent.name, command = lambda: self.attackarino(player,yolo))
        opposition.pack()
class building:
    def __init__(self, attack, health, name, upgrade, blocking, middle, photo, tree,audio):
        self.name = name
        self.attack = attack
        self.health = health
        self.upgrade = upgrade
        self.blocking = blocking
        self.middle = middle
        self.photo = photo
        self.tree = tree
        self.audio = audio
    def checkup(self, player):
        for same in range(3):
            for b in player.inventory:
                if player.inventory.count(b) > 1:
                    if b.upgrade != False:
                        player.inventory[:] = (value for value in player.inventory if  value != b)
                        player.inventory.append(b.upgrade)
                        break
                
    def add_to(self, player,place,weap):

        global current_turn,playing_field
        current_turn.inventory.append(self)
        
        if weap != False:
            current_turn.inventory.remove(weap)
            for a in current_turn.building_spots:
                if a[2] == True:
                    if a[3] == weap:
                        a[2] = False
                        playing_field.delete(a[4])
                        a.remove(a[4])
                        a.remove(a[3])
                        
                    
                    
        for a in player.building_spots:
            if a[2] == False:
                a[2] = True
                a.append(self)
                a.append(playing_field.create_image(a[0],a[1],image=self.photo))
                break
       
        
##        self.checkup(current_turn)
        write(self.name + ' has been added to ' + current_turn.name + "'s inventory")
        current_turn = False
        place.destroy()

    def makeButton(self, place, player,weap):
        asdf = Button(place, text=self.name,command = lambda: self.add_to(player,place,weap))
        asdf.pack()
    def prep(self, place, player):
        asdf = Button(place, text=self.name,command = lambda: self.selection(player,place))
        asdf.pack()
    def checkblock(self,player):
        blockers = 0
        for building in player.inventory:
            if building.blocking == True:
                blockers += 1
        if blockers > 0:
            return True
        else:
            return False
    def selection(self,player,place):
        global select,current_turn
        select = self        
        place.destroy()
        asdf = Toplevel()
        write('Choose who you want to attack')
        if self.checkblock(player.opponent):
            for a in player.opponent.inventory:
                if a.blocking == True:
                    a.forGlory(asdf,player)
        else:
            for a in player.opponent.inventory:
                a.forGlory(asdf,player)
            current_turn.sel(player,asdf)
                    
    def attackarino(self,player,place):
        global select
        self.health -= select.attack
        select.aud(select.audio)
        if self.health < 1:
            player.opponent.inventory.remove(self)
            for a in player.opponent.building_spots:
                if a[2] == True:
                    if a[3] == self:
                        a[2] = False
                        playing_field.delete(a[4])
                        a.remove(a[4])
                        a.remove(a[3])
                        break
            winsound.PlaySound(r"C:\Users\temp\Desktop\the box game\Audio\Boom HeadShot Song.wav", winsound.SND_FILENAME)

        place.destroy()
        current_turn = False
    def forGlory(self, place, player):
        global current_turn
        asdf = Button(place, text=self.name,command = lambda: self.attackarino(player,place))
        asdf.pack()
    def aud(self, audio):
        winsound.PlaySound(audio, winsound.SND_FILENAME)
class rocker:
    def __init__(self,name):
        self.name = name
#############################
# BUILDINGS
#############################

## remember attack, health, name, upgrade, blocking, middle, photo, tree

triple_gun = building(3,1,'triple gun', False, False, False,PhotoImage(file='boxGame/triple.gif'),2,r'C:\Users\temp\Desktop\the box game\Audio\triplegun.wav')
gun = building(1,1, 'gun', triple_gun, False, False,PhotoImage(file='boxGame/gun.gif'),1,r'C:\Users\temp\Desktop\the box game\Audio\gun.wav')

tripleflag = building(0,3,'triple flag', False, True, False, PhotoImage(file='boxGame/triplef.gif'),2,False)
flag = building(0,1,'flag', tripleflag,True, False,PhotoImage(file='boxGame/flag.gif'),1,False)


minigun = building(4,3,'minigun',False,False,False,PhotoImage(file='boxGame/mini.gif'),3,r'C:\Users\temp\Desktop\the box game\Audio\minigun.wav')
machinegun = building(2,3,'machinegun',minigun,False,True,PhotoImage(file='boxGame/machinegun.gif'),2,r'C:\Users\temp\Desktop\the box game\Audio\machinegun.wav')
starting_machinegun = building(0,3,'starting machinegun',machinegun,False,False,PhotoImage(file='boxGame/starting.gif'),1,False)

machinegun.base = starting_machinegun

rock = rocker('rock')
paper = rocker('paper')
scissors = rocker('scissors')

rock.weakness = paper
rock.strong = scissors
rock.tie = rock

paper.weakness = scissors
paper.strong = rock
paper.tie = paper

scissors.weakness = rock
scissors.strong = paper
scissors.tie = scissors

guns = [gun,triple_gun]
machineGuns = [starting_machinegun,machinegun,minigun]
flags = [flag]

blockingBuildings = [flag]

weapons = [guns,machineGuns,flags]

def lets_battle(p1,p2):
    global winner
    if p1.choice.strong == p2.choice:
        return player1.name
    elif p1.choice.weakness == p2.choice:
        return player2.name
    elif p1.choice == p2.choice:
        return False
    else:
        print 'someone has screwed up the game must be restarted!'
def close_frame(frame):
    for child in frame.children:
        child.configure(state='disabled')

def open_frame(frame):
    for child in frame.children:
        child.configure(state='normal')
def openIntstructions():
    webbrowser.open('http://pattyboyo.github.io/game/theboxgame')
def countdown():
    for a in range(5,0,-1):
        print str(a)
        time.sleep(1)
def playBoxGame():
    write('Welcome to The Box Game!!! Press help for instructions,otherwise enjoy your stay!')
def done(choices):
    global times
    if times%2 == 0:
        player1.choice = choices
        write('Good, now player2 choose')
    else:
        player2.choice = choices
        write('Now battle!')
    times+=1

def attack():
    global current_turn
    if current_turn != False:
        write('Choose what you want to attack with')
        whoyouwannakill = Toplevel()
        for a in current_turn.inventory:
            if blockingBuildings.count(a) == 0:
                a.prep(whoyouwannakill, current_turn)
            
        
def build():
    global current_turn, weapons
    if current_turn != False:
        write('Choose something to build orupgrade')
        buildings = Toplevel()
##        for a in weapons:
##            if a.upgrade != False:
##                if current_turn.inventory.count(a) >0:
##                    a.upgrade.makeButton(buildings,current_turn)
##                    current_turn.inventory.remove(a)
##                elif current_turn.inventory.count(a.upgrade)>0:
##                    pass
##                else:
##                    a.makeButton(buildings,current_turn)
##            else:
##                a.makeButton(buildings,current_turn)
##
##        for a in current_turn.inventory:
##            if weapons.count(a) == 0:
##                a.upgrade.makeButton(buildings,current_turn)

        for cat in weapons:
            calls = 0
            for weap in cat:
                if current_turn.inventory.count(weap) == 1:
                    if weap.upgrade != False:
                        weap.upgrade.makeButton(buildings,current_turn,weap)
                        calls += 1
            if calls == 0:
                cat[0].makeButton(buildings,current_turn,False)
                    
                    

                    
                        
    
def damage(player):
    left = 9 - player.lives
    base = 30
    d = 350
    if player.name == 'player1':
        for a in range(1,4):
            for b in range(1,4):
                if left > 0:
                    playing_field.create_rectangle(a*base,b*base+d,a*base+base,b*base+base+d,fill='red')
                    left -=1
    else:
        for a in range(6,9):
            for b in range(1,4):
                if left > 0:
                    playing_field.create_rectangle(a*base,b*base+d,a*base+base,b*base+base+d,fill='red')
                    left-=1

def player_lives():
    base = 30
    d = 350
    for a in range(1,4):
        for b in range(1,4):
            playing_field.create_rectangle(a*base,b*base+d,a*base+base,b*base+base+d)

    for a in range(6,9):
        for b in range(1,4):
            playing_field.create_rectangle(a*base,b*base+d,a*base+base,b*base+base+d)

player2 = player('player2',[[250,100,False],[250,200,False],[250,300,False]])
player1 = player('player1',[[70,100,False],[70,200,False],[70,300,False]])
player1.opponent = player2
player2.opponent = player1
player1.inventory = []
player2.inventory = []
player1.choice = ''
player2.choice = ''
player1.lives = 9
player2.lives = 9


controls = Frame(root)
controls.grid(row=1,column=1,sticky=NW)

start = Button(controls,text='play!', command=playBoxGame)
start.grid(row=1, column=1, sticky=NW)
helpMoi = Button(controls,text='help',command=openIntstructions)
helpMoi.grid(row=1,column=2,sticky=NW)

player_menu = Frame(root)
player_menu.grid(row=1,column=3,sticky=NW)

attack = Button(player_menu,text='attack',command=attack)
attack.grid(row=1,column=1,sticky=NW)

build = Button(player_menu,text='build',command=build)
build.grid(row=1,column=2,sticky=NW)



player_lives()

rps = Frame(root)
rps.grid(row=2,columnspan = 20,sticky=NW)
rps_title = Label(rps,text = 'Rock Paper Scissors')
rps_title.grid(row=1,columnspan=5)
b = Button(rps,text='battle',command=turn)
b.grid(row=2,column=1,sticky=NW)
##done = Button(rps,text='done',command=done)
##done.grid(row=2,column=2,sticky=NW)

##choice = Entry(rps)
##choice.grid(row=2,column=3,sticky=NW)
rbutton = Button(rps,text='rock',command= lambda: done(rock))
rbutton.grid(row=2,column=3,sticky=NW)

pbutton = Button(rps,text='paper',command= lambda: done(paper))
pbutton.grid(row=2,column=4,sticky=NW)

sbutton = Button(rps,text='scissors',command= lambda: done(scissors))
sbutton.grid(row=2,column=5,sticky=NW)
output = Text(rps, state='disabled', height=7,width=55)
output.grid(columnspan=100,row=3,sticky=NW)



root.mainloop()

