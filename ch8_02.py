#생성자 : 인스턴스를 만들 때 호출되는 메서드 

class Monster:
    def __init__(self, health, attack, speed):#parameter
        self.health = health
        self.attack = attack
        self.speed = speed
    def decrease_health(self,num):
        self.health -= num
    def get_health(self):
        return self.health
#고블린 인스턴스 생성 

goblin = Monster(800,200,100) #augment #instance
print(goblin)
goblin.decrease_health(100)
print(goblin.get_health())


goblin = 3 
print(type(goblin))