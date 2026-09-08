# # basic class
# class TestClass:
#   test_attr = 'hello world!'
#   another_attr = [1,2,3]

#   def test_method(self):
#     print('meth in class')
#     print(self.test_attr)
#     self.another_method('123')

#   def another_method(self, test_param: str):
#     print(test_param)

# # create instance
# test = TestClass()
# print(test.test_attr)
# test.another_attr = 'new val'
# print(test.another_attr)

# another_test = TestClass()
# print(another_test.another_attr)
# print(another_test.test_attr)

# another_test.test_attr = 'a new string!'
# another_test.test_method()

# another_test.another_method("this is a parameter")

# # mage class
# class Mage:
#   def __init__(self, health: int, mana: int):
#     self.health = health
#     self.mana = mana
#     print('mage class was created')
#     print(self.health)
#     print(self.mana)

#   def attack(self, target):
#     target.health -= 10

# class Monster:
#   health = 40

# mage = Mage(100, 200)
# monster = Monster()

# print(monster.health)
# mage.attack(monster)
# print(monster.health)

# inheritance
# class Human:
#   def __init__(self, name:str="Human", health:float = 25, damage:float = 1, defense:float = 0):
#     self.name = name
#     self.health = health
#     self.damage = damage
#     self.defense = defense

#   def attack(self, target:Human)->None:
#     target.health -= round(self.damage - target.defense, 2)
#     print(f'{self.name} attacked for {round(self.damage - target.defense, 2)} on {target.name}')

# class Warrior(Human):
#   def __init__(self, name:str="Warrior", health:float=25, defense:float=2.5, damage:float=1.5):
#     super().__init__(name=name, health=health, defense=defense, damage=damage)


# class Barbarian(Human):
#   def __init__(self, name:str="Barbarian", health:float=25, damage:float=5, defense:float=0):
#     super().__init__(name=name, health=health, damage=damage, defense=defense)

# warrior = Warrior(health=50, defense=5.5)
# barbarian = Barbarian(health=100, damage=8.8)

# print(f'{warrior.name}, health: {warrior.health}. defense: {warrior.defense}. damage: {warrior.damage}')
# print(f'{barbarian.name}, health: {barbarian.health}. defense: {barbarian.defense}. damage: {barbarian.damage}')
# barbarian.attack(warrior)
# warrior.attack(barbarian)
# print(f'{warrior.name}, health: {warrior.health}. defense: {warrior.defense}. damage: {warrior.damage}')
# print(f'{barbarian.name}, health: {barbarian.health}. defense: {barbarian.defense}. damage: {barbarian.damage}')

# # practice
# class Entity:
#   def attack(self)->None:
#     print(f'attack with {self.damage} damage')

# class Monster(Entity):
#   def __init__(self, health:float=50, damage:float=7.5):
#     self.health = health
#     self.damage = damage

#   def __repr__(self):
#     return f'a monster with {self.health} hp'

# monster = Monster(100, 10)
# print(monster.health)
# monster.attack()
# print(monster)