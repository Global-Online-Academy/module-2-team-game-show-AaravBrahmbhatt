import random

hist4 = [("split","steal"),("steal","steal"),("split","steal"),("steal","split"),("split","split"),("steal","split")]

def codecrafters1(history):
    if len(history) == 0:
        action = "steal"
    
    elif len(history) < 30:
        action = random.choice(["steal", "steal","split"])

    elif len(history) >=30:
        for action in range(len(history)):
                Opponentlastmove = history[-1]
                Nextmove = Opponentlastmove[1]
                action = Nextmove
    elif len(history) >= 60:
        percentage = random.randint(1,10)
        if percentage <= 7:
            action = "steal"
        else: 
            action = "split"
    elif len(history) >= 90:
        OpponentSplit = 0
        OpponentSteal = 0
        OpponentPercent = 0
        for r in history:
            (me,them) = r
            if them == "split":
                OpponentSplit += 1
            elif them == "steal":
                OpponentSteal += 1
        OpponentPercent1 = OpponentSplit / (OpponentSteal + OpponentSplit)
        OpponentPercent2 = OpponentSteal / (OpponentSteal + OpponentSplit)
        if OpponentPercent1 > OpponentPercent2:
            percentage2 = random.randint(1,20)
            if percentage2 >= 15:
                action = "steal"
            else:
                action = "split"
    elif len(history) >= 120:
        percentage = random.randint(1,10)
        if percentage >= 7:
            action = Nextmove
        else: 
            action = random.choice(["steal","split"])
    elif len(history) >= 150:
                
        opponent25previous = history[-25:]

        newMoves = []

        for r in history:

            opponentMoves = r
                
        newMoves.append(opponentMoves)
        splitCount = 0
        stealCount = 0
        for m in newMoves:
            if m == "split":
                splitCount += 1
            else:
                stealCount += 1
            if splitCount > stealCount:
                percentage3 = random.randint(1,20)
                if percentage3 >= 17:
                    action = "split"
            elif stealCount > splitCount:
                action = "steal"
            else:
                action = "steal"
    elif len(history) >= 180:
            Opponentlastmove = history[-1]
            Nextmove = Opponentlastmove[1]
            action = Nextmove
    else:
        if len(history) % 5 == 0:
            action = random.choice(["steal", "steal","split"])
                
        if len(history) % 20 == 0:
            action = random.choice(["steal", "steal", "steal", "steal", "split", "split"])
    return action
print(codecrafters1(hist4))


