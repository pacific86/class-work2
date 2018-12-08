class Restaurant():

    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        msg = self.name + " has excellent " + self.cuisine_type + "."
        print("\n" + msg)

    def open_restaurant(self):
        msg = self.name + " is open today!"
        print("\n" + msg)

greek_world = Restaurant('greek world', 'gyros')
greek_world.describe_restaurant()

bomboba = Restaurant("bomboba", 'bubble tea')
bomboba.describe_restaurant()

elephant_thai = Restaurant('elephant thai', 'pad thai')
elephant_thai.describe_restaurant()