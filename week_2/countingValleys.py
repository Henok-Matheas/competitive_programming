def countingValleys(steps, path):
    
    direction = {'U':1,
    'D':-1}
    place = 0
    valley = 0
    
    for i in range(len(path)):
        if place == 0 and place+direction[path[i]] == -1:
            valley += 1
        place+=direction[path[i]]
    return valley