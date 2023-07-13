def CountStep(start, end, step):
    count = start
    stepping = []
    while True:
        stepping.append(count)
        count += step
        if count >= end:
            stepping.append(count)
            break
    return stepping

Counter = CountStep(0, 50, 1)

def CountNStep(start, end, nstep):
    Ncount = start
    Nstepping = []
    while True:
        Nstepping.append(Ncount)
        Ncount -= nstep
        if Ncount <= end:
            Nstepping.append(Ncount)
            break
    return Nstepping

NCounter = CountNStep(0, -50, 1)