import random
class Monster(object):
    def __init__(self,name):
        self.name = name
        self.alive = True
        self.gold = 100
        self.health = random.randint(3,12)
        self.action = ""
    def __str__(self):
        return self.name + " has " + str(self.health) + " health"
        if not self.alive:
            print(enemy.name + " has met the end of his days")
    def attack(self, enemy):
        enemy.get_hurt(random.randint(1,6))
        if enemy.health % 3 == 0:
            self.action = self.name + " charged at " + enemy.name
            self.action += " with a psychotic look in his eye. "
            self.action2 = "he trips and his sword bounces into " 
            self.action2 += enemy.name + "'s shoulder"
        elif enemy.health % 3 == 1:
            self.action = self.name + " pokes " + enemy.name
        else:
            self.action = enemy.name + " blocked " + self.name
            self.action2 = self.name + " punches " + enemy.name + " right in the face"
            
    def get_hurt(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            self.alive = False

class Red_Dragon(Monster):
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.shake = False
        self.health = random.randint(15,30)
        self.Image = "images/red_dragon.jpg"
        self.sound = "audio/dragon_roar.wav"
        self.x = 120
        self.y = 200
        self.enemyX = 500
        self.enemyY = 200
        
    def special(self, enemy):#fire breath
        enemy.get_hurt(random.randint(6,12))
        self.action = "The dragon spits a fiery terror engalfing the field,"
        self.action2 = enemy.name + "'s helmet spun around and he walked"
        self.action2 += " into a patch of fire"

class White_Dragon(Red_Dragon):
    def __init__(self, name):
        super(White_Dragon, self).__init__(name)
        self.Image = "images/white_dragon.jpg"
        self.sound = "audio/dragon_attack.wav"
        self.x = 150
        self.y = 200
        self.shake = False
        self.enemyX = 450
        self.enemyY = 200
    
    def special(self, enemy):#ice breath
        enemy.get_hurt(random.randint(2,8))
        self.action = "The ice crystals rain from above tearing everything in its path,"
        self.action2 = "as the almighty white dragon soars the skies."

class Goblin(Monster):
    def __init__(self, name):
        super(Goblin, self).__init__(name)
        self.health = random.randint(1,8)
        self.Image = "images/goblin.jpg"
        self.sound = "audio/goblin_attack.wav"
        self.x = 100
        self.y = 310
        self.shake = False
        self.enemyX = 500
        self.enemyY = 310
        
    def attack(self, enemy):
        enemy.get_hurt(random.randint(1,6))
        self.action = self.name + " ferociously waddles over to " + enemy.name
        self.action2 = "climbs up his body, scratches at his face, "
        self.action2 += "and bites his nose."
        
    def special(self, enemy):#scream
        self.action = self.name + " releases a wretched screech,"
        self.action2 = enemy.name + " rips off his own ears to release himself from the pain."
        enemy.get_hurt(3)
