
def countingValleys(steps, path):
    currentLevel=0
    NumberOfValley=0
    for steps in path:
        if steps=="D":
            currentLevel-=1
            if currentLevel==-1:
                NumberOfValley+=1
        elif steps=="U":
            currentLevel+=1
    return NumberOfValley
        
