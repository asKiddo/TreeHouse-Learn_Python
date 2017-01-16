import sys

from character import Character
from monster import Dragon
from monster import Goblin
from monster import Troll


class Game:
    def setup(self):
        self.player = Character()
        self.monsters = [
            Goblin(),
            Troll(),
            Dragon()
        ]
        self.monster = self.get_next_monster()
        
    def get_next_monster(self):
        try:
            return self.monsters.pop(0)
        except IndexError:
            return None
        
    def monster_turn(self):
        if self.monster.attack():
            print("The {} is attacking you!".format(self.monster))
            if input("Dodge? (Y/N) ").lower() == 'y':
                if self.player.dodge():
                    print("Dodge worked!")
                else:
                    print("Too slow, it got you!")
                    self.player.hp -= 1
            else:
                print("{} hit you for 1 point.".format(self.monster))
                self.player -= 1
        else:
            print("{} isn't attacking this turn".format(self.monster))
        
    def player_turn(self):
        player_choice = input("[A]ttack, [R]est, [Q]uit: ").lower()
        if player_choice == 'a':
            print("You're attacking {}".format(self.monster))
            if self.player.attack():
                if self.monster.dodge():
                    print("The {} dodged!".format(self.monster))
                else:
                    if self.player.leveled_up():
                        self.monster.hp -= 2
                    else:
                        self.monster.hp -= 1
                
                    print("You hit {} with your {}".format(self.monster, self.player.weapon))
            else:
                print("You missed!")
        elif player_choice == 'r':
            print("You rested to heal.")
            self.player.rest()
        elif player_choice == 'q':
            print("Thanks for playing...")
            sys.exit()
        else:
            self.player_turn()
        
    def cleanup(self):
        if self.monster.hp <= 0:
            self.player.exp += self.monster.exp
            print("You killed {}!".format(self.monster))
            self.monster = self.get_next_monster()
    
    def __init__(self):
        self.setup()
        
        while self.player.hp and (self.monster or self.monsters):
            print('\n'+'='*20)
            print(self.player)
            self.monster_turn()
            print('-'*20)
            self.player_turn()
            self.cleanup()
            print('\n'+'='*20)
        
        if self.player.hp:
            print("You win!")
        elif self.monster or self.monsters:
            print("You lose!")
        else:
            print("It was too close to call!")
        sys.exit()
        

Game()