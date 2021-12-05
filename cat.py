# Sarah Terakura
# Assignment 10.1: Your Own Class
# cat.py

# The purpose of this assignment is to create a custom class based on a real world object.  

# This code was written in reference to Professor Hari's lectures, slides, and the car.py example program, as well as the ultimate__fruit_basket.py example. 

# Quick description of this specific class:
#   - This Cat class is intended to simulate a tamagochi-like experience, where users get to create their own cats, and take care of them to earn affection points. 
#   - There are multiple choices of actions that users can choose from, each action resulting in either earning or losing affection points. 
#   - There are 2 useful methods in this class that allows users to check their progress on their cats: get_affection_advice, and get_cat_overview. 

# create the class. 
class Cat:
    # set some class attributes. 
    affection = 0.0
    clean = True
    # initiating the class variables. 
    def __init__(self, name, fur, fav_toy, fav_food): 
        self.name = name
        self.fur = fur
        self.fav_toy = fav_toy
        self.fav_food = fav_food

    # the next few methods are some actions that the user can do with their cat to gain/lose affection, as well as keep them hygenic. 
    def play(self, toy):
        if toy == self.fav_toy:
            self.affection += 0.5
        else:
            self.affection += 0.2
    
    def bath(self):
        self.affection -= 0.3
        self.clean = True 

    def outside(self):
        self.clean = False
 
    def feed(self, food):
        if food == self.fav_food:
            self.affection += 1.0
        else:
            self.affection += 0.4
    
    def pet(self):
        self.affection += 0.1

    def ignore(self):
        self.affection -= 0.5

    # This method allows users to get a sense of mentally healthy, unhealthy their cats are.         
    def get_affection_advice(self):
        print(f"The affeciton level of {self.name} is: {self.affection}. ")
        if self.affection > 10.0:
            print("Wow!! Great job!! your cat is super happy! Best friends for life.")
        if self.affection < -5.0:
            print("OHNO!! Your cat seems unhappy... make sure to give it lots of love and care.")

    # This method gives an overview of the cat the user  wants to look at in an oprganized format. 
    def get_cat_overview(self):
        print (f" Name: {self.name}\n Fur Color: {self.fur}\n Favorite Toy: {self.fav_toy}\n Favorite Food: {self.fav_food}\n Affection Level: {self.affection}\n Is Clean: {self.clean}")

def main():
    # Test code here:
    cat1 = Cat("Sammy", "red", "yarn", "chicken")
    cat1.get_cat_overview()

if __name__ == "__main__":
    main()    
