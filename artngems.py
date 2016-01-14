 
def gems():
    """ This function returns a Gem and calculated value of the gem
    """
    roll = D.hundred()
    if roll <= 25:
        gem_list = ['Banded eye', 'Moss agate', 'Azurite', 'Blue quartz',
                    'Hematite', 'Lapis lazuli', 'Malachite', 'Obsidian',
                    'Rhodochrosite', 'Tiger eye', 'Turquoise',
                    'Pearl (freshwater irregular)'
                    ]
        gem = R.choice(gem_list)
        return gem
 
    elif roll <= 50:
        gem_list = ['Bloodstone', 'Carnelian', 'Chalcedony', 'Chrysoprace',
                    'citrine', 'Iolite', 'Jasper', 'Moonstone', 'Onyx',
                    'Peridot', 'Rock crystal (clear quartz)', 'Sard',
                    'Sardonyx', 'Rose quarts', 'Smoky quarts',
                    'Star rose quarts', 'Zircon'
                    ]
        gem = R.choice(gem_list)
        return gem

    elif roll <= 70:
        gem_list = ['Amber', 'Amethyst', 'Chrysoberyl', 'Coral', 'Red Garnet',
                    'Brown-green Garnet', 'jade', 'jet', 'White Pearl',
                    'Golden Pearl', 'Pink Pearl', 'Silver Pearl', 'Red Spinel',
                    'Red-brown Spinel', 'Deep green Spinel', 'Tourmaline'
                    ]
        gem = R.choice(gem_list)
        return gem

    elif roll <= 90:
        gem_list = ['Alexandrite', 'Aquamarine', 'Violet Garnet',
                    'Black Pearl', 'Deep blue Spinel', 'Golden yellow Topas'
                    ]
        gem = R.choice(gem_list)
        return gem

    elif roll <= 99:
        gem_list = ['Emerald', 'White Opal', 'Black Opal', 'Fire Opal',
                    'Blue Sapphire', 'Fiery yellow Corundum',
                    'Rich purple Corundum', 'Blue star Sapphire',
                    'Black star Sapphire', 'Star Ruby'
                    ]
        gem = R.choice(gem_list)
        return gem

    elif roll <= 100:
        gem_list = ['Clearest bright green Emerald',
                    'Blue-white Canary', 'Pink Diamond', 'Brown Diamond',
                    'Blue Diamond', 'Jacinth'
                    ]
        gem = R.choice(gem_list)
        return gem
 
 
def art():
    """ This function returns a peice of art and calculated value of it
    """
    roll = D.hundred()
    if roll <= 10:
        art_list = ['Silver ewer', 'Carved bone', 'Ivory statuette',
                    'Finely wrought small gold bracelet'
                    ]
        art = R.choice(art_list)
        value = 0
        for i in range(1):
            value += D.ten()
        value = value * 10
        return art + " worth " + str(value) + " Gp"
 
    elif roll <= 25:
        art_list = ['Cloth of gold vestments', 
                    'black velvet mask with numerous citrines',
                    'silver chalice with lapis lazuli gems'
                    ]
        art = R.choice(art_list)
        value = 0
        for i in range(3):
            value += D.six()
        value = value * 10
        return art + " worth " + str(value) + " Gp"   
 
    elif roll <= 40:
        art_list = ['Large well-done wool tapestry', 
                    'brass mug with jade inlays',
                    ]
        art = R.choice(art_list)
        value = 0
        for i in range(1):
            value += D.six()
        value = value * 100
        return art + " worth " + str(value) + " Gp"   
 
    elif roll <= 50:
        art_list = ['Silver comb with moonstones', 
                    'silver-plated steel longsword with jet jewel in hilt',
                    ]
        art = R.choice(art_list)
        value = 0
        for i in range(1):
            value += D.ten()
        value = value * 100
        return art + " worth " + str(value) + " Gp"   
 
    elif roll <= 60:
        art_list = ['Carved harp of exotic wood with ivory inlay and zircon'
                    ' gems', 'solid gold idol (10 lb.)'
                    ]
        art = R.choice(art_list)
        value = 0
        for i in range(2):
            value += D.six()
        value = value * 100
        return art + " worth " + str(value) + " Gp"
 
    elif roll <= 70:
        art_list = ['Gold dragon comb with red garnet eye',
                    'Gold and topaz bottle stopper cork', 
                    'Ceremonial electrum dagger with a star ruby in the pommel'
                    ]
        art = R.choice(art_list)
        value = 0
        for i in range(3):
            value += D.six()
        value = value * 100
        return art + " worth " + str(value) + " Gp"
 
    elif roll <= 80:
        art_list = ['Eyepatch with mock eye of sapphire and moonstone',
                    'fire opal pendant on a fine gold chain', 
                    'old masterpiece painting'
                    ]
        art = R.choice(art_list)
        value = 0
        for i in range(4):
            value += D.six()
        value = value * 100
        return art + " worth " + str(value) + " Gp"
 
    elif roll <= 85:
        art_list = ['Embroidered silk and velvet mantle with'
                    ' numerous moonstones',
                    'sapphire pendant on gold chain', 
                    ]
        art = R.choice(art_list)
        value = 0
        for i in range(5):
            value += D.six()
        value = value * 100
        return art + " worth " + str(value) + " Gp"
 
    elif roll <= 90:
        art_list = ['Embroidered and bejeweled glove',
                    'jeweled anklet', 'gold music box'
                    ]
        art = R.choice(art_list)
        value = 0
        for i in range(1):
            value += D.four()
        value = value * 1000
        return art + " worth " + str(value) + " Gp"
 
    elif roll <= 95:
        art_list = ['Golden circlet with four aquamarines',
                    'a string of small pink pearls (necklace)'
                    ]
        art = R.choice(art_list)
        value = 0
        for i in range(1):
            value += D.six()
        value = value * 1000
        return art + " worth " + str(value) + " Gp"
 
    elif roll <= 99:
        art_list = ['Jeweled gold crown', 'jeweled electrum ring']
        art = R.choice(art_list)
        value = 0
        for i in range(2):
            value += D.four()
        value = value * 1000
        return art + " worth " + str(value) + " Gp"
 
    elif roll <= 100:
        art_list = ['Gold and ruby ring', 'gold cup set with emeralds']
        art = R.choice(art_list)
        value = 0
        for i in range(2):
            value += D.six()
        value = value * 1000
        return art + " worth " + str(value) + " Gp"