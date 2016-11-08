from Tkinter import *
import webbrowser
import time
import time
times=0
current_turn = False
def write(content):
    output.configure(state='normal')
    output.delete('1.0',END)
    output.insert(END,content)
    output.configure(state='disabled')
def turn():
    global current_turn
    if lets_battle(player1,player2) == player1.name:
        write('Player 1 has won!           Make a choice')
        current_turn=player1
    elif lets_battle(player1,player2) == player2.name:
        write('Player 2 has won!           Make a choice')
        current_turn=player2
    elif lets_battle(player1,player2) == False:
        write('Tie! Try again')
        current_turn = False
select = 0

class player:
    def __init__(self,name):
        self.name = name

    def attackarino(self,player,place):
        global select
        self.opponent.lives -= select.attack
        if self.opponent.lives < 1:
            write('GGGGGG!!!!!!                ' + current_turn.name + 'wins')
        place.destroy()
        damage(self.opponent)
        current_turn = False
    def sel(self, player,yolo):
        opposition = Button(yolo, text=current_turn.opponent.name, command = lambda: self.attackarino(player,yolo))
        opposition.pack()
class building:
    def __init__(self, attack, health, name, upgrade, blocking, middle):
        self.name = name
        self.attack = attack
        self.health = health
        self.upgrade = upgrade
        self.blocking = blocking
        self.middle = middle
    def checkup(self, player):
        for same in range(3):
            for b in player.inventory:
                if player.inventory.count(b) > 1:
                    if b.upgrade != False:
                        player.inventory[:] = (value for value in player.inventory if  value != b)
                        player.inventory.append(b.upgrade)
                        break
                
    def add_to(self, player,place):

        global current_turn
        current_turn.inventory.append(self)
##        self.checkup(current_turn)
        current_turn = False
        place.destroy()

    def makeButton(self, place, player):
        asdf = Button(place, text=self.name,command = lambda: self.add_to(player,place))
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
        write('Choose who you want to      attack')
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
        if self.health < 1:
            player.opponent.inventory.remove(self)
        place.destroy()
        current_turn = False
    def forGlory(self, place, player):
        global current_turn
        asdf = Button(place, text=self.name,command = lambda: self.attackarino(player,place))
        asdf.pack()

class rocker:
    def __init__(self,name):
        self.name = name
#############################
# BUILDINGS
#############################
triple_gun = building(3,1,'triple gun', False, False, False)
gun = building(1,1, 'gun', triple_gun, False, False)

flag = building(0,1,'flag', False,True, False)

minigun = building(4,3,'minigun',False,False,False)
machinegun = building(2,3,'machinegun',minigun,False,True)
starting_machinegun = building(0,3,'starting machinegun',machinegun,False,False)

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

weapons = [gun,flag, starting_machinegun]

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
    write('Welcome to The Box Game!!!  Press help for instructions,otherwise enjoy your stay!')
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
        write('Choose what you want to     attack with')
        whoyouwannakill = Toplevel()
        for a in current_turn.inventory:
            if a != flag:
                a.prep(whoyouwannakill, current_turn)
            
        
def build():
    global current_turn, weapons
    if current_turn != False:
        write('Choose something to build orupgrade')
        buildings = Toplevel()
        for a in weapons:
            if a.upgrade != False:
                if current_turn.inventory.count(a) >0:
                    a.upgrade.makeButton(buildings,current_turn)
                    current_turn.inventory.remove(a)
                elif current_turn.inventory.count(a.upgrade)>0:
                    pass
                else:
                    a.makeButton(buildings,current_turn)
            else:
                a.makeButton(buildings,current_turn)

        for a in current_turn.inventory:
            if weapons.count(a) == 0:
                a.upgrade.makeButton(buildings,current_turn)
                current_turn.inventory.remove(a)
    
    
def damage(player):
    left = 9 - player.lives
    base = 30
    if player.name == 'player1':
        for a in range(1,4):
            for b in range(1,4):
                if left > 0:
                    playing_field.create_rectangle(a*base,b*base,a*base+base,b*base+base,fill='red')
                    left -=1
    else:
        for a in range(6,9):
            for b in range(1,4):
                if left > 0:
                    playing_field.create_rectangle(a*base,b*base,a*base+base,b*base+base,fill='red')
                    left-=1

def player_lives():
    base = 30
    for a in range(1,4):
        for b in range(1,4):
            playing_field.create_rectangle(a*base,b*base,a*base+base,b*base+base)

    for a in range(6,9):
        for b in range(1,4):
            playing_field.create_rectangle(a*base,b*base,a*base+base,b*base+base)

player2 = player('player2')
player1 = player('player1')
player1.opponent = player2
player2.opponent = player1
player1.inventory = []
player2.inventory = []
player1.choice = ''
player2.choice = ''
player1.lives = 9
player2.lives = 9


root = Tk()
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

game_menu = Frame(root)
game_menu.grid(row=1,column=2,sticky=NW)

playing_field = Canvas(game_menu, height=150,width=300)
playing_field.grid(row=1,column=1,sticky=NW)

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
output = Text(rps, state='disabled', height=7,width=28)
output.grid(columnspan=100,row=3,sticky=NW)

root.mainloop()

