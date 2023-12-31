from fighter import Fighter
from weapon import Weapon
from my_queue import Queue

class FighterManager :
    
    def __init__(self):
        self._fighters = []
        self._weapons = []
        
    def create_fighter(self,name,description=''):
        f = Fighter(name,description)
        self._fighters.append(f)
        return f
    
    def create_weapon(self,name,description='',damage=8,weight=2):
        w = Weapon(name,description,damage,weight)
        self._weapons.append(w)
        return w
    
    def create_fight(self,combattant,combattu):
        if combattant.get_healthPoints() > 0:
            combattant.attack(combattu)
            print('pv de',combattu,combattu.get_healthPoints())
            return self.create_fight(combattu,combattant)
        else:
#             self._fighters.remove(combattant)
            return combattu
    
    def do_tounament(self):
        file = Queue()
        for element in self._fighters:
            file.enqueue(element)
        while not file.size() == 1:
            tant = file.dequeue()
            ttu = file.dequeue()
            self.create_fight(tant,ttu)
            
    
marcel = Fighter('Marcel', 'The best one') # on instancie avec les variables de la méthode __init__
Yves_cadour = Fighter('Yves', 'NSI chef') # on instancie avec les variables de la méthode __init__ 