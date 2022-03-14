#OOP
class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name #attributes
        self.age = age
        
    def run(self):
        print('run')
        return 'done'

player1 = PlayerCharacter('Cindy', 44)
player2 = PlayerCharacter('Tom', 21)
player2.attack = 50

help(list)
# print(player2.attack)

#OOP example
class PlayerCharacter:
# Class Object Attribute    
    membership = True
    def __init__(self, name, age):
        if (self.membership):
            self.name = name #attributes
            self.age = age
        
    def run(self):
        print('run')
        return 'done'

player1 = PlayerCharacter('Cindy', 44)
player2 = PlayerCharacter('Tom', 21)
player2.attack = 50

print(player1.name)
print(player2.membership)

help(list)
# print(player2.attack)

#OOP
class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name #attributes
        self.age = age
        
    def run(self):
        print('run')
        return 'done'

player1 = PlayerCharacter('Cindy', 44)
player2 = PlayerCharacter('Tom', 21)
player2.attack = 50

help(list)
# print(player2.attack)

#OOP example
class PlayerCharacter:
# Class Object Attribute    
    membership = True
    def __init__(self, name, age):
        if (PlayerCharacter.membership):
            self.name = name #attributes
            self.age = age
        
    def shout(self):
        print(f'my name is {self.name}')


player1 = PlayerCharacter('Cindy', 44)
player2 = PlayerCharacter('Tom', 21)
player2.attack  = 50

print(player1.shout())
print(player2.shout())

help(list)
# print(player2.attack)


#OOP example
class PlayerCharacter:
# Class Object Attribute    
    membership = True
    def __init__(self, name, age):
        if (PlayerCharacter.membership):
            self.name = name #attributes
            self.age = age
        
    def shout(self):
        print(f'my name is {self.name}')

# print(f'my name is {PlayerCharacter.name}') name does not have a property or attribute of a class because it is define in our constucture function 
player1 = PlayerCharacter('Cindy', 44)
player2 = PlayerCharacter('Tom', 21)
player2.attack  = 50

print(player1.shout())
print(player2.shout())

help(list)
# print(player2.attack)



#OOP example
class PlayerCharacter:
# Class Object Attribute    
    membership = True
    def __init__(self, name, age):
        if (PlayerCharacter.membership):
            self.name = name #attributes
            self.age = age
        
    def shout(self):
        print(f'my name is {self.name}')

    def run(self, hello):
        print(f'my name is {self.name}')

player1 = PlayerCharacter('Cindy', 44)
player2 = PlayerCharacter('Tom', 21)
player2.attack  = 50

print(player1.run('hello'))
print(player2.shout())









