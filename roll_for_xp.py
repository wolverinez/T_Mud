
import dice as D

def test_20roll(stat, roll):
    if stat <= 20:
        
        return 0
    else:
        roll = D.d20()
        
        if roll == 20:
            return test_20roll(stat-20, roll)
        elif roll <= stat - 20:
            
            return 1
        else:
            
            return 0

def roll_for_xp(rolls, stat, teacherbonus=0):
    count = 0
    for i  in range(rolls):
        roll = D.d20()
       
        if roll == 20:
            count += test_20roll(stat, roll)
        elif roll == 1:
            xproll = D.d3(1)
            
            count += xproll
        elif roll < 20:
            roll = roll - teacherbonus
            if roll <= stat:
                
                count += 1
    return count




def how_many_rolls_for_xp(xp_needed, stat, with_teacher = False):
    xp = 0
    roll = 0
    while True:
        if xp < xp_needed:
            xp += roll_for_xp(1, stat)
            roll += 1
        else:
            break
    if with_teacher == True:
        return "xp =" + str(xp) + "\nweeks: " + str(roll/2)
    else:
        return "xp =" + str(xp) + "\nweeks: " + str(roll)


            
            
