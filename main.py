from Player import *
from monsters import *
from livewires import games, color
from Tkinter import *
from random import randint

class dd59(Frame):
    def __init__(self, master):
	Frame.__init__(self)
        self.grid()
        self.species = StringVar()
        self.species.set(None)
        self.Image = "hero.jpg"
        self.x = 100
        self.y = 260
        self.lbl = Label(self)
        self.lbl["text"] = "Choose Your Hero"
        self.lbl.grid()
        
        self.sir = Radiobutton(self, text = "Knight",
                               variable = self.species,
                               value = "Knight").grid()

        self.cler = Radiobutton(self, text = "Cleric",
                                variable = self.species,
                                value = "Cleric").grid()

        self.thief = Radiobutton(self, text = "Thief",
                                 variable = self.species,
                                 value = "Thief").grid()
        
        self.hero = Radiobutton(self, text = "Hero",
                              variable = self.species,
                              value = "Hero").grid()
        
        self.redDragon = Radiobutton(self, text = "Red Dragon",
                                     variable = self.species,
                                     value = "Red Dragon").grid()
        
        self.whiteDragon = Radiobutton(self, text = "White Dragon",
                                       variable = self.species,
                                       value = "White Dragon").grid()

        self.goblin = Radiobutton(self, text = "Goblin",
                                  variable = self.species,
                                  value = "Goblin").grid()
        
        self.bttn = Button(self, text = "ok", command = self.set_char).grid()
            
    def set_char(self):
        if self.species.get() == "Thief":
            user = Thief("Edward")
            self.get_stats(user)
            
        elif self.species.get() == "Cleric":
            user = Cleric("flames")
            self.get_stats(user)
            
        elif self.species.get() == "Knight":
            user = Knight("sir")
            self.get_stats(user)

        elif self.species.get() == "Hero":
            user = Player("Bob")
            self.get_stats(user)

        elif self.species.get() == "Red Dragon":
            user = Red_Dragon("spitty")
            self.get_stats(user)

        elif self.species.get() == "White Dragon":
            user = White_Dragon("flappy")
            self.get_stats(user)

        elif self.species.get() == "Goblin":
            user = Goblin("grouchy")
            self.get_stats(user)

    def get_stats(self, user):
        self.x = user.x
        self.y = user.y
        self.Image = user.Image
        self.main(user)
        
    def main(self, user):
        games.init(screen_width = 640, screen_height = 480, fps = 50)
        music = games.music.load("audio/background.mp3")
        games.music.play()
        wall_image = games.load_image("images/background.jpg",transparent = False)
        games.screen.background = wall_image

        choice = randint(0,2)
        if choice == 0:
            enemy = Red_Dragon("screechy")
        elif choice == 1:
            enemy = White_Dragon("Frosty")
        else:
            enemy = Goblin("shorty")

        user_health = games.Text(value = "health: " + str(user.health),
                                 size = 40,
                                 color = color.red,
                                 x = 75,
                                 y = 20)
       
        enemy_health = games.Text(value = "health: " + str(enemy.health),
                                   size = 40,
                                   color = color.red,
                                   x = 550,
                                   y = 20)
        games.screen.add(user_health)
        games.screen.add(enemy_health)
        
        character = player(user, enemy, user_health, enemy_health)
        games.screen.add(character)
        
        attacker = opponent(user, enemy)
        games.screen.add(attacker)

        games.screen.mainloop()
            
class player(games.Sprite):
    def __init__(self, user, enemy, user_health, enemy_health):
        self.user = user
        self.enemy = enemy
        self.userHealth = user_health
        self.enemyHealth = enemy_health
        Image = games.load_image(user.Image)
        super(player, self).__init__(image = Image, x = user.x, y = user.y)
        self.DELAY = 200
        self.delay = 0
        self.attacked = False
        self.left = False
        self.XPOS = self.x
        self.shake = False
        self.count = 10
        
    def update(self):
        choice = randint(0,1)
        
        if self.delay > 0:
            self.delay -= 1
            
        if games.keyboard.is_pressed(games.K_a) and self.both_alive and self.delay == 0:
            self.enemyHP = self.enemy.health
            self.user.attack(self.enemy)
            self.delay = self.DELAY
            damage = self.enemyHP - self.enemy.health
            self.loss(damage, self.enemy.enemyX, self.enemy.enemyY)
            self.attacked = True
            self.commentary(self.user.action, self.delay)
            self.enemy.shake = True
            self.attackSound = games.load_sound(self.user.sound)
            self.attackSound.play()
            
        if games.keyboard.is_pressed(games.K_s) and self.both_alive and self.delay == 0:
            self.enemyHP = self.enemy.health
            self.user.special(self.enemy)
            self.delay = self.DELAY
            damage = self.enemyHP - self.enemy.health
            self.loss(damage, self.enemy.enemyX, self.enemy.enemyY)
            self.attacked = True
            self.commentary(self.user.action, self.delay)
            self.enemy.shake = True
            self.attackSound = games.load_sound(self.user.sound)
            self.attackSound.play()
            
            
        if self.both_alive and self.attacked:
            if self.delay == 0:
                self.userHP = self.user.health
                if choice == 0:
                    self.enemy.attack(self.user)
                else:
                    self.enemy.special(self.user)
                damage = self.userHP - self.user.health
                self.loss(damage, self.user.x, self.user.y)
                attackSound = games.load_sound(self.enemy.sound)
                attackSound.play()
                self.attacked = False
                self.delay = self.DELAY
                try:
                    action2 = self.enemy.action2
                except:
                    action2 = ""
                self.commentary(self.enemy.action, self.delay, action2)
                self.shake = True
                
        if self.shake:
            self.count -= 1
            if self.count >= 0:
                if self.left:
                    self.x += 10
                    if self.x == self.XPOS - 100:
                        self.left = True
                else:
                    self.x -= 10
                    if self.x == self.XPOS + 100:
                        self.left = False
            else:
                self.shake = False
                self.count = 10
                
        if games.keyboard.is_pressed(games.K_F1):
            self.txt = games.Message(value = "a = attack      "
                                     +"s = special        "
                                     +"F1 = help       "
                                     +"ESC = exit",
                                     size = 25, color = color.white,
                                     x = games.screen.width/2,
                                     y = games.screen.height -20,
                                     lifetime = 250)
            games.screen.add(self.txt)

        if games.keyboard.is_pressed(games.K_ESCAPE):
            self.quit()
    
        if self.user.alive:
            self.userHealth.value = "health: " + str(self.user.health)
        else:
            self.userHealth.value = "Dead"
            self.end_game("You lost")

        if self.enemy.alive:
            self.enemyHealth.value = "health: " + str(self.enemy.health)
        else:
            self.enemyHealth.value = "Dead"
            self.end_game("You Won!")
    @property   
    def both_alive(self):
        if self.user.alive and self.enemy.alive:
            return True        

    def loss(self, damage, x, y):
        damage = -damage
        lost = games.Message(value = str(damage), size = 50, color = color.red,
                             x = x, y = y, dy = -1, lifetime = 250)
        games.screen.add(lost)
        
    def commentary(self, value, delay, value2 = ""):
        self.action = games.Message(value = value,size = 25,
                                    color = color.white,
                                    x = games.screen.width/2,
                                    y = games.screen.height - 35,
                                    lifetime = delay)
        games.screen.add(self.action)
        if value2 != "":
            self.action2 = games.Message(value = value2,size = 25,
                                    color = color.white,
                                    x = games.screen.width/2,
                                    y = games.screen.height - 20,
                                    lifetime = delay)
            games.screen.add(self.action2)
            
    def end_game(self, status):
        end_message = games.Message(value = status, size = 75,color = color.red,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    lifetime = 5 * games.screen.fps,
                                    after_death = games.screen.quit)
        games.screen.add(end_message)
        games.music.stop()

class opponent(games.Sprite):
    def __init__(self, user, enemy):
        self.user = user
        self.enemy = enemy
        Image = games.load_image(enemy.Image)
        super(opponent, self).__init__(image = Image, x = enemy.enemyX,
                                       y = enemy.enemyY)
        self.count = 10

    def update(self):
        if self.enemy.shake:
            self.count -= 1
            if self.count >= 0:
                if self.count % 2 == 0:
                    self.x += 10
                else:
                    self.x -= 10
            else:
                self.enemy.shake = False
                self.count = 10


root = Tk()
root.title("Frame")
root.geometry("400x300")
app = dd59(root)
root.mainloop()
