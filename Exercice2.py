# exerice de classe 2
#Par Milan Mallak

import random
import names
import numpy as np

valeur = int
opt_genre = ["male", "female"]
genre = str
rndm_name = str

rndm_profession = str


#                                                   #    strg, dex, con, intel, wis, cha
Carpenter = np.array([10, 11, 0, 0, 0, 0])          #      10,    11,   0,     0,   0,   0
Stonemason = np.array([11, 10, 0, 0, 0, 0])         #      11,    10,   0,     0,   0,   0
Armorer = np.array([14, 12, 0, 0, 0, 0])            #      14,    12,   0,     0,   0,   0
Blacksmith = np.array([14, 11, 0, 0, 0, 0])         #      14,    11,   0,     0,   0,   0
Farmer = np.array([0, 0, 11, 0, 0, 0])              #      11,     0,  11,     0,   0,   0
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

prof_dict = {
"Carpenter": [10, 11, 0, 0, 0, 0],
"Stonemason": [11, 10, 0, 0, 0, 0],
"Armorer": [14, 12, 0, 0, 0, 0],
"Blacksmith": [14, 11, 0, 0, 0, 0],
"Farmer": [11, 0, 11, 0, 0, 0],
"Fisherman": [10, 0, 10, 0, 0, 0],
"Miller": [12, 0, 10, 0, 0, 0],
"Butcher": [14, 0, 0, 0, 0, 0],
"Baker": [1, 0, 0, 0, 10, 0],
"Cook": [0, 14, 14, 0, 10, 0],
"Beerbrewer": [0, 0, 0, 0, 0, 0],
"Innkeeper": [0, 0, 0, 0, 0, 10],
"Apothecary": [0, 0, 0, 12, 13, 0],
"Barber_surgeon": [0, 0, 14, 14, 0, 0],
"Shoemaker": [0, 14, 0, 0, 1, 0],
"Tailor": [0, 14, 0, 1, 0, 0],
"Architect": [0, 0, 0, 14, 0, 0],
"Clerk": [0, 0, 0, 11, 0, 0],
"Merchant": [0, 0, 0, 12, 0, 14],
"Bailiff": [14, 0, 0, 0, 12, 0],
"Carpenter": [11, 11, 0, 0, 0, 0],
"Alchemist": [0, 0, 0, 14, 16, 0],
"Astronomer": [0, 0, 0, 16, 14, 0],
"Candlemaker": [0, 0, 0, 0, 1, 0],
"Scribe": [0, 12, 0, 0, 13, 0]
}
invert_prof_dict = {str(value): key for key, value in prof_dict.items()}

opt_profession = [Carpenter, Stonemason, Armorer, Blacksmith, Farmer, Fisherman, Miller, Butcher, Baker, Cook, Beerbrewer, Innkeeper, Apothecary, Barber_surgeon, Shoemaker, Tailor, Architect, Clerk, Merchant, Bailiff, Alchemist, Astronomer, Candlemaker, Scribe]
ctrl_opt_profession = []
prof_count = int

def ctrl_rndm_profession():
    global rndm_profession

    for i in opt_profession:
        if (stats >= i).all():
            ctrl_opt_profession.append(i)

    rndm_profession = random.choice(ctrl_opt_profession)


def rndm_attribut():
    global valeur
    ld = []
    for a in range(4):
        ld.append(random.randint(1, 6)) # lancé de dés 6
    ld.sort(reverse = True)
    valeur = ld[0] + ld[1] + ld[2] # les trois meilleurs

def rndm_caracteristics():
    global rndm_name

    if genre == "male" :
        rndm_first_name = names.get_first_name(gender = "male")
    else :
        rndm_first_name = names.get_first_name(gender="female")

    rndm_last_name = names.get_last_name()
    rndm_name = rndm_first_name + " " + rndm_last_name
    return rndm_name

class NPC :
    def __init__(self, strg, dex, con, intel, wis, cha, nom, profession):
        self.strg = strg
        self.dex = dex
        self.con = con
        self.intel = intel
        self.wis = wis
        self.cha = cha

        self.HP = random.randint(1, 20) # dé 20
        self.ac = random.randint(1, 12) # dé 12

        self.genre = random.choice(opt_genre)
        self.nom = nom

        #self.species = placeholder
        #self.ethnicity = placeholder

        self.profession = profession

rndm_attribut()
NPC.strg = valeur
rndm_attribut()
NPC.dex = valeur
rndm_attribut()
NPC.con = valeur
rndm_attribut()
NPC.intel = valeur
rndm_attribut()
NPC.wis = valeur
rndm_attribut()
NPC.cha = valeur

NPC.nom = rndm_caracteristics()

print(NPC.strg, NPC.dex, NPC.con, NPC.intel, NPC.wis, NPC.cha, NPC.nom)

stats = np.array([NPC.strg, NPC.dex, NPC.con, NPC.intel, NPC.wis, NPC.cha])

ctrl_rndm_profession()
print(invert_prof_dict[str(rndm_profession)])