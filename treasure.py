
"""this module contains funktions to roll for treasure
treasure is a ADT with the following structure
{
'kc':0, 'sc':0, 'gc':0, 'pc':0,
'jewels':{
          '"jewel_type"':(
                          price, cut_level,
                          color, quality, weightingrams
                          )
          }
}
"""


import dice as D
import random as R


def gem_quality_mod(base_price, quality):
    """function to modify the base price of a gem based on the
    quality of the gem 
    """
    if quality in range(1, 6) and type(quality) == int:
        
        if quality == 1:
            return base_price * 0.4

        elif quality == 2:
            return base_price * 0.6

        elif quality == 3:
            return base_price * 1.5

        elif quality == 4:
            return base_price * 2.5

        elif quality == 5:
            return base_price * 5

    elif not type(quality) == int:
        print("ERROR: pleace use int type to define clarity")

    elif quality not in range(1, 6):
        print("ERROR: pleace use a number between 1 and 5 to signify clarity")      

    else:
        print("ERROR unknown malfunction")


def gem_color_mod(color, price):
    """function to modify price based on color quality of the gem
    """
    if type(color) == int and color in range(1, 11):
        return price * color
    elif not type(color) == int:
        print("ERROR: pleace use int type to define color")
    elif not color in range(1, 11):
        print("ERROR: pleace use a number between 1 and 10 to signify color")
    else:
        print("ERROR: unknown malfunction")

def cut_mod(cut, price):
    """function to modify price of a gem based on the quality of the cut
    """
    if type(cut) == int and cut in range(1, 6):
        if cut == 1:
            return price * 0.5
        elif cut == 2:
            return price
        elif cut == 3:
            return price * 2
        elif cut == 4:
            return price * 5
        elif cut == 5:
            return price * 10
    elif not type(cut) == int:
        print("ERROR: pleace use int to define cut level")
    elif not cut in range(1, 6):
        print("ERROR: pleace use a number between 1 and 5 to signify cut")
    else:
        print("ERROR: unknown malfunction")


def diamond_value(carat, quality, color, cut=0):
    """funtion to calculate the price of a diamond in silver coins
    if the diamond is cut the function returns a tuple (price, new_carat)
    else the function return the value of the raw diamond_value
    
    carat is the weight of diamond in carat (1 carat = 0.2g)
    
    quality is the amount of impurities in the diamond and is denoted by a 
        value between 1(impuritiesand or flaws visible to the naked eye)
        and 5(flawless)
    
    color is the color quality if the diamond
        and is a value between 1 (worst) and 10(perfect)

    cut if cut is == 0 (base case) the diamond is uncut 
        if the diamond is cut the level of craftmanship is denoted 
        by a number between 1(poorly skilled novice)
        and 5(renowned master cutter)
        cutting the diamond
        will reduce the carat of the stone by roughly two thirds
    """
    if type(carat) == int or type(carat) == float:
        procent = carat / 5000
        base_price = 140000000 * procent ** 2
    else:
        print("ERROR: pleace use int or float to define carat")
    
    temp_price = gem_quality_mod(base_price, quality)
    price = gem_color_mod(color, temp_price)
    if not cut == 0:
        price = cut_mod(cut, diamond_value(carat*0.33, quality, color))
        return (price, carat * 0.33)
    return price



def what_is_this_gem_worth(gem_type, carat, quality, color, cut_level=0):
    """this funtion returns the value of a gem
    it takes the following arguments:
    gem_type = string 
    carat = the weight of the gem in carat 1 carat = 0.2g
    quality = an int between 1 and 5
    color = an int between 1 and 10
    cut_level = 0 for uncut gems if cut add a number between 1 and 5 
    """
    if gem_type.lower() == "diamond":
        if type(carat) == int or type(carat) == float:
            procent = carat / 5000
            base_price = 140000000 * procent ** 2
            print("base price before mods= " + str(base_price))
        else:
            print("ERROR: pleace use int or float to define carat")
    temp_price = gem_quality_mod(base_price, quality)
    price = gem_color_mod(color, temp_price)
    if not cut_level == 0:
        price = cut_mod(cut_level, price)
    return price


def find_carat(jewel_type):
    """this function takes a string with a jewel type as argument
    and returns a randomly assigned weigh in carat
    """
    if jewel_type.lower() == 'diamond':
        roll = R.randint(1, 63840)
        if roll <= 100:
            return 10
        elif roll <= 210:
            return 9.5
        elif roll <= 333:
            return 9
        elif roll <= 471:
            return 8.5
        elif roll <= 627:
            return 8
        elif roll <= 804:
            return 7.5
        elif roll <= 1008:
            return 7
        elif roll <= 1244:
            return 6.5
        elif roll <= 1521:
            return 6
        elif roll <= 1851:
            return 5.5
        elif roll <= 2251:
            return 5
        elif roll <= 2744:
            return 4.5
        elif roll <= 3369:
            return 4
        elif roll <= 4185:
            return 3.5
        elif roll <= 5296:
            return 3
        elif roll <= 6896:
            return 2.5
        elif roll <= 9396:
            return 2
        elif roll <= 13840:
            return 1.5
        elif roll <= 23840:
            return 1
        elif roll <= 63840:
            return 0.5
    
 
def find_jewel_type():
    """ This function returns a jewel chosen at random
    """
    roll = D.hundred()
    if roll <= 25:
        gem_list = ['Banded eye', 'Agate', 'Azurite', 'Quartz',
                    'Hematite', 'Lapis lazuli', 'Malachite', 'Obsidian',
                    'Rhodochrosite', 'Tiger eye', 'Turquoise',
                    'Pearl'
                    ]
        gem = R.choice(gem_list)
        return gem

    elif roll <= 50:
        gem_list = ['Bloodstone', 'Carnelian', 'Chalcedony', 'Chrysoprace',
                    'citrine', 'Iolite', 'Jasper', 'Moonstone', 'Onyx',
                    'Peridot', 'Rock crystal (clear quartz)', 'Sard',
                    'Sardonyx', 'Quarts',
                    'Quarts', 'Zircon'
                    ]
        gem = R.choice(gem_list)
        return gem

    elif roll <= 70:
        gem_list = ['Amber', 'Amethyst', 'Chrysoberyl', 'Coral', 'Garnet',
                    'Garnet', 'jade', 'jet',
                    'Pearl', 'Spinel', 'Tourmaline'
                    ]
        gem = R.choice(gem_list)
        return gem

    elif roll <= 90:
        gem_list = ['Alexandrite', 'Aquamarine', 'Garnet',
                    'Pearl', 'Spinel', 'Topas'
                    ]
        gem = R.choice(gem_list)
        return gem

    elif roll <= 99:
        gem_list = ['Emerald', 'Opal', 'Opal', 'Opal',
                    'Sapphire', 'Corundum',
                    'Corundum', 'Sapphire',
                    'Sapphire', 'Ruby'
                    ]
        gem = R.choice(gem_list)
        return gem

    elif roll <= 100:
        gem_list = ['Diamond']
        gem = R.choice(gem_list)
        return gem




def create_jewel():
    jewel_type = find_jewel_type()
    carat = find_carat(jewel_type)
    quality = find_quality(jewel_type)
    color = find_color(jewel_type)
    cut_level = find_cut_level()

    if jewel_type.lower() == 'diamond':
        price = diamond_value(carat, quality, color, cut)
        if type(price) == tuple:
            carat = price[1]
            price = price[0]

    return {'jewel_type':(
                          price, cut_level,
                          color, quality, carat*0.2
                          )
            }



def t1():
    """this function creates a treasure representing an average
    citicens likly pocket coinage
    """
    sc = D.d4(-1)
    kc = D.d10()
