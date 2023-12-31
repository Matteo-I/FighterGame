from random import randrange , uniform
from weapon import Weapon

class Fighter:
    """
    La classe d'un fighter
    """
    def __init__(self, name, description):
        v = randrange(1,9)
        self._name = name
        self._description = description
        self._agility = v
        self._strenght = 10-v
        self._healthPoints = 100 # Lors de la création d'une instance, les points de vie valent 100.
        self._equipedWeapon = None
    
    def __repr__(self):
            """
            methode spe qui represente le fighter
            """
            return self.get_name()
            
    def get_name(self):
        """
        Retourne le nom du combattant.
        """
        return self._name
    
    def get_description(self):
        """
        Retourne la description du combattant.
        """
        return self._description
    
    def set_description(self, description):
        """
        Affecte la description du combattant.
        
        """
        self._description=description
    
    def get_agility(self):
        return self._agility
    
    def get_healthPoints(self):
        return self._healthPoints
    
    def get_strenght(self):
        return self._strenght
    
    def get_equipedWeapon(self):
        return self._equipedWeapon
    
    #def set_weapon(self,weapon):
        #self._equipedWeapon = weapon
    
    def take_weapon(self,weapon):
        if self.get_equipedWeapon() == None and weapon.get_owner() == 'none':
            self._equipedWeapon = weapon
            weapon._owner = self
            self._agility -= weapon.get_weight()
            if self.get_agility() < 1:
                self._agility = 1
        else:
            if self.get_equipedWeapon() == 'none':
                print("cette arme est deja equiper par quelqu'un d'autre")
            else:   
                print(self.get_name(),'a deja une arme equiper :')
        return self.get_equipedWeapon()
            
    
    def punch(self,fighter):
       '''
        permet au fighter a de punch un fighter b
        calcule la vie perdu du fighter b en fonction de la force du fighter a et de l'agilité du fighter b et d'un peu d'aleatoire
        '''
       points=int(uniform(0.7,1.0)*10+self.get_strenght()/fighter.get_agility())
       fighter._healthPoints-=points
       print(self,'a punch',fighter)
       return fighter._healthPoints
    
    def attack(self,fighter):
        if self.get_equipedWeapon() != None and self.get_equipedWeapon().get_ammos() > 0 :
            self.get_equipedWeapon().shoot(fighter)
        else:
            self.punch(fighter)
        return fighter._healthPoints
            
    def summary(self):
        summary = 'Nom:'+ self.get_name() + '\n' + 'Description:'+ self.get_description() + '\n' + 'Points de vie:' + str(self.get_healthPoints()) + '\n' + 'Agilité:' + str(self.get_agility()) + '\n' + 'Force:' + str(self.get_strenght()) + '\n' + 'Arme:'+ self.get_equipedWeapon()
        return summary

bow_of_light = Weapon('Bow of light','arc de zelda',10,1)
marcel = Fighter('Marcel', 'The best one') # on instancie avec les variables de la méthode __init__
Yves_cadour = Fighter('Yves', 'NSI chef') # on instancie avec les variables de la méthode __init__ 