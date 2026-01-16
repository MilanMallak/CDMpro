#test zone

import numpy as np

#a = np.array([11, 11, 0, 0, 8, 1])
#b = np.array([18, 18, 18, 18, 18, 0])
#
#if (a > b).any() :
#    print("Horrayy!!")

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


opt_profession = [Carpenter, Stonemason, Armorer, Blacksmith, Farmer, Fisherman, Miller, Butcher, Baker, Cook, Beerbrewer, Innkeeper, Apothecary, Barber_surgeon, Shoemaker, Tailor, Architect, Clerk, Merchant, Bailiff, Alchemist, Astronomer, Candlemaker, Scribe]
ctrl_opt_profession = []
prof_count = int

stats = np.array([0, 0, 0, 0, 0, 0])

#def ctrl_rndm_profession():
#    prof_count = 0
#    while prof_count < 20 :
#        if (stats >= opt_profession[prof_count]).any() :
#            ctrl_opt_profession.append(opt_profession[prof_count])
#        prof_count =+ 1

def ctrl_rndm_profession():
    for i in opt_profession:
        if (stats >= i).all():
            ctrl_opt_profession.append(i)


ctrl_rndm_profession()
print(ctrl_opt_profession)