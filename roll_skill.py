import dice as D


def test_20roll(fv, roll):
    if fv <= 20:
        return "critical faliure"
    else:
        roll = D.d20()
        if roll == 20:
            return test_20roll(fv-20, roll)
        elif roll <= fv - 20:
            return "success"
        else:
            return "faliure"


def roll_skill(fv):
    roll = D.d20()

    if roll == 1:
        return "perfect"
    elif roll == 20:
        return test_20roll(fv, roll)
    elif roll <= fv:
        return "success"
    else:
        return "faliure"



def test_roll_skill(fv):
    i = 1
    skill_roll = roll_skill(fv)
    while True:
        if skill_roll == "critical faliure":
            break
        skill_roll = roll_skill(fv)
        i += 1
    return i
