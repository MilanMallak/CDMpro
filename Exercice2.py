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

#opt_profession = {[11, 11, 0, 0, 0, 0], [11, 11, 0, 0, 0, 0], [14, 12, 0, 0, 0, 0], [14, 11, 0, 0, 0, 0], [0, 0, 11, 0, 0, 0], [10, 0, 10, 0, 0, 0], [12, 0, 10, 0, 0, 0], [14, 0, 0, 0, 0, 0],
#                  [0, 0, 0, 0, 10, 0], [0, 14, 14, 0, 10, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 10], [0, 0, 0, 12, 13, 0], [0, 0, 0, 14, 14, 0], [0, 14, 0, 0, 0, 0], [0, 14, 0, 0, 0, 0],
#                  [0, 0, 0, 14, 0, 0], [0, 0, 0, 11, 0, 0], [0, 0, 0, 12, 0, 14], [14, 0, 0, 0, 12, 0], [0, 0, 0, 14, 16, 0], [0, 0, 0, 16, 14, 0], [0, 0, 0, 0, 0, 0], [0, 12, 0, 0, 13, 0]}

# opt_profession = {}                               #    strg, dex, con, intel, wis, cha
Carpenter = np.array([11, 11, 0, 0, 0, 0])          #      11,    11,   0,     0,   0,   0
Stonemason = np.array([11, 11, 0, 0, 0, 0])         #      11,    11,   0,     0,   0,   0
Armorer = np.array([14, 12, 0, 0, 0, 0])            #      14,    12,   0,     0,   0,   0
Blacksmith = np.array([14, 11, 0, 0, 0, 0])         #      14,    11,   0,     0,   0,   0
Farmer = np.array([0, 0, 11, 0, 0, 0])              #      11,     0,  11,     0,   0,   0
Fisherman = np.array([10, 0, 10, 0, 0, 0])          #      10,     0,  10,     0,   0,   0
Miller = np.array([12, 0, 10, 0, 0, 0])             #      12,     0,  10,     0,   0,   0
Butcher = np.array([14, 0, 0, 0, 0, 0])             #      14,     0,   0,     0,   0,   0
Baker = np.array([0, 0, 0, 0, 10, 0])               #       0,     0,   0,     0,  10,   0
Cook = np.array([0, 14, 14, 0, 10, 0])              #       0,    14,  14,     0,  10,   0
Beerbrewer = np.array([0, 0, 0, 0, 0, 0])           #       0,     0,   0,     0,   0,   0
Innkeeper = np.array([0, 0, 0, 0, 0, 10])           #       0,     0,   0,     0,   0,  10
Apothecary = np.array([0, 0, 0, 12, 13, 0])         #       0,     0,   0,    12,  13,   0
Barber_surgeon = np.array([0, 0, 0, 14, 14, 0])     #       0,     0,   0,    14,  14,   0
Shoemaker = np.array([0, 14, 0, 0, 0, 0])           #       0,    14,   0,     0,   0,   0
Tailor = np.array([0, 14, 0, 0, 0, 0])              #       0,    14,   0,     0,   0,   0
Architect = np.array([0, 0, 0, 14, 0, 0])           #       0,     0,   0,    14,   0,   0
Clerk = np.array([0, 0, 0, 11, 0, 0])               #       0,     0,   0,    11,   0,   0
Merchant = np.array([0, 0, 0, 12, 0, 14])           #       0,     0,   0,    12,   0,  14
Bailiff = np.array([14, 0, 0, 0, 12, 0])            #      14,     0,   0,     0,  12,   0
Alchemist = np.array([0, 0, 0, 14, 16, 0])          #       0,     0,   0,    14,  16,   0
Astronomer = np.array([0, 0, 0, 16, 14, 0])         #       0,     0,   0,    16,  14,   0
Candlemaker = np.array([0, 0, 0, 0, 0, 0])          #       0,     0,   0,     0,   0,   0
Scribe = np.array([0, 12, 0, 0, 13, 0])             #       0,    12,   0,     0,  13,   0

def ctrl_rndm_profession():
#    loser = False
#    count = 0
#    for stat in [11, 11, 0, 0, 0, 0]:
#        count += 1
#        if stats[count] < stat:
#            loser  =True
#            break





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
    def __init__(self, strg, dex, con, intel, wis, cha, nom):
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

        #self.profession = placeholder

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