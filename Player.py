import random
class Player(object):
    def __init__(self,name):
        self.name = name
        self.alive = True
        self.gold = 100
        self.health = random.randint(3,12)
        self.Image = "images/hero.jpg"
        self.x = 100
        self.y = 260
        self.sound = "audio/hero_attack.wav"
        self.action = ""
    def __str__(self):
        return self.name + " has " + str(self.health) + " health"
        if not self.alive:
            print(enemy.name + " has met the end of his days")
    def attack(self, enemy):
        enemy.get_hurt(random.randint(1,6))
        if enemy.health % 3 == 0:
            self.action = self.name + " charged at " + enemy.name 
            self.action += " with a psychotic look in his eye."
            self.action2 = "he trips and his sword bounces into " 
            self.action2 += enemy.name + "'s shoulder"
        elif enemy.health % 3 == 1:
            self.action = self.name + " pokes " + enemy.name
        else:
            self.action = enemy.name + " blocked " + self.name 
            self.action2 = self.name + " punches " + enemy.name
            self.action2 += " right in the face"

    def special(self, name):
        self.action = "Humans aren't special!"
        
    def get_hurt(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            self.alive = False
            
class Cleric(Player):
    def __init__(self, name):
        super(Cleric, self).__init__(name)
        self.Image = "images/cleric.jpg"
        self.x = 100
        self.y = 280
        self.sound = "audio/cleric_attack.wav"
        
    def special(self, enemy):#heal
        self.health += random.randint(1,8)
        self.action = self.name + " takes a sip from hocus pocus"

class Knight(Player):
    def __init__(self, name):
        super(Knight, self).__init__(name)
        self.Image = "images/knight.jpg"
        self.x = 100
        self.y = 280
        self.sound = "audio/knight_attack.wav"

    def special(self, enemy):#smite
        enemy.get_hurt(random.randint(12,20))
        self.action = self.name + " bashes " + enemy.name + " with his flail" 

class Thief(Player):
    def __init__(self, name):
        super(Thief, self).__init__(name)
        self.Image = "images/thief.jpg"
        self.x = 100
        self.y = 300
        self.sound = "audio/thief_attack.wav"
        

    def special(self, enemy):#steal
        self.gold -= random.randint(1,10)
        
