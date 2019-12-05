# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    '''
    This is an Player class with attributes:
    name, currentRoom
    '''
    def __init__(self, name, currentRoom):
        self.name = name
        self.currentRoom = currentRoom

    def __str__(self):
         return f'Hi, {self.name} You are in {self.currentRoom}'

 