# -----------------------------------------------------------------------------------------------------------------------------------------------------------
# 3) (a) (i)
class Animal():
    def __init__(self, name, sound, size, intelligence):
        self.Name = name # String
        self.Sound = sound # String
        self.Size = size # Integer
        self.Intelligence = intelligence # Integer

    # -------------------------------------------------------------------------------------------------------------------------------------------------------
    # 3) (a) (ii)
    def Description(self):
        return f"The animal's name is {self.Name}, it makes a {self.Sound}, its size is {self.Size} and its intelligence level is {self.Intelligence}"
    
    # -------------------------------------------------------------------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------------------------------------------------------------------   
# 3) (b) (i)
class Parrot(Animal):
    def __init__(self, name, sound, size, intelligence, wingspan, numberwords):
        super().__init__(name, sound, size, intelligence)
        self.WingSpan = wingspan # Integer
        self.NumberWords = numberwords # Integer

    def ChangeNumberWords(self, addwords):
        self.NumberWords += addwords

    # -------------------------------------------------------------------------------------------------------------------------------------------------------
    # 3) (b) (ii)
    def Description(self):
        return f"{super().Description()}. It has a wingspan of {self.WingSpan}cm and can say {self.NumberWords} words."
    
    # -------------------------------------------------------------------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------------------------------------------------------------------   
# 3) (c) (i)
class Wolf(Animal):
    def __init__(self, name, sound, size, intelligence, territorysize):
        super().__init__(name, sound, size, intelligence)
        self.TerritorySize = territorysize

    def SetTerritorySize(self, addterritory):
        self.TerritorySize += addterritory

    # -------------------------------------------------------------------------------------------------------------------------------------------------------
    # 3) (c) (ii)
    def Description(self):
        return f"{super().Description()}. Its territory is {self.TerritorySize} square miles."
    
    # -------------------------------------------------------------------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------------------------------------------------------------------   
# 3) (d) (i)
new_parrot = Parrot("Chewie", "Squawk", 1, 10, 30, 29)
new_wolf = Wolf("Nighteyes", "Howl", 8, 7, 100)
new_horse = Animal("Copper", "Neigh", 10, 6)

# -----------------------------------------------------------------------------------------------------------------------------------------------------------   

# -----------------------------------------------------------------------------------------------------------------------------------------------------------   
# 3) (d) (ii)
new_wolf.SetTerritorySize(-20)
new_parrot.ChangeNumberWords(2)
print(new_parrot.Description())
print(new_wolf.Description())
print(new_horse.Description())

# -----------------------------------------------------------------------------------------------------------------------------------------------------------   
