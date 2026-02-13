# exerice de classe 3
#Par Milan Mallak

import random
import names
import numpy as np
from dataclasses import dataclass

valeur = int
opt_genre = ["male", "female"]
genre = random.choice(opt_genre)
opt_species = ["Human", "Elf", "Dwarf"]
species = str
opt_ethnicity = ["Caucasian", "Asian"]
ethnicity = str
rndm_name = str
rndm_profession = str
opt_alignement = ["lawful good", "neutral good", "chaotic good",
                  "lawful neutral", "true neutral", "chaotic neutral",
                  "lawful evil", "neutral evil", "chaotic evil"]
alignement = random.choice(opt_alignement)
alignement = random.choice(opt_alignement)
alignement = str
alignement = str
hitD = int
dmg = int


#                                                   #    strg, dex, con, intel, wis, cha
Carpenter = np.array([10, 11, 0, 0, 0, 0])          #      10,    11,   0,     0,   0,   0
Stonemason = np.array([11, 10, 0, 0, 0, 0])         #      11,    10,   0,     0,   0,   0
Armorer = np.array([14, 12, 0, 0, 0, 0])            #      14,    12,   0,     0,   0,   0
Blacksmith = np.array([14, 11, 0, 0, 0, 0])         #      14,    11,   0,     0,   0,   0
Farmer = np.array([11, 0, 11, 0, 0, 0])              #      11,     0,  11,     0,   0,   0
Fisherman = np.array([10, 0, 10, 0, 0, 0])          #      10,     0,  10,     0,   0,   0
Miller = np.array([12, 0, 10, 0, 0, 0])             #      12,     0,  10,     0,   0,   0
Butcher = np.array([14, 0, 0, 0, 0, 0])             #      14,     0,   0,     0,   0,   0
Baker = np.array([0, 0, 0, 0, 10, 0])               #       0,     0,   0,     0,  10,   0
Cook = np.array([0, 14, 14, 0, 10, 0])              #       0,    14,  14,     0,  10,   0
Beerbrewer = np.array([1, 0, 0, 0, 0, 0])           #       1,     0,   0,     0,   0,   0
Innkeeper = np.array([0, 0, 0, 0, 0, 10])           #       0,     0,   0,     0,   0,  10
Apothecary = np.array([0, 0, 0, 12, 13, 0])         #       0,     0,   0,    12,  13,   0
Barber_surgeon = np.array([0, 0, 0, 14, 14, 0])     #       0,     0,   0,    14,  14,   0
Shoemaker = np.array([0, 14, 0, 0, 1, 0])           #       0,    14,   0,     0,   1,   0
Tailor = np.array([0, 14, 0, 1, 0, 0])              #       0,    14,   0,     1,   0,   0
Architect = np.array([0, 0, 0, 14, 0, 0])           #       0,     0,   0,    14,   0,   0
Clerk = np.array([0, 0, 0, 11, 0, 0])               #       0,     0,   0,    11,   0,   0
Merchant = np.array([0, 0, 0, 12, 0, 14])           #       0,     0,   0,    12,   0,  14
Bailiff = np.array([14, 0, 0, 0, 12, 0])            #      14,     0,   0,     0,  12,   0
Alchemist = np.array([0, 0, 0, 14, 16, 0])          #       0,     0,   0,    14,  16,   0
Astronomer = np.array([0, 0, 0, 16, 14, 0])         #       0,     0,   0,    16,  14,   0
Candlemaker = np.array([0, 0, 0, 0, 1, 0])          #       0,     0,   0,     0,   1,   0
Scribe = np.array([0, 12, 0, 0, 13, 0])             #       0,    12,   0,     0,  13,   0

#Monster "professions"
Melee_fighter = np.array([10, 0, 0, 0, 0, 0])
Ranged_fighter = np.array([0, 10, 0, 0, 0, 0])
Grunt = np.array([0, 0, 0, 0, 0, 0])


profession_dict = {
"[10 11  0  0  0  0]" : "Carpenter",
"[11 10  0  0  0  0]" : "Stonemason",
"[14 12  0  0  0  0]" : "Armorer",
"[14 11  0  0  0  0]" : "Blacksmith",
"[11  0 11  0  0  0]" : "Farmer",
"[10  0 10  0  0  0]" : "Fisherman",
"[12  0 10  0  0  0]" : "Miller",
"[14  0  0  0  0  0]" : "Butcher",
"[ 0  0  0  0 10  0]" : "Baker",
"[ 0 14 14  0 10  0]" : "Cook",
"[1 0 0 0 0 0]" : "Beerbrewer",
"[ 0  0  0  0  0 10]" : "Innkeeper",
"[ 0  0  0 12 13  0]" : "Apothecary",
"[ 0  0  0 14 14  0]" : "Barber surgeon",
"[ 0 14  0  0  1  0]" : "Shoemaker" ,
"[ 0 14  0  1  0  0]" : "Tailor",
"[ 0  0  0 14  0  0]" : "Architect",
"[ 0  0  0 11  0  0]" : "Clerk",
"[ 0  0  0 12  0 14]" : "Merchant",
"[14  0  0  0 12  0]" : "Bailiff",
"[ 0  0  0 14 16  0]" : "Alchemist",
"[ 0  0  0 16 14  0]" : "Astronomer",
"[0 0 0 0 1 0]" : "Candlemaker",
"[ 0 12  0  0 13  0]" : "Scribe",
#Monster "professions"
"[10  0  0  0  0  0]" : "Melee fighter",
"[ 0 10  0  0  0  0]" : "Ranged fighter",
"[0 0 0 0 0 0]" : "Grunt"
}

opt_profession = [Carpenter, Stonemason, Armorer, Blacksmith, Farmer, Fisherman, Miller, Butcher, Baker, Cook, Beerbrewer, Innkeeper, Apothecary, Barber_surgeon, Shoemaker, Tailor, Architect, Clerk, Merchant, Bailiff, Alchemist, Astronomer, Candlemaker, Scribe]
ctrl_opt_profession = []

def rndm_attribut():
    global valeur
    ld = []
    for a in range(4):
        ld.append(random.randint(1, 6)) # lancé de dés 6
    ld.sort(reverse = True)
    valeur = ld[0] + ld[1] + ld[2] # les trois meilleurs
    return valeur

def rndmz_name():
    global rndm_name

    if genre == "male" :
        rndm_first_name = names.get_first_name(gender = "male")
    elif genre == "female" :
        rndm_first_name = names.get_first_name(gender = "female")

    rndm_last_name = names.get_last_name()
    rndm_name = rndm_first_name + " " + rndm_last_name
    return rndm_name

def rndmz_species():
    global rndm_species
    rndm_species= random.choice(opt_species)
    return rndm_species

def rndmz_ethnicity():
    global rndm_ethnicity
    if rndm_species in ("Human", "Elf", "Dwarf"):
        rndm_ethnicity = random.choice(opt_ethnicity)
    else:
        rndm_ethnicity = "N/A"
    return rndm_ethnicity

def ctrl_rndmz_profession():
    global rndm_profession
    global rndm_profession_code
    global rndm_species
    ctrl_opt_profession = []
    if rndm_species in ("Human", "Elf", "Dwarf"):
        for i in opt_profession:
            if (stats >= i).all():
                ctrl_opt_profession.append(i)
    else: #for monsters
        if (stats >= Melee_fighter).all():
            ctrl_opt_profession.append(Melee_fighter)
        elif (stats >= Ranged_fighter).all():
            ctrl_opt_profession.append(Ranged_fighter)
        else:
            ctrl_opt_profession.append(Grunt)

    rndm_profession_code = str(random.choice(ctrl_opt_profession))
    rndm_profession = (profession_dict.get(rndm_profession_code))
    return rndm_profession

def rndmz_alignement():
    global rndm_alignement
    rndm_alignement = random.choice(opt_alignement)
    return rndm_alignement


@dataclass
class Item:
    name: str
    qty: int

class Inventory :
    def __init__(self,):
        self.liste_item = []
    def add(self,):
        label = Item(label, )
        if item.name in self.liste_item:
            item.qty += nbr
        else :
            self.liste_item.append(item.name)
    def remove(self,):
        if item.name in self.liste_item:
            if item.qty <= nbr
                self.liste_item.remove(item.name)
            else :
                item.qty -= nbr
    def show(self):
        print(self.liste_item)


class NPC :
    def __init__(self, strg, dex, con, intel, wis, cha, nom, species, ethnicity, profession, alignement,):
        self.strg = strg
        self.dex = dex
        self.con = con
        self.intel = intel
        self.wis = wis
        self.cha = cha

        self.HP = random.randint(1, 20) # dé 20
        self.ac = random.randint(1, 12) # dé 12

        self.genre = genre
        self.nom = nom

        self.species = species
        self.ethnicity = ethnicity

        self.profession = profession

        self.alignement = alignement

        self.backpack = Inventory()



    def details(self):
        print(
            f"Name: {self.nom}\n"
            f"Species: {self.species} | Ethnicity: {self.ethnicity}\n"
            f"Profession: {self.profession}\n"
            f"Genre: {self.genre}\n"
            f"HP: {self.HP} | AC: {self.ac}\n"
            f"STR: {self.strg} DEX: {self.dex} CON: {self.con}\n"
            f"INT: {self.intel} WIS: {self.wis} CHA: {self.cha}\n"
            f"Alignment: {self.alignement}"
        )

    def HPverif(self):
        global dead
        dead = False
        if self.HP <= 0 :
            dead = True
        return dead

class Hero(NPC) :
    def attack(self, target):
        global hitD
        global crit
        hitD = random.randint(1, 20)
        if hitD == 20 :
            crit = True
            kobold.hit()
        elif hitD == 1 :
            crit = False
        else :
            crit = False
            target.hit()
    def hit(self):
        global hitD
        global hitIndicater
        global crit
        global dmg
        dmg = 0
        if crit == True:
            dmg = random.randint(1, 8)
            self.HP -= dmg
        elif 1 < hitD <= 19:
            if hitD >= self.ac:
                hitIndicater = True
                dmg = random.randint(1, 6)
                self.HP -= dmg
        else:
            hitIndicater = False

class Kobold(NPC) :
    def attack(self, target):
        global hitD
        global crit
        hitD = random.randint(1, 20)
        if hitD == 20:
            crit = True
            kobold.hit()
        elif hitD == 1:
            crit = False
        else:
            crit = False
            target.hit()
    def hit(self):
        global hitD
        global hitIndicater
        global crit
        global dmg
        dmg = 0
        if crit == True :
            dmg = random.randint(1,8)
            self.HP -= dmg
        elif 1 < hitD <= 19 :
            if hitD >= self.ac :
                hitIndicater = True
                dmg = random.randint(1, 6)
                self.HP -= dmg
        else :
            hitIndicater = False


strg = rndm_attribut()
dex = rndm_attribut()
con = rndm_attribut()
intel = rndm_attribut()
wis = rndm_attribut()
cha = rndm_attribut()

stats = np.array([strg, dex, con, intel, wis, cha])

hero = Hero(strg, dex, con, intel, wis, cha, rndmz_name(), rndmz_species(), rndmz_ethnicity(), ctrl_rndmz_profession(), rndmz_alignement())
hero.details()

print("\n")

strg = rndm_attribut()
dex = rndm_attribut()
con = rndm_attribut()
intel = rndm_attribut()
wis = rndm_attribut()
cha = rndm_attribut()

stats = np.array([strg, dex, con, intel, wis, cha])

genre = random.choice(opt_genre)

rndm_species = "Kobold"
kobold = Kobold(strg, dex, con, intel, wis, cha, "N/A", "Kobold", rndmz_ethnicity(), ctrl_rndmz_profession(), rndmz_alignement())
kobold.details()


print("\n")

#input("Paisez ENTER pour commencé le combats\n")
#while True:
#    print(f"{hero.nom} attack le Kobold")
#    hero.attack(kobold)
#    if crit == True :
#        print(f"le/la Kobold se prend un coup critique et perd {dmg} point de vie. Il/Elle lui reste maintenant {kobold.HP}HP")
#    elif hitIndicater == True :
#        print(f"le/la Kobold se prend un coup et perd {dmg} point de vie. Il/Elle lui reste maintenant {kobold.HP}HP")
#    else :
#        print(f"l'attaque manque le Kobold")
#
#    if kobold.HPverif() == True :
#        break
#
#    print(f"c'est maintenant le tour du Kobold"
#          f"Le Kobold attack {hero.nom}")
#    kobold.attack(hero)
#    if crit == True :
#        print(f"l'héro/ïne se prend un coup critique et perd {dmg} point de vie. Il/Elle lui reste maintenant {hero.HP}HP")
#    elif hitIndicater == True :
#        print(f"l'héro/ïne se prend un coup et perd {dmg} point de vie. Il/Elle lui reste maintenant {hero.HP}HP")
#    else :
#        print(f"l'attaque manque l'héro/ïne")
#
#    if hero.HPverif() == True :
#        break
#
#    print(f"c'est maintenant le tour de {hero.nom}")
#
#if kobold.HP <= 0 :
#    print(f"{hero.nom} vain son adversaire!")
#else :
#    print(f"{hero.nom} a péri")

print("Paisez ENTER pour commencé le combats\n"
      "Écrivez : Add [quantité de votre choix] de [item de votre choix]\n"
      "pour ajouter un item à l'inventaire du Héro\n"
      "Écrivez : Remove [quantité de votre choix] de [item de votre choix]\n"
      "pour enlever un item de l'inventaire du Héro\n"
      "Cliquez I pour voir l'inventaire")
while True:
    player_action = str(input("\n"))

    if "Add" in player_action or "add" in player_action:
        info = player_action.split()
        hero.backpack.add(info[4], info[1])
    elif "Remove" in player_action or "remove" in player_action:
        info = player_action.split()
        hero.backpack.remove(info[4], info[1])
    elif player_action == "I" or player_action == "i":
        print("code works 3")
    elif player_action == (""):
        print("code works 4")

item = Item("stick", 3)

inventory = Inventory()

inventory.add(item)
inventory.show()
